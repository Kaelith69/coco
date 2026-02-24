# Architecture

<p align="center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 80" width="700" height="80">
  <defs>
    <linearGradient id="archPageBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1e1b4b"/>
      <stop offset="100%" style="stop-color:#0c4a6e"/>
    </linearGradient>
    <linearGradient id="archPageAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#7C3AED"/>
      <stop offset="100%" style="stop-color:#06B6D4"/>
    </linearGradient>
  </defs>
  <rect width="700" height="80" rx="10" fill="url(#archPageBg)"/>
  <rect x="0" y="74" width="700" height="4" rx="2" fill="url(#archPageAccent)"/>
  <text x="350" y="36" font-family="Segoe UI,Arial" font-size="22" font-weight="800" fill="white" text-anchor="middle">System Architecture</text>
  <text x="350" y="60" font-family="Arial" font-size="12" fill="#a78bfa" text-anchor="middle">Component design · Threading model · Data pipeline</text>
</svg>
</p>

This page describes the internal architecture of the Coconut Detection system — its components, threading model, and the flow of data from camera capture to disk.

---

## High-Level Component Map

```
┌─────────────────────────────────────────────────────────────────┐
│                         coco.py                                 │
│                                                                 │
│  ┌──────────┐    ┌──────────────┐    ┌──────────────────────┐  │
│  │  Webcam  │───►│  YOLOv5      │───►│  Confidence Filter   │  │
│  │  Capture │    │  Inference   │    │  (conf > 0.67)       │  │
│  └──────────┘    └──────────────┘    └─────────┬────────────┘  │
│       ▲                                        │               │
│       │  cv2.VideoCapture(0)                   ▼               │
│       │                           ┌────────────────────┐      │
│       │                           │  Bounding Box Draw │      │
│       │                           │  + Class Label     │      │
│       │                           └────────┬───────────┘      │
│       │                                    │                   │
│       │                           ┌────────▼───────────┐      │
│       │                           │   cv2.imshow        │      │
│       │                           │   (display window) │      │
│       │                           └────────────────────┘      │
│       │                                    │                   │
│       │                           ┌────────▼───────────┐      │
│       │                           │  _save_queue        │      │
│       │                           │  Queue(maxsize=50) │      │
│       │                           └────────────────────┘      │
│                                            │                   │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─│─ ─ ─ ─ ─ ─ ─ ─  │
│  (background thread)                       │                   │
│                                   ┌────────▼───────────┐      │
│                                   │  _save_worker       │      │
│                                   │  (daemon=True)     │      │
│                                   └────────────────────┘      │
│                                            │                   │
│                                   ┌────────▼───────────┐      │
│                                   │  CoconutDetection   │      │
│                                   │  Pictures/  (JPEG) │      │
│                                   └────────────────────┘      │
└─────────────────────────────────────────────────────────────────┘
```

---

## Component Descriptions

### 1. Configuration Block

```python
MODEL_PATH          = 'best1.pt'
YAML_PATH           = 'AIYolov5/data.yaml'
SAVE_DIR            = 'CoconutDetection Pictures'
CONFIDENCE_THRESHOLD = 0.67
CAMERA_INDEX        = 0
MIN_LABEL_Y         = 15
```

All tuneable constants are defined at module level for easy configuration without editing logic code. Paths are derived relative to `__file__` to make the application relocatable.

---

### 2. Webcam Capture (`cv2.VideoCapture`)

- Opened with `cv2.VideoCapture(CAMERA_INDEX)`.
- Returns BGR-format `numpy.ndarray` frames on each `cap.read()` call.
- If the camera cannot be opened, the application exits with a non-zero code after sending the sentinel to the save worker.

---

### 3. YOLOv5 Inference Engine

```python
model = torch.hub.load('ultralytics/yolov5', 'custom', path=MODEL_PATH, force_reload=False)
model.eval()
```

- Loaded via `torch.hub` with a local custom weights file (`best1.pt`).
- `force_reload=False` prevents re-downloading model code on every run.
- `model.eval()` sets the model to inference mode (disables dropout/batch-norm training behavior).
- Inference is called with `results = model(frame)` and detections extracted as `results.xyxy[0].cpu().numpy()` — an `[N, 6]` array of `[x1, y1, x2, y2, confidence, class_index]`.

---

### 4. Class Name Resolution

```python
if os.path.exists(YAML_PATH):
    classes = yaml.safe_load(open(YAML_PATH))['names']
else:
    classes = model.names
```

- Prefers loading class names from `AIYolov5/data.yaml` for explicit control.
- Falls back to names embedded in the model weights if the YAML is absent.

---

### 5. Detection Loop

The main loop continuously:
1. Reads a frame from the webcam.
2. Runs inference.
3. Iterates over all detections; those exceeding `CONFIDENCE_THRESHOLD` are:
   - Drawn as a green `cv2.rectangle`.
   - Labelled with class name and confidence via `cv2.putText` (in red).
4. Enqueues a copy of any detected frame into `_save_queue` (unless full).
5. Calls `cv2.imshow` to update the display.
6. Polls `cv2.waitKey(1)` for keyboard input.

---

### 6. Keyboard Handler

| Key | Constant check | Action |
|---|---|---|
| `Q`, `q`, `Esc` | `ord('q')`, `27` | Break loop → clean teardown |
| `C`, `c` | `ord('c')` | `cv2.destroyAllWindows()` + break |
| `M`, `m` | `ord('m')` | Set window to `WINDOW_FULLSCREEN` |
| `N`, `n` | `ord('n')` | Set window to `WINDOW_NORMAL` |

---

### 7. Non-blocking Image Save Worker

```python
_save_queue: queue.Queue = queue.Queue(maxsize=50)

def _save_worker():
    os.makedirs(SAVE_DIR, exist_ok=True)
    while True:
        frame = _save_queue.get()
        if frame is None:   # sentinel → exit
            break
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        cv2.imwrite(os.path.join(SAVE_DIR, f'coconut_detection_{timestamp}.jpg'), frame)
        _save_queue.task_done()

_save_thread = threading.Thread(target=_save_worker, daemon=True)
_save_thread.start()
```

**Key design decisions:**

| Decision | Rationale |
|---|---|
| `daemon=True` | Thread exits automatically when the main process ends |
| `maxsize=50` | Bounds memory usage; prevents unbounded queue growth during bursts |
| Frame drops when full | Non-blocking: inference loop never waits for I/O |
| Sentinel (`None`) | Clean shutdown: `_save_queue.put(None)` signals worker to exit |
| `frame.copy()` | Ensures the worker holds its own buffer independent of the main loop |

---

### 8. Teardown (finally block)

```python
finally:
    cap.release()
    cv2.destroyAllWindows()
    _save_queue.put(None)   # signal worker to exit
```

- `cap.release()` frees the camera hardware.
- `cv2.destroyAllWindows()` closes all OpenCV windows.
- `_save_queue.put(None)` sends the sentinel to allow the worker thread to exit gracefully before the process ends.

---

## Threading Model

```
Main Thread                        _save_worker Thread
──────────────────────────────     ────────────────────────────
  cap.read()  ─────────────┐         _save_queue.get() (blocks)
  model(frame)             │              │
  filter + annotate        │         frame = dequeue
  cv2.imshow               │         cv2.imwrite(...)
  _save_queue.put(frame) ──┘         _save_queue.task_done()
  cv2.waitKey(1)
```

The two threads share only one object: `_save_queue`. All access is thread-safe by design — `queue.Queue` is inherently thread-safe in CPython.

---

## File I/O Pattern

| File | Read/Write | Timing |
|---|---|---|
| `best1.pt` | Read once | Module load time |
| `AIYolov5/data.yaml` | Read once | Module load time |
| `CoconutDetection Pictures/*.jpg` | Write async | Per detection, background thread |

---

## Windows Compatibility Patch

```python
if sys.platform == "win32":
    pathlib.PosixPath = pathlib.WindowsPath
```

YOLOv5 model weights saved on Linux/macOS embed `PosixPath` objects. Loading them on Windows raises a `NotImplementedError`. This one-line patch replaces `PosixPath` with `WindowsPath` in the `pathlib` module before the model is loaded, resolving the incompatibility transparently.
