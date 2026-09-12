<div align="center">

  <img src="assets/og-banner.png" alt="Tangent Suite Banner" width="550" />

  <p align="center">
    <strong>Ultra-fast, 100% private, client-side digital utilities.</strong><br>
    Break away from bloated web apps. Process documents, compress images, and organize files locally without transmitting a single byte to an external server.
  </p>

  <p align="center">
    <a href="https://misbah-37.github.io/tangent/"><strong>Explore Live Site »</strong></a>
    <br />
    <br />
    <img src="https://img.shields.io/badge/Privacy-100%25%20Client--Side-00d2ff?style=flat-square" alt="Privacy" />
    <img src="https://img.shields.io/badge/Telemetry-Zero-success?style=flat-square" alt="No Telemetry" />
    <img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square" alt="License" />
  </p>

</div>

---

## ⚡ The Tangent Philosophy

Most utility websites quietly upload your sensitive photos, contracts, and financial PDFs to remote cloud servers to process them. 

**Tangent is engineered differently:**
- **0 Bytes Outbound:** All web tools run 100% inside your browser's local sandbox via WebAssembly and client-side JavaScript.
- **No Accounts, No Tracking:** Zero sign-ups, zero analytics cookies, and zero personal data collection.
- **Offline Capable:** Once loaded, web utilities continue running seamlessly even if you disconnect from the internet.

---

## 🛠️ The Toolkit

### 1. 📄 PDF Suite (`pdf-converter.html`)
- **Features:** Merge multiple PDFs, split documents, extract page ranges, and perform structural compression.
- **Engine:** Client-side execution using [`pdf-lib`](https://pdf-lib.js.org/) and [`pdf.js`](https://mozilla.github.io/pdf.js/). Your files never leave RAM.

### 2. 📁 Desktop File Organizer (`file-organizer.html`)
- **Features:** Native standalone Windows utility that sorts cluttered directories (e.g. `Downloads`, `Desktop`) into 12 distinct categories in seconds.
- **Compiled with Nuitka:** Direct C-binary compilation with minimal heuristic profile.
- **Integrity (SHA-256):** `fe54fa49bde4b8830c8c47b5b3b3c9cfa22fe5a625a2ed18ce71b72a4f7f0b72`
- **VirusTotal:** [Verified Clean Report](https://www.virustotal.com/gui/file/fe54fa49bde4b8830c8c47b5b3b3c9cfa22fe5a625a2ed18ce71b72a4f7f0b72)

### 3. 🖼️ Photo Resizer (`photo-resizer.html`)
- **Features:** Scale dimensions, constrain proportions, adjust compression quality, and convert image formats (JPEG, PNG, WebP) in real time.
- **Engine:** Hardware-accelerated HTML5 Canvas 2D rasterization.

### 4. 📱 QR Code Generator (`qr-generator.html`)
- **Features:** Generate high-density, error-corrected QR codes for URLs, Wi-Fi networks, and contact cards with custom colors and instant PNG downloads.
- **Engine:** Lightweight client-side QR generation engine.

### 5. ⌨️ Typing Speed Test (`typing-test.html`)
- **Features:** Clean, distraction-free typing benchmark with real-time WPM, accuracy calculation, error highlighting, and difficulty tiers.
- **Privacy:** Best scores saved locally via `localStorage`.

---

## 🚀 Running Locally

Because Tangent is built with modern vanilla web standards, you don't need `npm install` or complex build pipelines.

Simply clone the repository and serve the files locally:

```bash
# Clone the repository
git clone https://github.com/Misbah-37/tangent.git

# Navigate to directory
cd omnitools-web

# Serve with Python
python -m http.server 8000

# Or serve with Node.js
npx serve .
```

Open `http://localhost:8000` in your browser.

---

## 🔒 Security & Architecture

| Feature | Tangent Implementation |
| :--- | :--- |
| **Server Uploads** | **None.** Processing occurs in browser memory or native offline binary. |
| **Content Security Policy** | Strict inline execution with pinned CDNs (`cdnjs.cloudflare.com`, `cdn.jsdelivr.net`). |
| **Network Telemetry** | No Google Analytics, no Facebook Pixel, no tracking pixels. |
| **Data Retention** | Data disappears as soon as you close or refresh the tab. |

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information. Built for speed, privacy, and precision.
