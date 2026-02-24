# Installation

<p align="center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 80" width="700" height="80">
  <defs>
    <linearGradient id="instBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1e1b4b"/>
      <stop offset="100%" style="stop-color:#0c4a6e"/>
    </linearGradient>
    <linearGradient id="instAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#7C3AED"/>
      <stop offset="100%" style="stop-color:#06B6D4"/>
    </linearGradient>
  </defs>
  <rect width="700" height="80" rx="10" fill="url(#instBg)"/>
  <rect x="0" y="74" width="700" height="4" rx="2" fill="url(#instAccent)"/>
  <text x="350" y="36" font-family="Segoe UI,Arial" font-size="22" font-weight="800" fill="white" text-anchor="middle">Installation Guide</text>
  <text x="350" y="60" font-family="Arial" font-size="12" fill="#a78bfa" text-anchor="middle">Windows · Linux · macOS · GPU / CPU</text>
</svg>
</p>

---

## Prerequisites

| Requirement | Version | Notes |
|---|---|---|
| Python | 3.8+ | `python --version` to check |
| pip | latest | `pip install --upgrade pip` |
| Webcam | USB or built-in | Index 0 by default |
| Disk space | ~500 MB | For PyTorch + YOLOv5 weights |
| RAM | 4 GB+ | 8 GB+ recommended |
| GPU (optional) | CUDA 11.x / 12.x | Dramatically improves FPS |

---

## Step 1 — Clone the Repository

```sh
git clone https://github.com/Kaelith69/coco.git
cd coco
```

---

## Step 2 — Create a Virtual Environment

Using a virtual environment keeps dependencies isolated from your system Python.

### Windows

```cmd
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```sh
python3 -m venv .venv
source .venv/bin/activate
```

You should see `(.venv)` at the beginning of your shell prompt when the environment is active.

---

## Step 3 — Install Dependencies

### CPU-only (default)

```sh
pip install -r requirements.txt
```

This installs:

| Package | Purpose |
|---|---|
| `torch` | Deep learning framework, model loading |
| `opencv-python` | Camera capture, frame processing, display |
| `pyyaml` | YAML config file parsing |
| `ultralytics` | YOLOv5 model hub support |

---

### GPU (CUDA) Installation

If you have an NVIDIA GPU, install the CUDA-enabled PyTorch build first, then install the remaining requirements:

**CUDA 12.1:**
```sh
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt
```

**CUDA 11.8:**
```sh
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements.txt
```

> **Find your CUDA version:** Run `nvidia-smi` in a terminal. The top-right corner shows the maximum supported CUDA version.
> Browse all available builds at [pytorch.org/get-started/locally](https://pytorch.org/get-started/locally/).

---

## Step 4 — Verify the Model File

The pre-trained weights file must be present at the repository root:

```
coco/
└── best1.pt   ← must exist
```

The file is included in the repository. If it is missing (e.g., after a partial clone), re-clone or download it manually.

---

## Step 5 — Verify the Installation

```sh
python -c "import torch, cv2, yaml; print('OK — torch', torch.__version__, '| cv2', cv2.__version__)"
```

Expected output (versions may vary):
```
OK — torch 2.x.x | cv2 4.x.x
```

---

## Platform-Specific Notes

### Windows

- The application automatically applies a `pathlib.PosixPath = pathlib.WindowsPath` patch to handle model weights saved on Linux/macOS systems.
- Use Command Prompt or PowerShell (not Git Bash) for best compatibility with OpenCV window events.

### Linux

- Ensure your user has webcam access:
  ```sh
  sudo usermod -aG video $USER
  # Then log out and back in
  ```
- If using X11 forwarding (SSH), set `DISPLAY` appropriately before running.

### macOS

- Grant camera access to Terminal / your IDE when prompted by macOS privacy controls.
- Apple Silicon (M1/M2): PyTorch runs on MPS (Metal Performance Shaders). CPU inference is also supported. GPU support requires PyTorch ≥ 2.0.

### Raspberry Pi / Jetson Nano

- Use `opencv-python-headless` instead of `opencv-python` if running headlessly.
- Install PyTorch from the ARM-specific wheel for your device (see official ARM build pages).
- Reduce `CONFIDENCE_THRESHOLD` slightly or use a smaller YOLOv5 variant if FPS is insufficient.

---

## Troubleshooting Installation

| Error | Likely Cause | Fix |
|---|---|---|
| `ModuleNotFoundError: No module named 'cv2'` | opencv not installed | `pip install opencv-python` |
| `CUDA not available` | CPU-only torch build | Reinstall with CUDA wheel |
| `NotImplementedError: PosixPath` | Windows + Linux-saved weights | Already patched; re-run app |
| `OSError: [Errno 2] No such file or directory: 'best1.pt'` | Missing weights | Ensure file exists at repo root |
| `Cannot open camera (index 0)` | No webcam detected | Check USB connection; try index 1 |

For further help, see the [Troubleshooting](Troubleshooting) page.
