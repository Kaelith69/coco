import sys
import torch
import yaml
import cv2
import threading
import os
from datetime import datetime
import pathlib

# Patch for Windows: torch.hub loads models saved on Linux which use PosixPath.
# On Windows, PosixPath cannot be instantiated, so we remap it to WindowsPath.
if sys.platform == "win32":
    pathlib.PosixPath = pathlib.WindowsPath

# Resolve the model path relative to this script's directory so the code works
# regardless of the working directory or operating system.
_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
_DEFAULT_MODEL_PATH = os.path.join(
    _BASE_DIR,
    "AIYolov5", "content", "yolov5", "runs", "train",
    "yolov5s_results", "weights", "best.pt",
)
_YAML_PATH = os.path.join(_BASE_DIR, "AIYolov5", "data.yaml")
_SAVE_DIR = os.path.join(_BASE_DIR, "CoconutDetection Pictures")
_WINDOW_NAME = "Coconut Detection"
_CONF_THRESHOLD = 0.67


def save_image(frame):
    """Save *frame* as a timestamped JPEG in the detections output directory."""
    os.makedirs(_SAVE_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    image_name = f"coconut_detection_{timestamp}.jpg"
    image_path = os.path.join(_SAVE_DIR, image_name)
    cv2.imwrite(image_path, frame)
    print(f"Image saved: {image_path}")


def load_model(model_path):
    """Load the YOLOv5 custom model from *model_path*."""
    if not os.path.exists(model_path):
        raise FileNotFoundError(
            f"Model weights not found at '{model_path}'. "
            "Please ensure best.pt is present before running."
        )
    return torch.hub.load("ultralytics/yolov5", "custom", path=model_path)


def load_classes(yaml_path, model):
    """Return class-name list from *yaml_path*, falling back to model.names."""
    if os.path.exists(yaml_path):
        with open(yaml_path, "r") as f:
            data = yaml.safe_load(f)
        classes = data.get("names", [])
        print(f"Loaded custom class names from {yaml_path}")
    else:
        print(f"YAML file not found at '{yaml_path}'. Using model class names.")
        classes = model.names if hasattr(model, "names") else []
    return classes


def run_detection(model, classes):
    """Open the default webcam and run real-time coconut detection."""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError(
            "Unable to open webcam. Check that a camera is connected and accessible."
        )

    cv2.namedWindow(_WINDOW_NAME, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(_WINDOW_NAME, 800, 600)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame. Exiting.")
                break

            # Run inference on the current frame.
            results = model(frame)
            # results.xyxy[0]: tensor [x1, y1, x2, y2, confidence, class]
            detections = results.xyxy[0].cpu().numpy()

            for detection in detections:
                x1, y1, x2, y2, conf, cls = detection
                if conf > _CONF_THRESHOLD:
                    class_idx = int(cls)
                    class_name = (
                        classes[class_idx] if class_idx < len(classes) else str(class_idx)
                    )
                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    label_y = max(int(y1) - 5, 15)  # keep label inside frame at top edge
                    cv2.putText(
                        frame,
                        f"{class_name} {conf:.2f}",
                        (int(x1), label_y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 0, 255),
                        2,
                        cv2.LINE_AA,
                    )
                    # Save detection asynchronously to avoid blocking the main loop.
                    threading.Thread(target=save_image, args=(frame.copy(),), daemon=True).start()

            cv2.imshow(_WINDOW_NAME, frame)
            key = cv2.waitKey(1)
            if key in [ord("q"), ord("Q"), 27]:        # Q / Esc → quit
                break
            elif key in [ord("c"), ord("C")]:           # C → close window
                cv2.destroyAllWindows()
                break
            elif key in [ord("m"), ord("M")]:           # M → maximise
                cv2.setWindowProperty(
                    _WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN
                )
            elif key in [ord("n"), ord("N")]:           # N → restore normal
                cv2.setWindowProperty(
                    _WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL
                )
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    model = load_model(_DEFAULT_MODEL_PATH)
    classes = load_classes(_YAML_PATH, model)
    run_detection(model, classes)