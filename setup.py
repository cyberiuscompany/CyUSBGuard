from setuptools import setup, find_packages

setup(
    name="cyusbguard",
    version="1.0.0",
    description="Herramienta de análisis de USBs con integración con VirusTotal",
    author="Cyberius Company",
    author_email="contacto@cyberiuscompany.com",
    url="https://github.com/cyberiuscompany/CyUSBGuard",
    packages=find_packages(),
    py_modules=["cyusbguard", "ver_informe_en_frame"],
    include_package_data=True,
    package_data={
        "": [
            "index.html",
            "estilos.css",
            "script.js",
            "icono.png",
            "cyberius.ico",
            "config.json"
        ]
    },
    install_requires=[
        "pystray",
        "Pillow",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "cyusbguard=cyusbguard:lanzar_app"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.7',
)
