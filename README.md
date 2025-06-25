# CyUSBGuard

![GitHub release downloads](https://img.shields.io/github/downloads/CyberiusCompany/Cyberius-Unzip-Cracker/latest/total)
![Versión](https://img.shields.io/badge/versión-1.0.0-blue)
![Sistema](https://img.shields.io/badge/windows-x64-green)
![Sistema](https://img.shields.io/badge/linux-x64-green)
![Licencia](https://img.shields.io/badge/licencia-Privada-red)
![Uso](https://img.shields.io/badge/uso-solo%20legal-important)
![Python](https://img.shields.io/badge/python-3.7%2B-yellow)

Herramienta de análisis de USBs, con integración mediante API de VirusTotal y funcionamiento en segundo plano.

---

<p align="center">
  <img src="icono.png" alt="Banner" width="500"/>
</p

---

## Descripción

**CyUSBGuard** es una herramienta desarrollada en Python con interfaz gráfica que analiza dispositivos USB conectados al sistema, permitiendo realizar escaneos automáticos y manuales de archivos mediante la API de VirusTotal. 

Diseñada con un enfoque de ciberseguridad para entornos educativos, empresariales o domésticos.

## 🚀 Funcionalidades principales

- Detección automática de unidades USB conectadas.
- Escaneo de archivos con hashes y envío a VirusTotal.
- Visualización gráfica de resultados.
- Integración con tu propia clave API.
- Análisis pasivo en segundo plano (modo sigiloso).
- Generación de informes visuales y en HTML.
- Compatibilidad con Windows.
- Interfaz sencilla y personalizable.

## 🧰 Tecnologías utilizadas

- Python 3.x
- PyQt5
- pystray
- PIL (Pillow)
- requests
- webbrowser
- json

## 📁 Estructura del proyecto

```bash
├── cyusbguard.py # Código principal
├── ver_informe_en_frame.py # Vista de informe HTML incrustada
├── index.html # Vista web del informe
├── config.json # Configuración y API Key
├── estilos.css # Estilos de la vista
├── script.js # Lógica JS del informe
├── icono.png / cyberius.ico # Iconos de la app
├── requirements.txt # Dependencias
├── README.md # Este archivo
```

## ⚙️ Instalación y ejecución
```bash
# 1. Crear entorno virtual
python -m venv venv

# 2. Activarlo (en Windows)
.\venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar la herramienta
python cyusbguard.py

