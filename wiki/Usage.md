# Usage

<p align="center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 80" width="700" height="80">
  <defs>
    <linearGradient id="usageBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1e1b4b"/>
      <stop offset="100%" style="stop-color:#0c4a6e"/>
    </linearGradient>
    <linearGradient id="usageAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#7C3AED"/>
      <stop offset="100%" style="stop-color:#06B6D4"/>
    </linearGradient>
  </defs>
  <rect width="700" height="80" rx="10" fill="url(#usageBg)"/>
  <rect x="0" y="74" width="700" height="4" rx="2" fill="url(#usageAccent)"/>
  <text x="350" y="36" font-family="Segoe UI,Arial" font-size="22" font-weight="800" fill="white" text-anchor="middle">Usage Guide</text>
  <text x="350" y="60" font-family="Arial" font-size="12" fill="#a78bfa" text-anchor="middle">Running detection · keyboard shortcuts · configuration · output files</text>
</svg>
</p>

---

## Running the Application

With your virtual environment activated and dependencies installed:

```sh
python coco.py
```

A window titled **"Coconut Detection"** (800 × 600 px) opens showing the live webcam feed.

---

## What You Will See

1. **Live webcam stream** displayed in the named window.
2. **Green bounding boxes** drawn around each detected coconut that exceeds the confidence threshold.
3. **Red label text** above each box showing `<class_name> <confidence>` (e.g., `mature 0.91`).
4. **Console output** logging each saved image path:
   ```
   Image saved: CoconutDetection Pictures/coconut_detection_20240315_143022_012345.jpg
   ```

---

## Keyboard Shortcuts

| Key | Action |
|---|---|
| `Q` / `q` / `Esc` | Quit the application (releases camera, closes window) |
| `C` / `c` | Close the display window |
| `M` / `m` | Toggle fullscreen mode |
| `N` / `n` | Return to normal (windowed) mode |

> **No mouse interaction is required.** All controls are keyboard-driven.

---

## Output Files

All detected frames are automatically saved to:

```
CoconutDetection Pictures/
└── coconut_detection_YYYYMMDD_HHMMSS_ffffff.jpg
```

**Filename format:**

| Segment | Meaning |
|---|---|
| `YYYY` | 4-digit year |
| `MM` | 2-digit month |
| `DD` | 2-digit day |
| `HH` | 2-digit hour (24h) |
| `mm` | 2-digit minute |
| `SS` | 2-digit second |
| `ffffff` | Microseconds (6 digits) |

The directory is created automatically if it does not exist.

---

## Configuration

All tuneable parameters are constants at the top of `coco.py`. Edit them directly:

```python
# ─── Configuration ────────────────────────────────────────────────────────────
_BASE_DIR            = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH           = os.path.join(_BASE_DIR, 'best1.pt')
YAML_PATH            = os.path.join(_BASE_DIR, 'AIYolov5', 'data.yaml')
SAVE_DIR             = os.path.join(_BASE_DIR, 'CoconutDetection Pictures')
CONFIDENCE_THRESHOLD = 0.67
WINDOW_NAME          = 'Coconut Detection'
CAMERA_INDEX         = 0
MIN_LABEL_Y          = 15
```

| Constant | Default | Description |
|---|---|---|
| `MODEL_PATH` | `best1.pt` | Path to YOLOv5 weights file |
| `YAML_PATH` | `AIYolov5/data.yaml` | Class names override (optional) |
| `SAVE_DIR` | `CoconutDetection Pictures` | Directory for saved JPEG images |
| `CONFIDENCE_THRESHOLD` | `0.67` | Detections below this value are ignored |
| `CAMERA_INDEX` | `0` | OpenCV camera index (0 = default, 1 = second camera, …) |
| `MIN_LABEL_Y` | `15` | Minimum Y position for label text (prevents off-screen drawing) |

---

## Using a Different Camera

To use a different camera (e.g., a USB camera connected as device 1), change:

```python
CAMERA_INDEX = 1
```

For IP / RTSP cameras, replace the integer with a URL string:

```python
CAMERA_INDEX = "rtsp://username:password@192.168.1.100:554/stream"
```

> Note: RTSP support depends on your OpenCV build including GStreamer or FFMPEG.

---

## Adjusting the Confidence Threshold

Lower values increase recall (more detections, more false positives). Higher values increase precision (fewer detections, fewer false positives):

```python
CONFIDENCE_THRESHOLD = 0.50   # More detections
CONFIDENCE_THRESHOLD = 0.80   # Fewer, higher-certainty detections
```

---

## Using a Different Output Directory

```python
SAVE_DIR = os.path.join(_BASE_DIR, 'MyOutputFolder')
```

The directory is created automatically with `os.makedirs(SAVE_DIR, exist_ok=True)`.

---

## Example Console Output

```
Loaded custom class names from /path/to/AIYolov5/data.yaml: ['mature', 'immature']
Image saved: CoconutDetection Pictures/coconut_detection_20240315_143022_112233.jpg
Image saved: CoconutDetection Pictures/coconut_detection_20240315_143022_445566.jpg
Warning: save queue is full; detection frame dropped
Image saved: CoconutDetection Pictures/coconut_detection_20240315_143023_001122.jpg
```

The "save queue is full" warning indicates a high-frequency burst of detections. It is non-fatal — the detection loop continues without interruption.

---

## Stopping the Application

Press **`Q`**, **`q`**, or **`Esc`** at any time. The application will:

1. Break the detection loop.
2. Release the camera (`cap.release()`).
3. Close all OpenCV windows.
4. Send a sentinel (`None`) to the save worker thread.
5. The daemon thread exits automatically when the main process ends.
