import sys
import os
import threading
import queue
import torch
import yaml
import cv2
from datetime import datetime
import pathlib

# Patch for Windows to handle PosixPath issue (only applied on Windows)
if sys.platform == "win32":
    pathlib.PosixPath = pathlib.WindowsPath

# ─── Configuration ────────────────────────────────────────────────────────────
_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(_BASE_DIR, 'best1.pt')
YAML_PATH = os.path.join(_BASE_DIR, 'AIYolov5', 'data.yaml')
SAVE_DIR = os.path.join(_BASE_DIR, 'CoconutDetection Pictures')
CONFIDENCE_THRESHOLD = 0.67
WINDOW_NAME = 'Coconut Detection'
CAMERA_INDEX = 0
MIN_LABEL_Y = 15       # minimum y-offset so labels are not drawn off the top edge

# ─── Image-saving worker ──────────────────────────────────────────────────────
_save_queue: queue.Queue = queue.Queue(maxsize=50)

def _save_worker() -> None:
    """Background thread: drain the save queue and write images to disk."""
    os.makedirs(SAVE_DIR, exist_ok=True)
    while True:
        frame = _save_queue.get()
        if frame is None:   # sentinel value → exit
            break
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        path = os.path.join(SAVE_DIR, f'coconut_detection_{timestamp}.jpg')
        cv2.imwrite(path, frame)
        print(f"Image saved: {path}")
        _save_queue.task_done()

_save_thread = threading.Thread(target=_save_worker, daemon=True)
_save_thread.start()

# ─── Model loading ────────────────────────────────────────────────────────────
model = torch.hub.load('ultralytics/yolov5', 'custom', path=MODEL_PATH, force_reload=False)
model.eval()

# ─── Class names ──────────────────────────────────────────────────────────────
if os.path.exists(YAML_PATH):
    with open(YAML_PATH, 'r') as f:
        data = yaml.safe_load(f)
    classes = data.get('names', [])
    print(f"Loaded custom class names from {YAML_PATH}: {classes}")
else:
    print(f"YAML file not found at {YAML_PATH}. Using model class names.")
    classes = model.names if hasattr(model, 'names') else []

# ─── Video capture ────────────────────────────────────────────────────────────
cap = cv2.VideoCapture(CAMERA_INDEX)
if not cap.isOpened():
    print(f"Error: Cannot open camera (index {CAMERA_INDEX})")
    _save_queue.put(None)
    sys.exit(1)

cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
cv2.resizeWindow(WINDOW_NAME, 800, 600)

# ─── Detection loop ───────────────────────────────────────────────────────────
try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Run inference on the frame.
        results = model(frame)
        # results.xyxy[0]: [x1, y1, x2, y2, confidence, class]
        detections = results.xyxy[0].cpu().numpy()

        detected = False
        for detection in detections:
            x1, y1, x2, y2, conf, cls = detection
            if conf > CONFIDENCE_THRESHOLD:
                detected = True
                class_idx = int(cls)
                class_name = classes[class_idx] if class_idx < len(classes) else str(class_idx)
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                label_y = max(int(y1) - 5, MIN_LABEL_Y)
                cv2.putText(frame, f'{class_name} {conf:.2f}', (int(x1), label_y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2, cv2.LINE_AA)

        # Save one image per frame that contains at least one detection.
        if detected:
            if not _save_queue.full():
                _save_queue.put(frame.copy())
            else:
                print("Warning: save queue is full; detection frame dropped")

        cv2.imshow(WINDOW_NAME, frame)
        key = cv2.waitKey(1) & 0xFF
        if key in (ord('q'), ord('Q'), 27):     # Q / q / Esc → quit
            break
        elif key in (ord('c'), ord('C')):        # C / c → close window
            cv2.destroyAllWindows()
            break
        elif key in (ord('m'), ord('M')):        # M / m → maximise
            cv2.setWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        elif key in (ord('n'), ord('N')):        # N / n → normalise
            cv2.setWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
finally:
    cap.release()
    cv2.destroyAllWindows()
    _save_queue.put(None)   # signal worker thread to exit cleanly