
import tkinter as tk
from tkinter import scrolledtext
import json
import os

COLOR_BG = "#2d3037"
COLOR_TXT = "#ffffff"
COLOR_CAJA = "#4f5354"
COLOR_DETALLE = "#83f1e8"

def mostrar_informe_en_frame(frame):
    frame.configure(bg=COLOR_BG)
    for widget in frame.winfo_children():
        widget.destroy()

    ruta_json = os.path.join(os.getcwd(), "informe_usb.json")
    if not os.path.exists(ruta_json):
        lbl = tk.Label(frame, text="No se encontró el archivo informe_usb.json", fg="red", bg=COLOR_BG)
        lbl.pack(pady=10)
        return

    with open(ruta_json, encoding="utf-8") as f:
        data = json.load(f)

    info = data.get("info_dispositivo", {})
    archivos = data.get("archivos", [])

    titulo = tk.Label(frame, text="Información del Dispositivo", font=("Arial", 14, "bold"), fg=COLOR_DETALLE, bg=COLOR_BG)
    titulo.pack(pady=(10, 2))

    for k, v in info.items():
        linea = f"{k.replace('_', ' ').capitalize()}: {v}"
        lbl = tk.Label(frame, text=linea, fg=COLOR_TXT, bg=COLOR_BG, anchor="w", justify="left")
        lbl.pack(fill="x", padx=20)

    sep = tk.Label(frame, text="Archivos encontrados", font=("Arial", 14, "bold"), fg=COLOR_DETALLE, bg=COLOR_BG)
    sep.pack(pady=(15, 5))

    caja = scrolledtext.ScrolledText(frame, wrap="word", height=20, bg=COLOR_CAJA, fg=COLOR_TXT)
    for arch in archivos:
        caja.insert("end", f"{arch.get('archivo', 'Sin nombre')} - {arch.get('ruta', '')}\n")
        if "virustotal" in arch:
            vt = arch["virustotal"]
            if "detecciones" in vt:
                d = vt["detecciones"]
                caja.insert("end", f"  VT: Maliciosos: {d.get('malicious', 0)}, Sospechosos: {d.get('suspicious', 0)}\n")
            elif "error" in vt:
                caja.insert("end", f"  VT: {vt['error']}\n")
        caja.insert("end", "-"*50 + "\n")
    caja.config(state="disabled")
    caja.pack(fill="both", expand=True, padx=20, pady=10)
