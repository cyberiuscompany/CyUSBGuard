
![GitHub release downloads](https://img.shields.io/github/downloads/CyberiusCompany/Cyberius-Unzip-Cracker/latest/total)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![System](https://img.shields.io/badge/windows-x64-green)
![System](https://img.shields.io/badge/linux-x64-green)
![License](https://img.shields.io/badge/license-Private-red)
![Usage](https://img.shields.io/badge/usage-legal%20only-important)
![Python](https://img.shields.io/badge/python-3.7%2B-yellow)
![Tested on](https://img.shields.io/badge/tested%20on-Windows%2010%2F11%20%7C%20Ubuntu%2022.04-blue)

<p align="center">
  <a href="README.md">
    <img src="https://flagcdn.com/w40/es.png" alt="Español" title="Español">
    <strong>Español</strong>
  </a>
  &nbsp;|&nbsp;
  <img src="https://flagcdn.com/w40/us.png" alt="English" title="English">
  <strong>English</strong>
  &nbsp;|&nbsp;
  <a href="https://www.youtube.com/watch?v=xvFZjo5PgG0&list=RDxvFZjo5PgG0&start_radio=1&pp=ygUTcmljayByb2xsaW5nIG5vIGFkc6AHAQ%3D%3D">
    <img src="https://flagcdn.com/w40/jp.png" alt="Japanese" title="Japanese">
    <strong>日本語</strong>
  </a>
</p>

# CyUSBGuard

USB analysis tool with VirusTotal API integration and background monitoring capabilities.

- DeepWiki: https://deepwiki.com/cyberiuscompany/CyUSBGuard

---

<p align="center">
  <img src="icono.png" alt="Banner" width="500"/>
</p>

---

## Tool Screenshots

<h2 align="center">Main Menu</h2>
<p align="center">
  <img src="Menu-principal.png" alt="Main Menu" width="500"/>
</p>

<h2 align="center">Web Report Option</h2>
<p align="center">
  <img src="Opcion-Pagina-Web.png" alt="Web Option" width="500"/>
</p>

<h2 align="center">Background Options</h2>
<p align="center">
  <img src="Opciones Segundo Plano.png" alt="Background Options" width="500"/>
</p>

<h2 align="center">Running in Background</h2>
<p align="center">
  <img src="Programa en Segundo Plano.png" alt="Background Mode" width="500"/>
</p>

<h2 align="center">Web Scan Result</h2>
<p align="center">
  <img src="Resultado Analisis Web.png" alt="Web Scan Result" width="500"/>
</p>

<h2 align="center">Local Scan Result</h2>
<p align="center">
  <img src="Resultado de Analisis.png" alt="Local Scan Result" width="500"/>
</p>

<h2 align="center">Detailed Web Report</h2>
<p align="center">
  <img src="Resultado en Web A detalle del analisis.png" alt="Detailed Web Result" width="500"/>
</p>

---

## Description

**CyUSBGuard** is a Python-based GUI tool that analyzes connected USB devices. It allows automatic and manual scanning of files using the VirusTotal API.

Built for cybersecurity use in educational, enterprise, or home environments.

## 🚀 Key Features

- Automatic detection of connected USB drives.
- Hash-based file scanning with VirusTotal API.
- Graphical result visualization.
- Use your own API key.
- Passive background scanning (stealth mode).
- HTML and visual report generation.
- Windows compatibility.
- Simple and customizable interface.

## 🧰 Technologies Used

- Python 3.x
- PyQt5
- pystray
- PIL (Pillow)
- requests
- webbrowser
- json

## 📁 Project Structure

```bash
├── cyusbguard.py                  # Main script
├── ver_informe_en_frame.py       # Embedded HTML report view
├── index.html                    # Report HTML
├── config.json                   # Configuration and API Key
├── estilos.css                   # Styling for report
├── script.js                     # JS logic for report
├── icono.png / cyberius.ico      # App icons
├── requirements.txt              # Dependencies
├── README.md                     # This file
```

---

## 📄 Additional Documentation

- [🔐 Security](.github/SECURITY.md)
- [📜 License](LICENSE)
- [🤝 Code of Conduct](.github/CODE_OF_CONDUCT.md)
- [📬 Contributing](.github/CONTRIBUTING.md)
- [📢 Support](.github/SUPPORT.md)
- [⚠️ Legal Notice](DISCLAIMER.md)

---

## ⚙️ 1.1 Basic Installation 🪟 Windows

```bash
git clone https://github.com/cyberiuscompany/CyUSBGuard.git
cd CyUSBGuard
python -m venv venv
.env\Scriptsctivate
pip install -r requirements.txt
python cyusbguard.py
```

## ⚙️ 1.2 Basic Installation 🐧 Linux / macOS

```bash
git clone https://github.com/cyberiuscompany/CyUSBGuard.git
cd CyUSBGuard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 cyusbguard.py
```

## ⚙️ 2. Professional Package Installation

```bash
git clone https://github.com/cyberiuscompany/CyUSBGuard.git
cd CyUSBGuard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install .
cyusbguard
```
