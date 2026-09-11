# OmniTools ⚡

> **Fast, private, and 100% client-side digital utilities.** Process documents, resize images, generate QR codes, and organize files locally without sending a single byte to an external server.

🌐 **Live Website:** [https://misbah-37.github.io/omnitools-web/](https://misbah-37.github.io/omnitools-web/)

---

## 🛡️ The Privacy Promise

Most online utility sites quietly upload your sensitive photos, contracts, and documents to remote cloud servers to process them. **OmniTools is fundamentally different:**

* **0 Bytes Outbound**: All web utilities run entirely within your local browser sandbox via modern WebAssembly and JavaScript engines.
* **No Database / No Accounts**: No sign-ups, no tracking cookies, and zero analytical telemetry.
* **Offline Capable**: Once loaded, web tools continue functioning even if you disconnect from the internet.

---

## 🛠️ Included Utilities

### 1. 📄 PDF Suite (`pdf-converter.html`)
* **Features**: Merge multiple PDFs, split documents, extract selected pages, and perform structural compression.
* **Engine**: Built with [`pdf-lib`](https://pdf-lib.js.org/), [`pdf.js`](https://mozilla.github.io/pdf.js/), and [`jsPDF`](https://github.com/parallax/jsPDF).

### 2. 📁 Desktop File Organizer (`file-organizer.html`)
* **Features**: Native standalone Windows utility that categorizes messy folders (e.g. `Downloads`, `Desktop`) into 12 distinct categories in seconds.
* **Security & Integrity**: 
  * **Network Access**: 0 Bytes (Completely offline).
  * **Integrity Hash (SHA-256)**: `fb1f049609e868132699d07f07736423b821371cfce3d146469f689a7ed4fca2`
  * **VirusTotal**: [0/70 Detections Clean](https://www.virustotal.com/gui/file/fb1f049609e868132699d07f07736423b821371cfce3d146469f689a7ed4fca2)

### 3. 🖼️ Photo Resizer & Compressor (`photo-resizer.html`)
* **Features**: In-browser cropping, 1-click dimension presets (Passport, Square Avatar, Social Banner, Document A4), target KB compression, and PNG (lossless) vs. JPG format selection.
* **Engine**: Powered by [`Cropper.js`](https://github.com/fengyuanchen/cropperjs) and HTML5 Canvas.

### 4. 📱 QR Code Generator (`qr-generator.html`)
* **Features**: Instant static QR code generation for links and text, custom background/foreground colors, and PNG export.
* **Engine**: Powered by [`QRious`](https://github.com/neocotic/qrious).

### 5. ⌨️ Typing Speed Test (`typing-test.html`)
* **Features**: Real-time WPM counter, instant wrong-key error feedback, mobile keyboard support, and local personal best high-score retention via `localStorage`.

---

## 🚀 Tech Stack

* **Frontend**: Pure Semantic HTML5, Vanilla CSS3 (Obsidian Dark Theme, Glassmorphism, CSS Grid & Flexbox).
* **JavaScript**: Modern ES6+ (Zero bloated frameworks).
* **SEO**: OpenGraph Protocol, Semantic Schema.org (`FAQPage` & `WebApplication`) JSON-LD structured data.
* **Hosting**: GitHub Pages with HTTPS encryption.

---

## 📄 License & Rights

Copyright © 2026 OmniTools. All rights reserved.
