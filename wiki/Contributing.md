# Contributing

<p align="center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 80" width="700" height="80">
  <defs>
    <linearGradient id="contBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1e1b4b"/>
      <stop offset="100%" style="stop-color:#0c4a6e"/>
    </linearGradient>
    <linearGradient id="contAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#7C3AED"/>
      <stop offset="100%" style="stop-color:#06B6D4"/>
    </linearGradient>
  </defs>
  <rect width="700" height="80" rx="10" fill="url(#contBg)"/>
  <rect x="0" y="74" width="700" height="4" rx="2" fill="url(#contAccent)"/>
  <text x="350" y="36" font-family="Segoe UI,Arial" font-size="22" font-weight="800" fill="white" text-anchor="middle">Contributing Guide</text>
  <text x="350" y="60" font-family="Arial" font-size="12" fill="#a78bfa" text-anchor="middle">Bug fixes · feature additions · model improvements · documentation</text>
</svg>
</p>

Contributions to Coconut Detection are welcome! This guide explains the contribution workflow and coding conventions.

---

## Ways to Contribute

| Type | Description |
|---|---|
| 🐛 Bug fix | Correct incorrect behaviour or crashes |
| ✨ Feature | Add new functionality (see [Roadmap](Roadmap)) |
| 🧠 Model | Improve or retrain the coconut detection model |
| 📝 Documentation | Improve the README, wiki, or inline docstrings |
| 🎨 Refactor | Improve code readability without changing behaviour |
| 🧪 Tests | Add automated tests for detection pipeline logic |

---

## Development Setup

```sh
git clone https://github.com/Kaelith69/coco.git
cd coco
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## Contribution Workflow

### 1. Open or Find an Issue

- Check [existing issues](https://github.com/Kaelith69/coco/issues) before starting work.
- If your change is non-trivial, open an issue to discuss it first.

### 2. Fork and Branch

```sh
# Fork on GitHub, then clone your fork
git clone https://github.com/<your-username>/coco.git
cd coco

# Create a descriptive branch
git checkout -b feature/rtsp-camera-support
# or
git checkout -b fix/queue-full-warning-formatting
```

### 3. Make Your Changes

- Keep changes focused on one concern per pull request.
- Follow the [coding conventions](#coding-conventions) below.
- Update `requirements.txt` if you add a new dependency.
- Update the README or relevant wiki page if behaviour changes.

### 4. Test Your Changes

- Run the application manually with a webcam to verify detection works.
- If you've added logic (e.g., new configuration parsing), write a quick test in a `/tmp` script.

### 5. Commit

Write clear, imperative commit messages:

```
Add RTSP camera URL support in CAMERA_INDEX
Fix label drawn off-screen when y1 < MIN_LABEL_Y
Refactor _save_worker to use context manager
```

### 6. Open a Pull Request

- Push your branch and open a PR against `main`.
- Fill in the PR description explaining **what** changed and **why**.
- Reference the related issue (e.g., `Closes #12`).

---

## Coding Conventions

### Style

- Follow [PEP 8](https://peps.python.org/pep-0008/).
- Use 4-space indentation.
- Keep lines ≤ 100 characters.
- Group imports: stdlib → third-party → local.

### Constants

- All configuration constants go at the top of `coco.py` in the `─── Configuration ───` block.
- Use `UPPER_SNAKE_CASE` for module-level constants.

### Comments

- Use the existing section-separator style for major code blocks:
  ```python
  # ─── Section name ────────────────────────────────────────────────────────────
  ```
- Inline comments should be concise and explain *why*, not *what*.

### Error Handling

- Use descriptive error messages with context (file paths, values).
- Prefer early exits (`sys.exit`) over silent failures for critical errors (e.g., missing model file).

---

## Model Contributions

To contribute an improved model:

1. Train a new YOLOv5 model on coconut detection data.
2. Export weights as a `.pt` file.
3. Place the file in the repository root and update `MODEL_PATH` in `coco.py`.
4. Update `AIYolov5/data.yaml` with the correct class names.
5. Document training configuration (dataset, epochs, hyperparameters) in your PR description.

### Minimum bar for model PRs

- Precision / Recall / mAP metrics from validation set
- Confusion matrix image
- Sample detection images

---

## Documentation Contributions

- Edit files in the `wiki/` directory for wiki pages.
- Edit `README.md` for the project overview.
- Ensure SVGs render correctly by testing in a Markdown preview.

---

## Code of Conduct

Be respectful and constructive. We follow the [Contributor Covenant](https://www.contributor-covenant.org/) code of conduct.

---

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](../LICENSE).
