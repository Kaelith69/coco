# Privacy & Security

<p align="center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 80" width="700" height="80">
  <defs>
    <linearGradient id="privBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1e1b4b"/>
      <stop offset="100%" style="stop-color:#0c4a6e"/>
    </linearGradient>
    <linearGradient id="privAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#7C3AED"/>
      <stop offset="100%" style="stop-color:#06B6D4"/>
    </linearGradient>
  </defs>
  <rect width="700" height="80" rx="10" fill="url(#privBg)"/>
  <rect x="0" y="74" width="700" height="4" rx="2" fill="url(#privAccent)"/>
  <text x="350" y="36" font-family="Segoe UI,Arial" font-size="22" font-weight="800" fill="white" text-anchor="middle">Privacy &amp; Security</text>
  <text x="350" y="60" font-family="Arial" font-size="12" fill="#a78bfa" text-anchor="middle">Local-only operation · No telemetry · No personal data</text>
</svg>
</p>

---

## Privacy Principles

Coconut Detection is designed with a **local-first, offline-only** architecture. The following privacy guarantees apply by design:

---

## Data Handling

### What Data Is Captured

| Data Type | Captured? | Notes |
|---|---|---|
| Webcam video frames | Yes | Processed in-memory, not retained by default |
| Detected frames (JPEG) | Yes (if detection occurs) | Saved locally to `CoconutDetection Pictures/` |
| Personal / biometric data | **No** | Model detects coconuts only |
| Audio | **No** | No microphone access |
| Location / GPS | **No** | Not accessed |
| User identifiers | **No** | None collected |

### What Data Leaves the Device

**Nothing.** All processing is entirely local:

- No frames are transmitted over any network.
- No detection results are uploaded to any server.
- No usage analytics or telemetry are collected.
- No crash reports are sent automatically.

---

## Network Access

The application makes **no outbound network connections** during normal operation.

The only potential network access occurs at model load time if `torch.hub.load` needs to download YOLOv5 source code on first run. This is controlled by:

```python
model = torch.hub.load('ultralytics/yolov5', 'custom', path=MODEL_PATH, force_reload=False)
```

| Parameter | Value | Effect |
|---|---|---|
| `force_reload` | `False` | Uses cached model code if already downloaded; avoids re-download |

After the first successful run, `torch.hub` caches YOLOv5 code locally. Subsequent runs do not require internet access.

**To run in a fully air-gapped environment:**

1. Run the application once with internet access to populate the `torch.hub` cache (`~/.cache/torch/hub/`).
2. Disconnect from the network. The application will function normally using the cached code and local `best1.pt` weights.

---

## Local Storage

### Saved Images

All detection images are saved to:
```
CoconutDetection Pictures/
└── coconut_detection_YYYYMMDD_HHMMSS_ffffff.jpg
```

- This directory is created under the repository root by default.
- Images contain only the annotated camera frame — no metadata beyond the filename timestamp.
- You control this directory: delete, move, or change it freely via `SAVE_DIR` in `coco.py`.

### Model Weights

`best1.pt` is a binary PyTorch checkpoint file containing only model weights. It does not contain any user data.

---

## Security Model

### Attack Surface

| Component | Risk | Mitigation |
|---|---|---|
| `torch.hub.load` | Downloads code on first run | `force_reload=False`; air-gap after first run |
| `cv2.VideoCapture` | Reads camera hardware | OS-level camera permissions required |
| `cv2.imwrite` | Writes to local disk | Bounded queue prevents runaway disk usage |
| `yaml.safe_load` | Parses YAML config | Uses `safe_load` — does not execute arbitrary Python |

### Key Security Properties

- **No shell execution** — no `subprocess`, `os.system`, or `eval` calls.
- **No user input parsing** — the only input is keyboard scan codes via `cv2.waitKey`.
- **No external authentication** — no credentials, tokens, or secrets are stored or accessed.
- **Safe YAML parsing** — `yaml.safe_load` prevents YAML deserialization attacks.
- **No third-party telemetry libraries** — no Sentry, Datadog, or similar SDKs are included.

---

## Responsible Use

This application accesses your camera. Please ensure:

1. You have the right to record the environment where the camera is pointed.
2. Recorded images stored in `CoconutDetection Pictures/` are handled in accordance with any applicable privacy regulations (e.g., GDPR, local laws) if the environment could include people.
3. When deploying in shared or public spaces, post appropriate signage about camera usage.

---

## Reporting Security Issues

If you discover a security vulnerability in this project, please open a GitHub issue with the label `security`. For sensitive disclosures, contact the repository owner directly via GitHub.
