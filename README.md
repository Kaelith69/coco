<p align="center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 200" width="900" height="200">
  <defs>
    <linearGradient id="heroBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1e1b4b;stop-opacity:1"/>
      <stop offset="50%" style="stop-color:#2e1065;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#0c4a6e;stop-opacity:1"/>
    </linearGradient>
    <linearGradient id="accentLine" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#7C3AED;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#06B6D4;stop-opacity:1"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <!-- Background -->
  <rect width="900" height="200" rx="18" fill="url(#heroBg)"/>
  <!-- Accent bar -->
  <rect x="0" y="188" width="900" height="4" rx="2" fill="url(#accentLine)"/>
  <!-- Grid dots -->
  <g opacity="0.07" fill="#a78bfa">
    <circle cx="40" cy="40" r="1.5"/><circle cx="80" cy="40" r="1.5"/><circle cx="120" cy="40" r="1.5"/>
    <circle cx="40" cy="80" r="1.5"/><circle cx="80" cy="80" r="1.5"/><circle cx="120" cy="80" r="1.5"/>
    <circle cx="40" cy="120" r="1.5"/><circle cx="80" cy="120" r="1.5"/><circle cx="120" cy="120" r="1.5"/>
    <circle cx="860" cy="40" r="1.5"/><circle cx="820" cy="40" r="1.5"/>
    <circle cx="860" cy="80" r="1.5"/><circle cx="820" cy="80" r="1.5"/>
    <circle cx="860" cy="120" r="1.5"/><circle cx="820" cy="120" r="1.5"/>
  </g>
  <!-- Coconut icon with AI overlay -->
  <g transform="translate(65,100)">
    <!-- Palm leaves -->
    <path d="M0,-40 Q-28,-68 -50,-52" stroke="#06B6D4" stroke-width="3.5" fill="none" stroke-linecap="round" filter="url(#glow)"/>
    <path d="M0,-40 Q0,-72 -16,-78" stroke="#06B6D4" stroke-width="3.5" fill="none" stroke-linecap="round" filter="url(#glow)"/>
    <path d="M0,-40 Q28,-68 50,-52" stroke="#06B6D4" stroke-width="3.5" fill="none" stroke-linecap="round" filter="url(#glow)"/>
    <!-- Coconut body -->
    <ellipse cx="0" cy="0" rx="34" ry="38" fill="#4a2c0a" opacity="0.9"/>
    <ellipse cx="0" cy="0" rx="28" ry="32" fill="#7c4f1e"/>
    <!-- Eyes -->
    <circle cx="-10" cy="-6" r="4.5" fill="#1e1b4b"/>
    <circle cx="0" cy="-10" r="4.5" fill="#1e1b4b"/>
    <circle cx="10" cy="-6" r="4.5" fill="#1e1b4b"/>
    <!-- Detection box -->
    <rect x="-42" y="-46" width="84" height="92" rx="5" fill="none" stroke="#7C3AED" stroke-width="2" stroke-dasharray="7,3" opacity="0.9"/>
    <!-- Corner ticks -->
    <path d="M-42,-46 l12,0 M-42,-46 l0,12" stroke="#06B6D4" stroke-width="2.5" fill="none"/>
    <path d="M42,-46 l-12,0 M42,-46 l0,12" stroke="#06B6D4" stroke-width="2.5" fill="none"/>
    <path d="M-42,46 l12,0 M-42,46 l0,-12" stroke="#06B6D4" stroke-width="2.5" fill="none"/>
    <path d="M42,46 l-12,0 M42,46 l0,-12" stroke="#06B6D4" stroke-width="2.5" fill="none"/>
    <!-- Confidence badge -->
    <rect x="-42" y="-66" width="60" height="16" rx="8" fill="#7C3AED" opacity="0.9"/>
    <text x="-12" y="-54" font-family="monospace" font-size="9" fill="white" text-anchor="middle">0.93 ✓</text>
  </g>
  <!-- Title -->
  <text x="160" y="82" font-family="Segoe UI, Arial, sans-serif" font-size="42" font-weight="800" fill="white" letter-spacing="-1">Coconut Detection</text>
  <text x="162" y="118" font-family="Segoe UI, Arial, sans-serif" font-size="17" fill="#a78bfa">Real-time YOLOv5 inference · Custom-trained model · Auto image saving</text>
  <!-- Tech badges -->
  <rect x="162" y="136" width="90" height="26" rx="13" fill="#7C3AED" opacity="0.85"/>
  <text x="207" y="153" font-family="Arial" font-size="12" fill="white" text-anchor="middle" font-weight="600">Python 3.8+</text>
  <rect x="260" y="136" width="76" height="26" rx="13" fill="#2563EB" opacity="0.85"/>
  <text x="298" y="153" font-family="Arial" font-size="12" fill="white" text-anchor="middle" font-weight="600">YOLOv5</text>
  <rect x="344" y="136" width="82" height="26" rx="13" fill="#0891B2" opacity="0.85"/>
  <text x="385" y="153" font-family="Arial" font-size="12" fill="white" text-anchor="middle" font-weight="600">OpenCV</text>
  <rect x="434" y="136" width="68" height="26" rx="13" fill="#065f46" opacity="0.85"/>
  <text x="468" y="153" font-family="Arial" font-size="12" fill="white" text-anchor="middle" font-weight="600">MIT</text>
  <rect x="510" y="136" width="72" height="26" rx="13" fill="#1e3a5f" opacity="0.85"/>
  <text x="546" y="153" font-family="Arial" font-size="12" fill="white" text-anchor="middle" font-weight="600">PyTorch</text>
</svg>
</p>

<p align="center">
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.8%2B-7C3AED?style=flat-square&logo=python&logoColor=white" alt="Python 3.8+"/></a>
  <a href="https://github.com/ultralytics/yolov5"><img src="https://img.shields.io/badge/YOLOv5-custom-2563EB?style=flat-square&logo=pytorch&logoColor=white" alt="YOLOv5"/></a>
  <a href="https://opencv.org/"><img src="https://img.shields.io/badge/OpenCV-4.x-06B6D4?style=flat-square&logo=opencv&logoColor=white" alt="OpenCV"/></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-10B981?style=flat-square" alt="MIT License"/></a>
  <a href="https://github.com/Kaelith69/coco/blob/main/requirements.txt"><img src="https://img.shields.io/badge/requirements-pip-F59E0B?style=flat-square&logo=pypi&logoColor=white" alt="Requirements"/></a>
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-7C3AED?style=flat-square" alt="Platform"/>
</p>

---

## Overview

**Coconut Detection** is a real-time computer-vision application that identifies **mature** and **immature** coconuts in live webcam footage using a custom-trained [YOLOv5](https://github.com/ultralytics/yolov5) model. Every frame containing a detection is automatically saved as a time-stamped JPEG, enabling hands-free farm monitoring, harvest planning, and research dataset expansion.

---

## Table of Contents

- [Core Capabilities](#core-capabilities)
- [System Architecture](#system-architecture)
- [Data Flow](#data-flow)
- [Technology Stack](#technology-stack)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Project Structure](#project-structure)
- [Performance](#performance)
- [Use Cases](#use-cases)
- [Accessibility](#accessibility)
- [Privacy & Security](#privacy--security)
- [Roadmap](#roadmap)
- [Design Principles](#design-principles)
- [Contributing](#contributing)
- [License](#license)

---

## Core Capabilities

<p align="center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 260" width="760" height="260">
  <defs>
    <linearGradient id="capBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#0f172a"/>
      <stop offset="100%" style="stop-color:#1e1b4b"/>
    </linearGradient>
  </defs>
  <rect width="760" height="260" rx="14" fill="url(#capBg)"/>
  <!-- Title -->
  <text x="380" y="34" font-family="Segoe UI,Arial,sans-serif" font-size="15" fill="#a78bfa" text-anchor="middle" font-weight="600" letter-spacing="2">CORE CAPABILITIES</text>

  <!-- Card 1: Real-time Inference -->
  <rect x="20" y="52" width="156" height="106" rx="10" fill="#1e1b4b" stroke="#7C3AED" stroke-width="1.5"/>
  <text x="98" y="78" font-family="Arial" font-size="22" text-anchor="middle" fill="#7C3AED">⚡</text>
  <text x="98" y="100" font-family="Segoe UI,Arial" font-size="12" font-weight="700" fill="white" text-anchor="middle">Real-time</text>
  <text x="98" y="116" font-family="Segoe UI,Arial" font-size="12" font-weight="700" fill="white" text-anchor="middle">Inference</text>
  <text x="98" y="134" font-family="Segoe UI,Arial" font-size="10" fill="#94a3b8" text-anchor="middle">YOLOv5 per frame</text>
  <text x="98" y="148" font-family="Segoe UI,Arial" font-size="10" fill="#94a3b8" text-anchor="middle">live webcam feed</text>

  <!-- Card 2: Custom Model -->
  <rect x="196" y="52" width="156" height="106" rx="10" fill="#1e1b4b" stroke="#2563EB" stroke-width="1.5"/>
  <text x="274" y="78" font-family="Arial" font-size="22" text-anchor="middle" fill="#2563EB">🧠</text>
  <text x="274" y="100" font-family="Segoe UI,Arial" font-size="12" font-weight="700" fill="white" text-anchor="middle">Custom</text>
  <text x="274" y="116" font-family="Segoe UI,Arial" font-size="12" font-weight="700" fill="white" text-anchor="middle">Trained Model</text>
  <text x="274" y="134" font-family="Segoe UI,Arial" font-size="10" fill="#94a3b8" text-anchor="middle">best1.pt weights</text>
  <text x="274" y="148" font-family="Segoe UI,Arial" font-size="10" fill="#94a3b8" text-anchor="middle">coconut dataset</text>

  <!-- Card 3: Confidence Filter -->
  <rect x="372" y="52" width="156" height="106" rx="10" fill="#1e1b4b" stroke="#06B6D4" stroke-width="1.5"/>
  <text x="450" y="78" font-family="Arial" font-size="22" text-anchor="middle" fill="#06B6D4">🎯</text>
  <text x="450" y="100" font-family="Segoe UI,Arial" font-size="12" font-weight="700" fill="white" text-anchor="middle">Confidence</text>
  <text x="450" y="116" font-family="Segoe UI,Arial" font-size="12" font-weight="700" fill="white" text-anchor="middle">Filtering</text>
  <text x="450" y="134" font-family="Segoe UI,Arial" font-size="10" fill="#94a3b8" text-anchor="middle">threshold: 0.67</text>
  <text x="450" y="148" font-family="Segoe UI,Arial" font-size="10" fill="#94a3b8" text-anchor="middle">reduce false positives</text>

  <!-- Card 4: Auto Save -->
  <rect x="548" y="52" width="192" height="106" rx="10" fill="#1e1b4b" stroke="#7C3AED" stroke-width="1.5"/>
  <text x="644" y="78" font-family="Arial" font-size="22" text-anchor="middle" fill="#7C3AED">💾</text>
  <text x="644" y="100" font-family="Segoe UI,Arial" font-size="12" font-weight="700" fill="white" text-anchor="middle">Non-blocking</text>
  <text x="644" y="116" font-family="Segoe UI,Arial" font-size="12" font-weight="700" fill="white" text-anchor="middle">Image Saving</text>
  <text x="644" y="134" font-family="Segoe UI,Arial" font-size="10" fill="#94a3b8" text-anchor="middle">background worker thread</text>
  <text x="644" y="148" font-family="Segoe UI,Arial" font-size="10" fill="#94a3b8" text-anchor="middle">bounded queue (50)</text>

  <!-- Row 2 -->
  <!-- Card 5: Cross-platform -->
  <rect x="108" y="172" width="156" height="72" rx="10" fill="#1e1b4b" stroke="#2563EB" stroke-width="1.5"/>
  <text x="186" y="196" font-family="Arial" font-size="16" text-anchor="middle" fill="#2563EB">🖥️</text>
  <text x="186" y="214" font-family="Segoe UI,Arial" font-size="11" font-weight="700" fill="white" text-anchor="middle">Cross-platform</text>
  <text x="186" y="230" font-family="Segoe UI,Arial" font-size="10" fill="#94a3b8" text-anchor="middle">Win · Linux · macOS</text>

  <!-- Card 6: Keyboard control -->
  <rect x="284" y="172" width="156" height="72" rx="10" fill="#1e1b4b" stroke="#06B6D4" stroke-width="1.5"/>
  <text x="362" y="196" font-family="Arial" font-size="16" text-anchor="middle" fill="#06B6D4">⌨️</text>
  <text x="362" y="214" font-family="Segoe UI,Arial" font-size="11" font-weight="700" fill="white" text-anchor="middle">Keyboard Control</text>
  <text x="362" y="230" font-family="Segoe UI,Arial" font-size="10" fill="#94a3b8" text-anchor="middle">quit · fullscreen · normalise</text>

  <!-- Card 7: Maturity classes -->
  <rect x="460" y="172" width="188" height="72" rx="10" fill="#1e1b4b" stroke="#7C3AED" stroke-width="1.5"/>
  <text x="554" y="196" font-family="Arial" font-size="16" text-anchor="middle" fill="#7C3AED">🥥</text>
  <text x="554" y="214" font-family="Segoe UI,Arial" font-size="11" font-weight="700" fill="white" text-anchor="middle">Maturity Classes</text>
  <text x="554" y="230" font-family="Segoe UI,Arial" font-size="10" fill="#94a3b8" text-anchor="middle">mature · immature detection</text>
</svg>
</p>

---

## System Architecture

<p align="center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 370" width="780" height="370">
  <defs>
    <linearGradient id="archBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#0f172a"/>
      <stop offset="100%" style="stop-color:#1e1b4b"/>
    </linearGradient>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#7C3AED"/>
    </marker>
    <marker id="arrow2" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#06B6D4"/>
    </marker>
  </defs>
  <rect width="780" height="370" rx="14" fill="url(#archBg)"/>
  <text x="390" y="30" font-family="Segoe UI,Arial" font-size="14" fill="#a78bfa" text-anchor="middle" font-weight="600" letter-spacing="2">SYSTEM ARCHITECTURE</text>

  <!-- WEBCAM -->
  <rect x="30" y="55" width="130" height="60" rx="10" fill="#1e1b4b" stroke="#7C3AED" stroke-width="2"/>
  <text x="95" y="80" font-family="Arial" font-size="18" text-anchor="middle" fill="#7C3AED">📷</text>
  <text x="95" y="100" font-family="Segoe UI,Arial" font-size="12" font-weight="700" fill="white" text-anchor="middle">Webcam</text>
  <text x="95" y="114" font-family="Segoe UI,Arial" font-size="10" fill="#94a3b8" text-anchor="middle">cv2.VideoCapture(0)</text>

  <!-- Arrow 1 -->
  <line x1="160" y1="85" x2="200" y2="85" stroke="#7C3AED" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="180" y="78" font-family="Arial" font-size="9" fill="#94a3b8" text-anchor="middle">frame</text>

  <!-- INFERENCE -->
  <rect x="200" y="55" width="150" height="60" rx="10" fill="#1e1b4b" stroke="#2563EB" stroke-width="2"/>
  <text x="275" y="75" font-family="Arial" font-size="11" text-anchor="middle" fill="#06B6D4">YOLOv5</text>
  <text x="275" y="90" font-family="Segoe UI,Arial" font-size="11" font-weight="700" fill="white" text-anchor="middle">Inference Engine</text>
  <text x="275" y="105" font-family="Segoe UI,Arial" font-size="10" fill="#94a3b8" text-anchor="middle">best1.pt · torch.hub</text>

  <!-- Arrow 2 -->
  <line x1="350" y1="85" x2="390" y2="85" stroke="#7C3AED" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="370" y="78" font-family="Arial" font-size="9" fill="#94a3b8" text-anchor="middle">xyxy</text>

  <!-- CONFIDENCE FILTER -->
  <rect x="390" y="55" width="140" height="60" rx="10" fill="#1e1b4b" stroke="#06B6D4" stroke-width="2"/>
  <text x="460" y="80" font-family="Arial" font-size="18" text-anchor="middle" fill="#06B6D4">🎯</text>
  <text x="460" y="98" font-family="Segoe UI,Arial" font-size="11" font-weight="700" fill="white" text-anchor="middle">Confidence Filter</text>
  <text x="460" y="112" font-family="Segoe UI,Arial" font-size="10" fill="#94a3b8" text-anchor="middle">threshold ≥ 0.67</text>

  <!-- Arrow 3 -->
  <line x1="530" y1="85" x2="570" y2="85" stroke="#7C3AED" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- DRAW BOXES -->
  <rect x="570" y="55" width="175" height="60" rx="10" fill="#1e1b4b" stroke="#7C3AED" stroke-width="2"/>
  <text x="657" y="80" font-family="Segoe UI,Arial" font-size="11" font-weight="700" fill="white" text-anchor="middle">Draw Bounding Boxes</text>
  <text x="657" y="96" font-family="Segoe UI,Arial" font-size="10" fill="#94a3b8" text-anchor="middle">cv2.rectangle + putText</text>
  <text x="657" y="110" font-family="Segoe UI,Arial" font-size="10" fill="#94a3b8" text-anchor="middle">green box · red label</text>

  <!-- Arrow down from DRAW BOXES -->
  <line x1="657" y1="115" x2="657" y2="155" stroke="#7C3AED" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- cv2.imshow -->
  <rect x="570" y="155" width="175" height="55" rx="10" fill="#1e1b4b" stroke="#2563EB" stroke-width="1.5"/>
  <text x="657" y="178" font-family="Segoe UI,Arial" font-size="11" font-weight="700" fill="white" text-anchor="middle">cv2.imshow</text>
  <text x="657" y="195" font-family="Segoe UI,Arial" font-size="10" fill="#94a3b8" text-anchor="middle">Display Window (800×600)</text>

  <!-- Arrow detection path down -->
  <line x1="460" y1="115" x2="460" y2="155" stroke="#06B6D4" stroke-width="2" marker-end="url(#arrow2)"/>
  <text x="490" y="138" font-family="Arial" font-size="9" fill="#06B6D4" text-anchor="middle">detected?</text>

  <!-- SAVE QUEUE -->
  <rect x="355" y="155" width="160" height="55" rx="10" fill="#1e1b4b" stroke="#06B6D4" stroke-width="2"/>
  <text x="435" y="178" font-family="Segoe UI,Arial" font-size="11" font-weight="700" fill="white" text-anchor="middle">_save_queue</text>
  <text x="435" y="194" font-family="Segoe UI,Arial" font-size="10" fill="#94a3b8" text-anchor="middle">Queue(maxsize=50)</text>

  <!-- Arrow down -->
  <line x1="435" y1="210" x2="435" y2="250" stroke="#06B6D4" stroke-width="2" marker-end="url(#arrow2)"/>

  <!-- WORKER THREAD -->
  <rect x="355" y="250" width="160" height="55" rx="10" fill="#1e1b4b" stroke="#7C3AED" stroke-width="2"/>
  <text x="435" y="272" font-family="Segoe UI,Arial" font-size="11" font-weight="700" fill="white" text-anchor="middle">_save_worker</text>
  <text x="435" y="288" font-family="Segoe UI,Arial" font-size="10" fill="#94a3b8" text-anchor="middle">daemon=True thread</text>

  <!-- Arrow to disk -->
  <line x1="435" y1="305" x2="435" y2="330" stroke="#06B6D4" stroke-width="2" marker-end="url(#arrow2)"/>

  <!-- DISK -->
  <rect x="310" y="330" width="250" height="30" rx="10" fill="#1e1b4b" stroke="#06B6D4" stroke-width="1.5"/>
  <text x="435" y="350" font-family="Segoe UI,Arial" font-size="11" fill="#06B6D4" text-anchor="middle">CoconutDetection Pictures/ (JPEG)</text>

  <!-- YAML / MODEL paths -->
  <rect x="30" y="175" width="130" height="55" rx="10" fill="#1e1b4b" stroke="#7C3AED" stroke-width="1.5"/>
  <text x="95" y="198" font-family="Segoe UI,Arial" font-size="11" font-weight="700" fill="white" text-anchor="middle">data.yaml</text>
  <text x="95" y="215" font-family="Segoe UI,Arial" font-size="10" fill="#94a3b8" text-anchor="middle">class names</text>

  <line x1="160" y1="202" x2="200" y2="100" stroke="#a78bfa" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#arrow)"/>

  <!-- Legend -->
  <line x1="30" y1="295" x2="60" y2="295" stroke="#7C3AED" stroke-width="2"/>
  <text x="68" y="299" font-family="Arial" font-size="10" fill="#94a3b8">main thread</text>
  <line x1="30" y1="315" x2="60" y2="315" stroke="#06B6D4" stroke-width="2"/>
  <text x="68" y="319" font-family="Arial" font-size="10" fill="#94a3b8">worker thread</text>
  <line x1="30" y1="335" x2="60" y2="335" stroke="#a78bfa" stroke-width="1.5" stroke-dasharray="5,3"/>
  <text x="68" y="339" font-family="Arial" font-size="10" fill="#94a3b8">config load</text>
</svg>
</p>

---

## Data Flow

<p align="center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 140" width="780" height="140">
  <defs>
    <linearGradient id="dfBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#0f172a"/>
      <stop offset="100%" style="stop-color:#1e1b4b"/>
    </linearGradient>
    <marker id="df-arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#7C3AED"/>
    </marker>
  </defs>
  <rect width="780" height="140" rx="12" fill="url(#dfBg)"/>
  <text x="390" y="24" font-family="Segoe UI,Arial" font-size="13" fill="#a78bfa" text-anchor="middle" font-weight="600" letter-spacing="2">DATA FLOW</text>

  <!-- Nodes -->
  <rect x="10"  y="44" width="100" height="50" rx="8" fill="#312e81" stroke="#7C3AED" stroke-width="1.5"/>
  <text x="60"  y="66" font-family="Arial" font-size="10" fill="#c4b5fd" text-anchor="middle">Camera</text>
  <text x="60"  y="80" font-family="Arial" font-size="9"  fill="#94a3b8" text-anchor="middle">BGR frames</text>
  <text x="60"  y="92" font-family="Arial" font-size="9"  fill="#94a3b8" text-anchor="middle">numpy.ndarray</text>

  <line x1="110" y1="69" x2="138" y2="69" stroke="#7C3AED" stroke-width="1.5" marker-end="url(#df-arrow)"/>

  <rect x="138" y="44" width="112" height="50" rx="8" fill="#1e3a8a" stroke="#2563EB" stroke-width="1.5"/>
  <text x="194" y="66" font-family="Arial" font-size="10" fill="#93c5fd" text-anchor="middle">YOLOv5</text>
  <text x="194" y="80" font-family="Arial" font-size="9"  fill="#94a3b8" text-anchor="middle">model(frame)</text>
  <text x="194" y="92" font-family="Arial" font-size="9"  fill="#94a3b8" text-anchor="middle">results.xyxy[0]</text>

  <line x1="250" y1="69" x2="278" y2="69" stroke="#7C3AED" stroke-width="1.5" marker-end="url(#df-arrow)"/>

  <rect x="278" y="44" width="120" height="50" rx="8" fill="#164e63" stroke="#06B6D4" stroke-width="1.5"/>
  <text x="338" y="66" font-family="Arial" font-size="10" fill="#67e8f9" text-anchor="middle">Filter & Label</text>
  <text x="338" y="80" font-family="Arial" font-size="9"  fill="#94a3b8" text-anchor="middle">conf &gt; 0.67</text>
  <text x="338" y="92" font-family="Arial" font-size="9"  fill="#94a3b8" text-anchor="middle">x1,y1,x2,y2,cls</text>

  <line x1="398" y1="69" x2="426" y2="69" stroke="#7C3AED" stroke-width="1.5" marker-end="url(#df-arrow)"/>

  <rect x="426" y="44" width="120" height="50" rx="8" fill="#312e81" stroke="#7C3AED" stroke-width="1.5"/>
  <text x="486" y="66" font-family="Arial" font-size="10" fill="#c4b5fd" text-anchor="middle">Annotated Frame</text>
  <text x="486" y="80" font-family="Arial" font-size="9"  fill="#94a3b8" text-anchor="middle">bbox + label</text>
  <text x="486" y="92" font-family="Arial" font-size="9"  fill="#94a3b8" text-anchor="middle">cv2 display</text>

  <line x1="546" y1="69" x2="574" y2="69" stroke="#7C3AED" stroke-width="1.5" marker-end="url(#df-arrow)"/>

  <rect x="574" y="44" width="110" height="50" rx="8" fill="#164e63" stroke="#06B6D4" stroke-width="1.5"/>
  <text x="629" y="66" font-family="Arial" font-size="10" fill="#67e8f9" text-anchor="middle">Save Queue</text>
  <text x="629" y="80" font-family="Arial" font-size="9"  fill="#94a3b8" text-anchor="middle">async enqueue</text>
  <text x="629" y="92" font-family="Arial" font-size="9"  fill="#94a3b8" text-anchor="middle">frame.copy()</text>

  <line x1="684" y1="69" x2="712" y2="69" stroke="#06B6D4" stroke-width="1.5" marker-end="url(#df-arrow)"/>

  <rect x="712" y="44" width="60" height="50" rx="8" fill="#1e1b4b" stroke="#7C3AED" stroke-width="1.5"/>
  <text x="742" y="66" font-family="Arial" font-size="10" fill="#c4b5fd" text-anchor="middle">Disk</text>
  <text x="742" y="80" font-family="Arial" font-size="9"  fill="#94a3b8" text-anchor="middle">JPEG</text>
  <text x="742" y="92" font-family="Arial" font-size="9"  fill="#94a3b8" text-anchor="middle">timestamped</text>

  <!-- Timing bar -->
  <rect x="10" y="108" width="762" height="6" rx="3" fill="#1e1b4b"/>
  <rect x="10" y="108" width="128" height="6" rx="3" fill="#7C3AED"/>
  <rect x="138" y="108" width="140" height="6" rx="3" fill="#2563EB"/>
  <rect x="278" y="108" width="148" height="6" rx="3" fill="#06B6D4"/>
  <rect x="426" y="108" width="148" height="6" rx="3" fill="#7C3AED"/>
  <rect x="574" y="108" width="198" height="6" rx="3" fill="#06B6D4" opacity="0.6"/>
  <text x="390" y="130" font-family="Arial" font-size="9" fill="#64748b" text-anchor="middle">← main detection loop (per frame) ————————————————————— background I/O thread →</text>
</svg>
</p>

---

## Technology Stack

| Layer | Technology | Version | Purpose |
|---|---|---|---|
| Language | Python | 3.8+ | Application runtime |
| Deep Learning | PyTorch | latest | Model loading & GPU/CPU inference |
| Object Detection | YOLOv5 (Ultralytics) | custom | Coconut detection model |
| Computer Vision | OpenCV (`opencv-python`) | 4.x | Frame capture, drawing, display |
| Config | PyYAML | latest | Load class names from `data.yaml` |
| Concurrency | Python `threading` + `queue` | stdlib | Non-blocking image saving |
| Model Weights | `best1.pt` | custom-trained | YOLOv5s trained on coconut dataset |
| Platform | Windows / Linux / macOS | — | Cross-platform via pathlib patch |

---

## Features

| Feature | Detail |
|---|---|
| 🔴 Real-time inference | YOLOv5 runs on every webcam frame without frame-skipping |
| 🧠 Custom trained model | `best1.pt` — trained specifically on mature and immature coconuts |
| 🎯 Confidence filtering | Only detections ≥ **0.67** are visualised and saved |
| 💚 Visual annotation | Green bounding boxes + red confidence label overlaid on frame |
| 💾 Non-blocking auto-save | Background daemon thread drains a bounded queue (size 50) for disk I/O |
| 🕒 Timestamped output | Each saved JPEG follows `coconut_detection_YYYYMMDD_HHMMSS_ffffff.jpg` |
| 🖥️ Cross-platform | Windows PosixPath patch applied automatically on Windows systems |
| ⌨️ Keyboard shortcuts | Quit, close, fullscreen, and normalise window on the fly |
| 🔌 Configurable camera | `CAMERA_INDEX` constant supports multiple cameras or USB sources |
| 🐛 Queue overflow guard | Silently drops frames instead of blocking when queue is full |

---

## Installation

### Prerequisites

- Python **3.8** or later
- A USB or built-in **webcam**
- The weights file **`best1.pt`** (included in the repository)

### Steps

**1. Clone the repository**
```sh
git clone https://github.com/Kaelith69/coco.git
cd coco
```

**2. Create and activate a virtual environment** *(recommended)*
```sh
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

**3. Install dependencies**
```sh
pip install -r requirements.txt
```

> **GPU users (CUDA):** Install the CUDA-enabled PyTorch build first:
> ```sh
> pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
> pip install -r requirements.txt
> ```
> Select the correct CUDA version for your hardware from [pytorch.org/get-started/locally](https://pytorch.org/get-started/locally/).

**4. Verify model weights are present**
```
coco/
└── best1.pt   ← must exist before running
```

---

## Usage

```sh
python coco.py
```

A window titled **"Coconut Detection"** opens showing the live webcam feed.  
Coconuts detected with confidence ≥ 67 % are highlighted with a **green bounding box** and a **red label** showing the class name and confidence score.  
Each frame containing at least one detection is saved to `CoconutDetection Pictures/`.

---

## Configuration

All tunable parameters are constants at the top of `coco.py`:

| Constant | Default | Description |
|---|---|---|
| `MODEL_PATH` | `best1.pt` | Path to YOLOv5 custom weights |
| `YAML_PATH` | `AIYolov5/data.yaml` | Optional class-name override YAML |
| `SAVE_DIR` | `CoconutDetection Pictures` | Output folder for saved detection images |
| `CONFIDENCE_THRESHOLD` | `0.67` | Minimum confidence to accept and display a detection |
| `CAMERA_INDEX` | `0` | OpenCV camera index (`0` = default webcam) |
| `MIN_LABEL_Y` | `15` | Minimum Y offset to prevent labels drawing off the top edge |

---

## Keyboard Shortcuts

| Key | Action |
|---|---|
| `Q` / `q` / `Esc` | Quit the application cleanly |
| `C` / `c` | Close the display window |
| `M` / `m` | Toggle **fullscreen** mode |
| `N` / `n` | Return to **normal** (windowed) mode |

---

## Project Structure

```
coco/
├── coco.py                          # Main detection script
├── best1.pt                         # Pre-trained YOLOv5 weights (custom)
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
├── LICENSE                          # MIT license
├── wiki/                            # GitHub Wiki source pages
│   ├── Home.md
│   ├── Architecture.md
│   ├── Installation.md
│   ├── Usage.md
│   ├── Privacy.md
│   ├── Contributing.md
│   ├── Troubleshooting.md
│   └── Roadmap.md
└── AIYolov5/                        # YOLOv5 training artefacts
    └── content/yolov5/
        └── runs/
            ├── train/
            │   └── yolov5s_results/ # Training metrics, weights
            │       ├── weights/
            │       │   ├── best.pt
            │       │   └── last.pt
            │       ├── results.csv
            │       ├── results.png
            │       └── confusion_matrix.png
            └── detect/
                └── exp2/            # Sample detection results
```

---

## Performance

<p align="center">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 180" width="700" height="180">
  <defs>
    <linearGradient id="perfBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#0f172a"/>
      <stop offset="100%" style="stop-color:#1e1b4b"/>
    </linearGradient>
  </defs>
  <rect width="700" height="180" rx="12" fill="url(#perfBg)"/>
  <text x="350" y="28" font-family="Segoe UI,Arial" font-size="13" fill="#a78bfa" text-anchor="middle" font-weight="600" letter-spacing="2">PERFORMANCE STATS</text>

  <!-- Stat 1 -->
  <rect x="20" y="44" width="148" height="110" rx="10" fill="#1e1b4b" stroke="#7C3AED" stroke-width="1.5"/>
  <text x="94" y="80" font-family="Segoe UI,Arial" font-size="32" font-weight="800" fill="#7C3AED" text-anchor="middle">30+</text>
  <text x="94" y="100" font-family="Arial" font-size="10" fill="#c4b5fd" text-anchor="middle">FPS (GPU)</text>
  <text x="94" y="118" font-family="Arial" font-size="9" fill="#64748b" text-anchor="middle">real-time inference</text>
  <text x="94" y="132" font-family="Arial" font-size="9" fill="#64748b" text-anchor="middle">on modern GPU</text>

  <!-- Stat 2 -->
  <rect x="184" y="44" width="148" height="110" rx="10" fill="#1e1b4b" stroke="#2563EB" stroke-width="1.5"/>
  <text x="258" y="80" font-family="Segoe UI,Arial" font-size="32" font-weight="800" fill="#2563EB" text-anchor="middle">0.67</text>
  <text x="258" y="100" font-family="Arial" font-size="10" fill="#93c5fd" text-anchor="middle">Conf Threshold</text>
  <text x="258" y="118" font-family="Arial" font-size="9" fill="#64748b" text-anchor="middle">reduces false positives</text>
  <text x="258" y="132" font-family="Arial" font-size="9" fill="#64748b" text-anchor="middle">tunable in coco.py</text>

  <!-- Stat 3 -->
  <rect x="348" y="44" width="148" height="110" rx="10" fill="#1e1b4b" stroke="#06B6D4" stroke-width="1.5"/>
  <text x="422" y="80" font-family="Segoe UI,Arial" font-size="32" font-weight="800" fill="#06B6D4" text-anchor="middle">50</text>
  <text x="422" y="100" font-family="Arial" font-size="10" fill="#67e8f9" text-anchor="middle">Queue Size</text>
  <text x="422" y="118" font-family="Arial" font-size="9" fill="#64748b" text-anchor="middle">bounded save queue</text>
  <text x="422" y="132" font-family="Arial" font-size="9" fill="#64748b" text-anchor="middle">never blocks inference</text>

  <!-- Stat 4 -->
  <rect x="512" y="44" width="168" height="110" rx="10" fill="#1e1b4b" stroke="#7C3AED" stroke-width="1.5"/>
  <text x="596" y="80" font-family="Segoe UI,Arial" font-size="32" font-weight="800" fill="#7C3AED" text-anchor="middle">2</text>
  <text x="596" y="100" font-family="Arial" font-size="10" fill="#c4b5fd" text-anchor="middle">Detection Classes</text>
  <text x="596" y="118" font-family="Arial" font-size="9" fill="#64748b" text-anchor="middle">mature coconut</text>
  <text x="596" y="132" font-family="Arial" font-size="9" fill="#64748b" text-anchor="middle">immature coconut</text>
</svg>
</p>

> **Note:** Inference speed depends on hardware. CPU-only machines will achieve lower FPS. For real-time performance at 1080p, a CUDA-capable GPU is recommended.

---

## Use Cases

- 🌴 **Farm monitoring** — mount a camera in a coconut grove and log all detections for maturity tracking
- 🗓️ **Harvest planning** — review saved images to identify trees with a high proportion of mature coconuts
- 📊 **Research / dataset expansion** — collect new annotated images directly from the detection output folder
- ⚡ **Edge deployment** — run on Raspberry Pi 4 or Jetson Nano with a USB camera for low-cost field use

---

## Accessibility

- The detection window can be resized via keyboard (`M`/`N`) for use with different display sizes and assistive magnification tools.
- Bounding boxes use a high-contrast green (#00FF00) against the camera feed, and labels use red (#FF0000) for maximum legibility.
- All console output uses plain text for compatibility with screen readers and terminal assistive tools.
- The application exits cleanly via `Esc`, `Q`, or `C` — no mouse interaction required.

---

## Privacy & Security

- **No network transmission** — all inference runs locally on device. No frames, detections, or metadata are sent to any remote server.
- **Local-only storage** — saved images are written only to the local `CoconutDetection Pictures/` directory.
- **No personal data** — the model detects coconuts only; no biometric, personal, or identifying information is processed.
- **No external telemetry** — the application does not call home, update automatically, or collect usage statistics.
- **Model loading** — `torch.hub.load` with `force_reload=False` prevents unintended network model downloads after initial setup.

---

## Roadmap

| Status | Feature |
|---|---|
| ✅ | Real-time YOLOv5 webcam detection |
| ✅ | Auto timestamped JPEG saving |
| ✅ | Confidence threshold filtering |
| ✅ | Cross-platform support |
| 🔲 | Detection count overlay on frame |
| 🔲 | RTSP / IP camera stream support |
| 🔲 | CSV/JSON detection log export |
| 🔲 | REST API for remote monitoring |
| 🔲 | Model retraining pipeline documentation |
| 🔲 | Raspberry Pi / Jetson Nano deployment guide |
| 🔲 | GUI configuration panel |
| 🔲 | Video file input mode |

---

## Design Principles

1. **Separation of concerns** — inference, display, and disk I/O run in distinct logical stages
2. **Non-blocking I/O** — a bounded queue prevents disk latency from degrading detection throughput
3. **Fail-safe degradation** — a full queue drops frames rather than stalling the main loop
4. **Minimal configuration surface** — all tunable constants are co-located at the top of `coco.py`
5. **Platform neutrality** — a single `pathlib` patch handles the Windows/Unix path incompatibility transparently

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for bug fixes, model improvements, or new features. See [`wiki/Contributing.md`](wiki/Contributing.md) for the full guide.

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
