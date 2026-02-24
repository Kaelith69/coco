# Roadmap

<p align="center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 80" width="700" height="80">
  <defs>
    <linearGradient id="roadBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1e1b4b"/>
      <stop offset="100%" style="stop-color:#0c4a6e"/>
    </linearGradient>
    <linearGradient id="roadAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#7C3AED"/>
      <stop offset="100%" style="stop-color:#06B6D4"/>
    </linearGradient>
  </defs>
  <rect width="700" height="80" rx="10" fill="url(#roadBg)"/>
  <rect x="0" y="74" width="700" height="4" rx="2" fill="url(#roadAccent)"/>
  <text x="350" y="36" font-family="Segoe UI,Arial" font-size="22" font-weight="800" fill="white" text-anchor="middle">Project Roadmap</text>
  <text x="350" y="60" font-family="Arial" font-size="12" fill="#a78bfa" text-anchor="middle">Completed features · in-progress work · planned enhancements</text>
</svg>
</p>

---

## Legend

| Symbol | Meaning |
|---|---|
| ✅ | Completed and released |
| 🚧 | In progress |
| 🔲 | Planned |
| 💡 | Idea / under consideration |

---

## Completed

| Feature | Notes |
|---|---|
| ✅ Real-time YOLOv5 webcam detection | Core functionality |
| ✅ Custom-trained coconut model (`best1.pt`) | Mature and immature classes |
| ✅ Confidence threshold filtering (0.67) | Reduces false positives |
| ✅ Non-blocking background image saving | Bounded queue, daemon thread |
| ✅ Timestamped JPEG output | `YYYYMMDD_HHMMSS_ffffff` format |
| ✅ Green bounding box + red label overlay | Per-detection annotation |
| ✅ Keyboard controls (quit, fullscreen, normalise) | Q/C/M/N keys |
| ✅ Cross-platform support (Win/Linux/macOS) | PosixPath patch for Windows |
| ✅ Configurable camera index | `CAMERA_INDEX` constant |
| ✅ Class name loading from `data.yaml` | Falls back to model-embedded names |

---

## Near-Term (Next Release)

| Feature | Priority | Description |
|---|---|---|
| 🔲 Detection count overlay | High | Show `Detected: N mature / M immature` on frame |
| 🔲 CSV detection log | High | Append each detection to a CSV file with timestamp, class, confidence, bbox coords |
| 🔲 Video file input mode | Medium | Accept a video file path as `CAMERA_INDEX` alternative |
| 🔲 Configurable save frequency | Medium | Save every N-th detection frame instead of every frame |

---

## Medium-Term

| Feature | Priority | Description |
|---|---|---|
| 🔲 RTSP / IP camera stream support | High | Allow `CAMERA_INDEX` to accept RTSP URLs |
| 🔲 JSON detection log export | Medium | Structured detection records per session |
| 🔲 Frame annotation toggle | Medium | Keyboard shortcut to hide/show bounding boxes |
| 🔲 GUI configuration panel | Low | Simple Tkinter or PySimpleGUI settings window |
| 🔲 REST API for remote monitoring | Low | Expose detection events via a local HTTP endpoint |

---

## Long-Term

| Feature | Priority | Description |
|---|---|---|
| 🔲 Raspberry Pi / Jetson Nano deployment guide | High | Step-by-step docs + optimised launch script |
| 🔲 Model retraining pipeline documentation | High | Dataset preparation, training, evaluation workflow |
| 🔲 Multi-camera support | Medium | Run detection on N cameras in parallel |
| 🔲 Web dashboard | Medium | Browser UI showing live detections and saved images |
| 🔲 Alert / notification system | Low | Push notification when a threshold of mature coconuts is detected |
| 🔲 Export to ONNX / TensorRT | Low | Faster inference on NVIDIA hardware |

---

## Under Consideration

| Idea | Description |
|---|---|
| 💡 Yield estimation | Estimate coconut count per tree from detection density |
| 💡 Thermal camera support | Extend to thermal imaging for night-time grove monitoring |
| 💡 Dataset release | Publish the training dataset (with annotations) publicly |
| 💡 Mobile app | Android/iOS companion for field use |

---

## Contributing to the Roadmap

If you have a feature request:

1. Check [existing issues](https://github.com/Kaelith69/coco/issues) first.
2. Open a new issue with the label `enhancement`.
3. Describe the use case and expected behaviour.

PRs implementing roadmap features are very welcome — see the [Contributing guide](Contributing).
