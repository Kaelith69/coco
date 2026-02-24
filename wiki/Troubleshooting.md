# Troubleshooting

<p align="center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 80" width="700" height="80">
  <defs>
    <linearGradient id="trBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1e1b4b"/>
      <stop offset="100%" style="stop-color:#0c4a6e"/>
    </linearGradient>
    <linearGradient id="trAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#7C3AED"/>
      <stop offset="100%" style="stop-color:#06B6D4"/>
    </linearGradient>
  </defs>
  <rect width="700" height="80" rx="10" fill="url(#trBg)"/>
  <rect x="0" y="74" width="700" height="4" rx="2" fill="url(#trAccent)"/>
  <text x="350" y="36" font-family="Segoe UI,Arial" font-size="22" font-weight="800" fill="white" text-anchor="middle">Troubleshooting</text>
  <text x="350" y="60" font-family="Arial" font-size="12" fill="#a78bfa" text-anchor="middle">Common errors and their solutions</text>
</svg>
</p>

---

## Camera Errors

### `Error: Cannot open camera (index 0)`

**Cause:** OpenCV cannot access the webcam at index 0.

**Solutions:**

1. Ensure a webcam is physically connected.
2. Try a different camera index:
   ```python
   CAMERA_INDEX = 1   # Second camera
   ```
3. **Linux:** Ensure your user is in the `video` group:
   ```sh
   sudo usermod -aG video $USER
   # Log out and back in
   ```
4. **macOS:** Grant camera permission to Terminal/IDE in System Settings → Privacy → Camera.
5. **Windows:** Check Device Manager for webcam drivers.

---

### `Failed to grab frame`

**Cause:** Camera disconnected mid-session, or driver issue.

**Solutions:**

- Reconnect the webcam and restart the application.
- Try a different USB port.
- Check that no other application is using the camera exclusively.

---

## Model Loading Errors

### `OSError: [Errno 2] No such file or directory: 'best1.pt'`

**Cause:** The weights file is missing from the repository root.

**Solutions:**

1. Verify the file exists: `ls best1.pt` (Linux/macOS) or `dir best1.pt` (Windows).
2. Re-clone the repository: `git clone https://github.com/Kaelith69/coco.git`.

---

### `NotImplementedError: cannot instantiate 'PosixPath' on your system`

**Cause:** Model weights were saved on Linux/macOS and are being loaded on Windows.

**Solution:** This is automatically patched. Ensure you are running the latest `coco.py` which includes:

```python
if sys.platform == "win32":
    pathlib.PosixPath = pathlib.WindowsPath
```

---

### `RuntimeError: CUDA out of memory`

**Cause:** GPU does not have enough VRAM for the model.

**Solutions:**

1. Force CPU inference by setting the device before model load:
   ```python
   import os
   os.environ["CUDA_VISIBLE_DEVICES"] = ""   # add before imports
   ```
2. Or use a smaller input resolution.

---

### `torch.hub` download fails / hangs

**Cause:** No internet access or blocked PyPI/GitHub endpoint.

**Solutions:**

1. Run with internet access once to populate the cache.
2. If behind a proxy, set `HTTP_PROXY` / `HTTPS_PROXY` environment variables.
3. Pre-download the YOLOv5 code manually into `~/.cache/torch/hub/`.

---

## Dependency / Import Errors

### `ModuleNotFoundError: No module named 'cv2'`

```sh
pip install opencv-python
```

### `ModuleNotFoundError: No module named 'yaml'`

```sh
pip install pyyaml
```

### `ModuleNotFoundError: No module named 'torch'`

```sh
pip install torch
# or for CUDA:
pip install torch --index-url https://download.pytorch.org/whl/cu121
```

### `ModuleNotFoundError: No module named 'ultralytics'`

```sh
pip install ultralytics
```

---

## Display / Window Errors

### Window opens and immediately closes

**Cause:** Camera read fails on the first frame.

**Solutions:**

- Ensure the webcam is not in use by another application.
- Add a small sleep before the loop:
  ```python
  import time; time.sleep(0.5)
  ```

### Window does not respond to keyboard

**Cause:** The OpenCV window does not have focus.

**Solutions:**

- Click on the window to give it focus before pressing keys.
- On Linux with some desktop environments, try `cv2.waitKey(10)` instead of `cv2.waitKey(1)`.

---

## Performance Issues

### Very low FPS (< 5 FPS on CPU)

**Solutions:**

1. Use a CUDA-enabled GPU (see [Installation](Installation)).
2. Reduce input resolution by adding before inference:
   ```python
   frame = cv2.resize(frame, (640, 480))
   ```
3. Increase `cv2.waitKey` delay (reduces loop frequency):
   ```python
   cv2.waitKey(33)   # ~30 FPS cap
   ```

### `Warning: save queue is full; detection frame dropped`

This is **non-fatal**. It means detections are occurring faster than the disk can write.

**Solutions:**

1. Use a faster storage device (SSD over HDD).
2. Increase queue size:
   ```python
   _save_queue: queue.Queue = queue.Queue(maxsize=200)
   ```
3. Reduce image save frequency by saving every N frames instead of every frame.

---

## YAML / Class Name Errors

### Class names show as integers instead of names

**Cause:** `AIYolov5/data.yaml` is missing or malformed.

**Solutions:**

1. Verify the file exists: `ls AIYolov5/data.yaml`.
2. Verify its format:
   ```yaml
   names:
     - mature
     - immature
   nc: 2
   ```
3. If missing, the application falls back to names embedded in `best1.pt`.

---

## Collecting Debug Information

If you need to report an issue, collect this information:

```sh
python --version
python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
python -c "import cv2; print(cv2.__version__)"
python -c "import yaml; print(yaml.__version__)"
```

And include the full traceback from the terminal when the error occurred.

---

## Getting Help

- Open an issue on [GitHub](https://github.com/Kaelith69/coco/issues).
- Include your OS, Python version, dependency versions, and the full error output.
