<p align="center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 160" width="800" height="160">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#1a472a;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#2d6a4f;stop-opacity:1"/>
    </linearGradient>
  </defs>
  <rect width="800" height="160" rx="16" fill="url(#bg)"/>
  <!-- Coconut icon -->
  <ellipse cx="80" cy="80" rx="38" ry="42" fill="#6b3f12"/>
  <ellipse cx="80" cy="80" rx="32" ry="36" fill="#8b5e2a"/>
  <path d="M62 58 Q80 42 98 58" stroke="#4a2c0a" stroke-width="2.5" fill="none"/>
  <circle cx="70" cy="68" r="4" fill="#2d1a05"/>
  <circle cx="80" cy="64" r="4" fill="#2d1a05"/>
  <circle cx="90" cy="68" r="4" fill="#2d1a05"/>
  <!-- Palm leaves -->
  <path d="M80 42 Q55 10 30 18" stroke="#52b788" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M80 42 Q80 5 60 2"   stroke="#52b788" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M80 42 Q105 10 130 18" stroke="#52b788" stroke-width="3" fill="none" stroke-linecap="round"/>
  <!-- Detection bounding box hint -->
  <rect x="48" y="44" width="64" height="72" rx="4" fill="none" stroke="#74c69d" stroke-width="2" stroke-dasharray="6,3"/>
  <!-- Title text -->
  <text x="160" y="68" font-family="Segoe UI, Arial, sans-serif" font-size="36" font-weight="700" fill="#d8f3dc">Coconut Detection</text>
  <text x="162" y="104" font-family="Segoe UI, Arial, sans-serif" font-size="18" fill="#95d5b2">Real-time YOLOv5 inference · webcam · auto image saving</text>
  <!-- Badge pills -->
  <rect x="160" y="118" width="88" height="24" rx="12" fill="#1b4332"/>
  <text x="204" y="134" font-family="Arial" font-size="12" fill="#74c69d" text-anchor="middle">Python 3.8+</text>
  <rect x="256" y="118" width="72" height="24" rx="12" fill="#1b4332"/>
  <text x="292" y="134" font-family="Arial" font-size="12" fill="#74c69d" text-anchor="middle">YOLOv5</text>
  <rect x="336" y="118" width="80" height="24" rx="12" fill="#1b4332"/>
  <text x="376" y="134" font-family="Arial" font-size="12" fill="#74c69d" text-anchor="middle">OpenCV</text>
  <rect x="424" y="118" width="66" height="24" rx="12" fill="#1b4332"/>
  <text x="457" y="134" font-family="Arial" font-size="12" fill="#74c69d" text-anchor="middle">MIT</text>
</svg>
</p>

# Coconut Detection

Real-time detection of **mature** and **immature** coconuts using a custom-trained **YOLOv5** model, a standard webcam, and OpenCV. Detected frames are saved automatically as time-stamped JPEG images.

---

## Table of Contents
- [Features](#features)
- [Architecture](#architecture)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Project Structure](#project-structure)
- [Use Cases](#use-cases)
- [Contributing](#contributing)
- [License](#license)

---

## Features

| Feature | Detail |
|---|---|
| Real-time inference | YOLOv5 runs on each webcam frame |
| Custom model | Trained on coconut dataset (`best1.pt`) |
| Confidence filtering | Only detections above **0.67** are shown |
| Auto image saving | One JPEG per detected frame, saved to `CoconutDetection Pictures/` |
| Non-blocking I/O | A single background worker thread handles all disk writes via a bounded queue |
| Cross-platform | Runs on Windows, Linux, and macOS |
| Keyboard control | Quit, close, fullscreen, and normalise the window on the fly |

---

## Architecture

```
webcam
  │
  ▼
cv2.VideoCapture  ──►  YOLOv5 inference  ──►  draw bounding boxes
                                                        │
                                               conf > 0.67?
                                                    │  yes
                                                    ▼
                                           _save_queue (bounded)
                                                    │
                                            background thread
                                                    │
                                                    ▼
                                     CoconutDetection Pictures/
                                     coconut_detection_<ts>.jpg
```

- **Model**: `torch.hub.load('ultralytics/yolov5', 'custom', path='best1.pt')`
- **Class names**: loaded from `AIYolov5/data.yaml` when present; falls back to names embedded in the model.
- **Image saving**: a single `daemon=True` worker thread drains a `queue.Queue(maxsize=50)` so that disk I/O never blocks the detection loop. If the queue is full (burst of detections), frames are silently dropped rather than blocking.

---

## Requirements

- Python **3.8+**
- A USB or built-in **webcam**
- The pre-trained weights file **`best1.pt`** (included in the repository)

Python package dependencies (see `requirements.txt`):

```
torch
opencv-python
pyyaml
ultralytics
```

---

## Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/Kaelith69/coco.git
   cd coco
   ```

2. **Create and activate a virtual environment** *(recommended)*
   ```sh
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux / macOS
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
   > **GPU users**: install the CUDA-enabled build of PyTorch first (select the correct CUDA version for your system from https://pytorch.org/get-started/locally/):
   > `pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121`

4. **Verify the model file is present**
   ```
   coco/
   └── best1.pt   ← must exist
   ```

---

## Usage

```sh
python coco.py
```

A window titled **"Coconut Detection"** will open showing the live webcam feed.  
Coconuts detected with confidence ≥ 67 % are highlighted with a green bounding box and a red label.  
Each frame that contains at least one detection is saved to `CoconutDetection Pictures/`.

---

## Configuration

All tuneable parameters are constants at the top of `coco.py`:

| Constant | Default | Description |
|---|---|---|
| `MODEL_PATH` | `best1.pt` (repo root) | Path to YOLOv5 weights |
| `YAML_PATH` | `AIYolov5/data.yaml` | Optional class-name override |
| `SAVE_DIR` | `CoconutDetection Pictures` | Output folder for saved images |
| `CONFIDENCE_THRESHOLD` | `0.67` | Minimum confidence to accept a detection |
| `CAMERA_INDEX` | `0` | OpenCV camera index (`0` = default webcam) |

---

## Keyboard Shortcuts

| Key | Action |
|---|---|
| `Q` / `q` / `Esc` | Quit the application |
| `C` / `c` | Close the display window (detection continues until process exits) |
| `M` / `m` | Toggle **fullscreen** mode |
| `N` / `n` | Return to **normal** window mode |

---

## Project Structure

```
coco/
├── coco.py                     # Main detection script
├── best1.pt                    # Pre-trained YOLOv5 weights
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── AIYolov5/                   # YOLOv5 training artefacts
    └── content/yolov5/
        └── runs/train/
            └── yolov5s_results/
                ├── weights/best.pt
                ├── opt.yaml
                └── hyp.yaml
```

---

## Use Cases

- **Farm monitoring** – mount a camera in a coconut grove and log all detections for maturity tracking.
- **Harvest planning** – review saved images to identify trees with a high proportion of mature coconuts.
- **Research / dataset expansion** – collect new annotated images directly from the detection output folder.
- **Edge deployment** – run on a Raspberry Pi 4 or Jetson Nano with a USB camera for low-cost field use.

---

## Contributing

Contributions are welcome!  
Please open an issue or submit a pull request for bug fixes, model improvements, or new features.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.