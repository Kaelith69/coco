<div align="center">

<!-- SVG Hero Banner -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 200" width="900" height="200">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0f2027;stop-opacity:1" />
      <stop offset="50%" style="stop-color:#203a43;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#2c5364;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#56ab2f;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#a8e063;stop-opacity:1" />
    </linearGradient>
  </defs>
  <!-- Background -->
  <rect width="900" height="200" rx="16" ry="16" fill="url(#bgGrad)" />
  <!-- Decorative coconut palm silhouette -->
  <g opacity="0.15" fill="#a8e063">
    <ellipse cx="820" cy="60" rx="55" ry="20" transform="rotate(-30 820 60)" />
    <ellipse cx="830" cy="55" rx="50" ry="18" transform="rotate(10 830 55)" />
    <ellipse cx="800" cy="70" rx="55" ry="18" transform="rotate(-60 800 70)" />
    <rect x="817" y="70" width="8" height="110" rx="4" />
    <circle cx="821" cy="145" r="14" />
    <circle cx="835" cy="155" r="12" />
    <circle cx="808" cy="150" r="11" />
  </g>
  <!-- Title -->
  <text x="60" y="100" font-family="'Segoe UI', Arial, sans-serif" font-size="58"
        font-weight="900" fill="url(#textGrad)" letter-spacing="2">🥥 CoCo</text>
  <!-- Subtitle -->
  <text x="62" y="148" font-family="'Segoe UI', Arial, sans-serif" font-size="22"
        fill="#cce8b0" letter-spacing="1" opacity="0.9">Real-Time Coconut Detection · YOLOv5 · OpenCV</text>
  <!-- Version badge shape -->
  <rect x="62" y="163" width="90" height="22" rx="11" fill="#56ab2f" opacity="0.85" />
  <text x="107" y="179" font-family="Arial, sans-serif" font-size="13" fill="white"
        text-anchor="middle" font-weight="bold">v1.1.0</text>
</svg>

---

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-YOLOv5-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?logo=opencv&logoColor=white)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.1.0-brightgreen)](https://github.com/Kaelith69/coco/releases)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)](https://github.com/Kaelith69/coco)

</div>

---

## 📑 Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Features](#features)
4. [Project Structure](#project-structure)
5. [Prerequisites](#prerequisites)
6. [Installation](#installation)
7. [Usage](#usage)
8. [Configuration](#configuration)
9. [Keyboard Controls](#keyboard-controls)
10. [Output](#output)
11. [Contributing](#contributing)
12. [License](#license)

---

## Overview

**CoCo** is a real-time computer-vision application that uses a custom-trained **YOLOv5s** model to detect and classify **mature** and **immature coconuts** via a standard webcam. Detected coconuts are highlighted with bounding boxes, labelled with their class and confidence score, and automatically saved as timestamped images.

> *Put the "coco" in computer vision.* 🥥

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        coco.py                              │
│                                                             │
│  ┌──────────┐    ┌─────────────────┐    ┌───────────────┐  │
│  │ Webcam   │───▶│  YOLOv5 Model   │───▶│  OpenCV Frame │  │
│  │ (OpenCV) │    │  (torch.hub)    │    │  Annotator    │  │
│  └──────────┘    └─────────────────┘    └───────┬───────┘  │
│                                                 │           │
│                              ┌──────────────────▼──────┐   │
│                              │  Async Image Saver       │   │
│                              │  (daemon Thread pool)    │   │
│                              └─────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

| Layer | Technology | Role |
|---|---|---|
| Capture | OpenCV `VideoCapture` | Grabs webcam frames |
| Inference | YOLOv5s (`torch.hub`) | Object detection |
| Post-processing | NumPy / OpenCV | Bounding boxes & labels |
| Persistence | `threading` + `cv2.imwrite` | Non-blocking image saving |
| Class metadata | PyYAML | Human-readable class names |

---

## Features

- 🥥 **Dual-class detection** – distinguishes *Mature* from *Immature* coconuts
- ⚡ **Real-time inference** – processes live webcam feed frame-by-frame
- 💾 **Async image saving** – detections saved in the background with microsecond timestamps (no dropped frames)
- 🖥️ **Cross-platform** – works on Windows, Linux, and macOS (handles the `PosixPath`/`WindowsPath` model compatibility issue automatically)
- 🔧 **Configurable confidence threshold** – tweak `_CONF_THRESHOLD` in `coco.py`
- 📁 **Organised output** – all detection images stored in `CoconutDetection Pictures/`

---

## Project Structure

```
coco/
├── coco.py                          # Main detection script
├── best1.pt                         # (optional) alternative model weights
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
└── AIYolov5/
    ├── data.yaml                    # Class names for the custom model
    └── content/
        └── yolov5/
            └── runs/
                └── train/
                    └── yolov5s_results/
                        ├── weights/
                        │   ├── best.pt   ← primary model weights
                        │   └── last.pt
                        ├── results.csv
                        ├── results.png
                        ├── confusion_matrix.png
                        ├── P_curve.png
                        ├── PR_curve.png
                        ├── R_curve.png
                        ├── F1_curve.png
                        ├── opt.yaml
                        └── hyp.yaml
```

---

## Prerequisites

| Requirement | Minimum version |
|---|---|
| Python | 3.8 |
| CUDA (optional) | 11.x (for GPU acceleration) |
| Webcam | Any UVC-compatible device |

---

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/Kaelith69/coco.git
cd coco

# 2. (Recommended) Create and activate a virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux / macOS:
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

> **GPU users:** install the CUDA-enabled PyTorch wheel *before* running the command above.
> Visit [pytorch.org/get-started/locally](https://pytorch.org/get-started/locally/) for the correct install command.

---

## Usage

```bash
python coco.py
```

A window titled **"Coconut Detection"** will open showing the live webcam feed. Detected coconuts are highlighted with green bounding boxes and labelled with the class name and confidence score.

> ![A funny GIF of a coconut rolling here would slap – consider adding one!](https://media.giphy.com/media/your-gif-id/giphy.gif)
> *(Drop your favourite coconut / palm-tree GIF here for extra vibes 🌴)*

---

## Configuration

All tuneable constants live at the top of `coco.py`:

| Constant | Default | Description |
|---|---|---|
| `_DEFAULT_MODEL_PATH` | `AIYolov5/.../best.pt` | Path to YOLOv5 weights |
| `_YAML_PATH` | `AIYolov5/data.yaml` | Class-name YAML file |
| `_SAVE_DIR` | `CoconutDetection Pictures` | Output folder for saved images |
| `_CONF_THRESHOLD` | `0.67` | Minimum detection confidence (0–1) |

### Custom class names

Edit `AIYolov5/data.yaml`:

```yaml
nc: 2
names:
  - Mature Coconut
  - Immature Coconut
```

### Custom model weights

Pass a different weights file by editing `_DEFAULT_MODEL_PATH` in `coco.py`:

```python
_DEFAULT_MODEL_PATH = os.path.join(_BASE_DIR, "best1.pt")
```

---

## Keyboard Controls

| Key | Action |
|---|---|
| `Q` / `Esc` | Quit the application |
| `C` | Close the display window |
| `M` | Maximise (fullscreen) |
| `N` | Restore normal window size |

---

## Output

Detected frames are saved under `CoconutDetection Pictures/` with microsecond-precision filenames to avoid collisions:

```
CoconutDetection Pictures/
├── coconut_detection_20240315_143022_123456.jpg
├── coconut_detection_20240315_143022_456789.jpg
└── ...
```

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a pull request

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

<div align="center">

*Why did the coconut go to therapy?*
*Because it kept getting cracked under pressure.* 🥥

Made with ❤️ and too much coconut water.

</div>
