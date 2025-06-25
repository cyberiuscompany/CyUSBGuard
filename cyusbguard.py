import os
import hashlib
import json
import tkinter as tk
from tkinter import messagebox, ttk
import psutil
import win32api
import win32con
import win32file
import requests
import threading
from datetime import datetime
from ver_informe_en_frame import mostrar_informe_en_frame
import webbrowser
from PIL import Image
import pystray
import sys
import time

CONFIG_FILE = "config.json"
ICON_PATH = "cyberius.ico"

usb_monitor_thread = None
running = True


def cargar_configuracion():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {"api_key": ""}

def guardar_configuracion(api_key):
    with open(CONFIG_FILE, 'w') as f:
        json.dump({"api_key": api_key}, f)

def obtener_unidades_usb():
    unidades = []
    for part in psutil.disk_partitions():
        if 'removable' in part.opts or part.fstype != '':
            try:
                volumen = win32api.GetVolumeInformation(part.device)
                unidades.append((part.device.replace("\\", "").replace(":", ""), volumen[0]))
            except:
                continue
    return unidades

def obtener_info_archivo(ruta, api_key):
    try:
        stat = os.stat(ruta)
        with open(ruta, 'rb') as f:
            contenido = f.read()
            md5 = hashlib.md5(contenido).hexdigest()
            sha1 = hashlib.sha1(contenido).hexdigest()
            sha256 = hashlib.sha256(contenido).hexdigest()

        atributos = win32file.GetFileAttributes(ruta)
        oculto = bool(atributos & win32con.FILE_ATTRIBUTE_HIDDEN)
        solo_lectura = bool(atributos & win32con.FILE_ATTRIBUTE_READONLY)
        sistema = bool(atributos & win32con.FILE_ATTRIBUTE_SYSTEM)

        resultado_vt = {}
        if api_key:
            headers = {"x-apikey": api_key}
            url = f"https://www.virustotal.com/api/v3/files/{sha256}"
            resp = requests.get(url, headers=headers)
            if resp.status_code == 200:
                data = resp.json()
                resultado_vt = {
                    "detecciones": data['data']['attributes']['last_analysis_stats'],
                    "permalink": f"https://www.virustotal.com/gui/file/{sha256}"
                }
            else:
                resultado_vt = {"error": f"Este fichero no tiene reportes como Maliciso (HTTP {resp.status_code})"}

        return {
            "archivo": os.path.basename(ruta),
            "ruta": ruta,
            "tamaño_bytes": stat.st_size,
            "fecha_creacion": datetime.fromtimestamp(stat.st_ctime).isoformat(),
            "fecha_modificacion": datetime.fromtimestamp(stat.st_mtime).isoformat(),
            "fecha_acceso": datetime.fromtimestamp(stat.st_atime).isoformat(),
            "md5": md5,
            "sha1": sha1,
            "sha256": sha256,
            "oculto": oculto,
            "solo_lectura": solo_lectura,
            "sistema": sistema,
            "ext": os.path.splitext(ruta)[1],
            "es_ejecutable": ruta.lower().endswith(('.exe', '.bat', '.cmd', '.vbs', '.ps1')),
            "virustotal": resultado_vt
        }
    except Exception as e:
        return {"error": str(e), "ruta": ruta}

def obtener_info_usb(letra_unidad):
    try:
        path = letra_unidad + ":\\"
        volumen = win32api.GetVolumeInformation(path)
        uso_disco = psutil.disk_usage(path)

        return {
            "letra_unidad": letra_unidad,
            "etiqueta_volumen": volumen[0],
            "sistema_archivos": volumen[4],
            "numero_serie": volumen[1],
            "espacio_total_MB": round(uso_disco.total / (1024 * 1024), 2),
            "espacio_usado_MB": round(uso_disco.used / (1024 * 1024), 2),
            "espacio_libre_MB": round(uso_disco.free / (1024 * 1024), 2),
            "porcentaje_usado": uso_disco.percent
        }
    except Exception as e:
        return {"error": str(e)}

def analizar_usb(letra_unidad, api_key, progreso, callback_final):
    progreso["value"] = 0
    progreso.update()
    path_base = letra_unidad + ":\\" if not letra_unidad.endswith(":") else letra_unidad + "\\"
    info_usb = obtener_info_usb(letra_unidad)
    archivos_info = []
    total_archivos = sum(len(files) for _, _, files in os.walk(path_base))
    procesados = 0

    for root, _, files in os.walk(path_base):
        for nombre in files:
            ruta = os.path.join(root, nombre)
            info = obtener_info_archivo(ruta, api_key)
            archivos_info.append(info)
            procesados += 1
            progreso["value"] = (procesados / total_archivos) * 100
            progreso.update()

    informe = {
        "info_dispositivo": info_usb,
        "archivos": archivos_info
    }

    ruta_json = os.path.join(os.getcwd(), "informe_usb.json")
    if os.path.exists(ruta_json):
        os.remove(ruta_json)
    with open(ruta_json, "w", encoding="utf-8") as f:
        json.dump(informe, f, indent=2, ensure_ascii=False)

    callback_final(ruta_json)

def lanzar_a_bandeja(root):
    root.withdraw()

    def on_restore(icon, item):
        icon.stop()
        root.after(0, root.deiconify)

    def on_exit(icon, item):
        global running
        running = False
        icon.stop()
        root.destroy()

    image = Image.open(ICON_PATH)
    menu = pystray.Menu(
        pystray.MenuItem("Volver a menu", on_restore),
        pystray.MenuItem("Cerrar Herramienta", on_exit)
    )
    icon = pystray.Icon("cyusbguard", image, "CyUSBGuard", menu)
    threading.Thread(target=icon.run, daemon=True).start()

def monitorizar_usb(letra):
    global running
    while running:
        unidades = [p.device.replace(":\\", "") for p in psutil.disk_partitions() if 'removable' in p.opts]
        if letra not in unidades:
            messagebox.showinfo("Finalizado", f"USB {letra}:\\ se ha desconectado. Cerrando herramienta.")
            os._exit(0)
        time.sleep(3)

def lanzar_app():
    config = cargar_configuracion()
    root = tk.Tk()
    root.title("Cyberius USB Guard")
    root.geometry("950x700")
    root.configure(bg="#2d3037")
    root.iconbitmap(ICON_PATH)

    tk.Label(root, text="Selecciona una unidad USB:", bg="#2d3037", fg="white").pack(pady=5)
    unidades = obtener_unidades_usb()
    opciones = [f"{letra}:\\ ({nombre})" for letra, nombre in unidades]
    seleccion = tk.StringVar()
    combo = ttk.Combobox(root, textvariable=seleccion, values=opciones, state="readonly")
    combo.pack()

    tk.Label(root, text="API Key de VirusTotal Utilizada:", bg="#2d3037", fg="white").pack(pady=5)
    api_entry = tk.Entry(root, justify='center')
    api_entry.insert(0, config.get("api_key", ""))
    api_entry.pack()

    progreso = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
    progreso.pack(pady=20)

    path_label = tk.Label(root, text="", wraplength=800, bg="#2d3037", fg="#83f1e8")
    path_label.pack(pady=5)

    resultado_frame = tk.Frame(root, bg="#2d3037")
    resultado_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def lanzar_analisis():
        opcion = seleccion.get()
        if not opcion:
            messagebox.showerror("Error", "Selecciona una unidad.")
            return

        letra = opcion.split(":")[0]
        api_key = api_entry.get().strip()
        guardar_configuracion(api_key)

        btn_analizar.config(state=tk.DISABLED)
        path_label.config(text="")
        resultado_frame.destroy()
        nuevo_frame = tk.Frame(root, bg="#2d3037")
        nuevo_frame.pack(fill="both", expand=True, padx=10, pady=10)

        def done_callback(ruta_final):
            path_label.config(text=f"\u2714 Informe guardado en:{ruta_final}")
            btn_analizar.config(state=tk.NORMAL)
            mostrar_informe_en_frame(nuevo_frame)

        threading.Thread(target=analizar_usb, args=(letra, api_key, progreso, done_callback)).start()

    def abrir_web():
        webbrowser.open("https://cyberiuscompany.github.io/CyUSBGuard/")

    btn_analizar = tk.Button(root, text="Analizar USB", command=lanzar_analisis, bg="#4f5354", fg="white")
    btn_analizar.pack(pady=10)

    tk.Button(root, text="Ver en Web", command=abrir_web, bg="#4f5354", fg="white").pack(pady=5)
    tk.Button(root, text="Minimizar a bandeja", command=lambda: [lanzar_a_bandeja(root), threading.Thread(target=monitorizar_usb, args=(seleccion.get().split(":")[0],), daemon=True).start()], bg="#4f5354", fg="white").pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    try:
        lanzar_app()
    except Exception as e:
        import traceback
        with open("error_log.txt", "w", encoding="utf-8") as f:
            f.write(traceback.format_exc())
        import time
        time.sleep(5)