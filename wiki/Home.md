# Coconut Detection — Wiki Home

<p align="center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 130" width="700" height="130">
  <defs>
    <linearGradient id="homeBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1e1b4b"/>
      <stop offset="100%" style="stop-color:#0c4a6e"/>
    </linearGradient>
    <linearGradient id="homeAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#7C3AED"/>
      <stop offset="100%" style="stop-color:#06B6D4"/>
    </linearGradient>
  </defs>
  <rect width="700" height="130" rx="12" fill="url(#homeBg)"/>
  <rect x="0" y="124" width="700" height="4" rx="2" fill="url(#homeAccent)"/>
  <text x="350" y="52" font-family="Segoe UI,Arial" font-size="28" font-weight="800" fill="white" text-anchor="middle">🥥 Coconut Detection</text>
  <text x="350" y="80" font-family="Segoe UI,Arial" font-size="14" fill="#a78bfa" text-anchor="middle">Real-time YOLOv5 inference · Custom-trained model · Auto image saving</text>
  <text x="350" y="108" font-family="Arial" font-size="11" fill="#64748b" text-anchor="middle">Python · PyTorch · OpenCV · MIT License</text>
</svg>
</p>

Welcome to the **Coconut Detection** project wiki. This wiki provides comprehensive documentation for developers, contributors, and end users.

---

## Quick Links

| Page | Description |
|---|---|
| [Architecture](Architecture) | System design, component breakdown, threading model |
| [Installation](Installation) | Setup guide for all platforms including GPU |
| [Usage](Usage) | Running the application, keyboard shortcuts, configuration |
| [Privacy](Privacy) | Data handling, local-only operation, security model |
| [Contributing](Contributing) | How to contribute code, models, and documentation |
| [Troubleshooting](Troubleshooting) | Common errors and their solutions |
| [Roadmap](Roadmap) | Planned features and future direction |

---

## Project Summary

**Coconut Detection** is a real-time computer-vision application that identifies **mature** and **immature** coconuts in live webcam footage using a custom-trained [YOLOv5](https://github.com/ultralytics/yolov5) model.

### At a Glance

| Property | Value |
|---|---|
| Language | Python 3.8+ |
| Model | YOLOv5s (custom-trained, `best1.pt`) |
| Framework | PyTorch + Ultralytics YOLOv5 |
| Vision Library | OpenCV |
| Detection Classes | `mature`, `immature` |
| Confidence Threshold | 0.67 |
| Output | Live annotated window + timestamped JPEG files |
| Platform | Windows, Linux, macOS |
| License | MIT |

---

## How It Works

1. **Webcam frames** are captured continuously via `cv2.VideoCapture`.
2. Each frame is passed to the **YOLOv5 inference engine** (loaded from `best1.pt`).
3. Detections with **confidence ≥ 0.67** are annotated with bounding boxes and class labels.
4. Annotated frames are displayed in a named OpenCV window.
5. Frames with detections are enqueued into a **bounded save queue** (capacity 50).
6. A background **daemon thread** drains the queue and writes each frame as a timestamped JPEG to `CoconutDetection Pictures/`.

---

## Repository Layout

```
coco/
├── coco.py              # Main application
├── best1.pt             # Custom YOLOv5 weights
├── requirements.txt     # Python dependencies
├── README.md            # Project overview
├── LICENSE              # MIT license
├── wiki/                # This wiki
└── AIYolov5/            # Training artefacts
```

---

## Getting Started

New to the project? Start here:

1. Read the [Installation guide](Installation) to set up your environment.
2. Follow the [Usage guide](Usage) to run detection.
3. Review [Architecture](Architecture) to understand the system internals.
4. Check [Troubleshooting](Troubleshooting) if you encounter any issues.
