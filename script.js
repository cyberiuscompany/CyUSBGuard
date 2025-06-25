function marcarPaso(paso) {
  if (paso === 1) {
    document.getElementById('step2').classList.remove('oculto');
  } else if (paso === 2) {
    document.getElementById('step3').classList.remove('oculto');
  }
}

function analizarJSON() {
  const fileInput = document.getElementById('jsonFile');
  const barra = document.getElementById('barraCarga');
  const progreso = document.getElementById('progreso');

  if (!fileInput.files.length) {
    alert("Por favor selecciona un archivo JSON.");
    return;
  }

  const reader = new FileReader();
  reader.onload = function (event) {
    try {
      const data = JSON.parse(event.target.result);

      document.getElementById('step1').classList.add('oculto');
      document.getElementById('step2').classList.add('oculto');
      document.getElementById('step3').classList.add('oculto');
      barra.classList.remove('oculto');
      progreso.style.width = '0%';

      setTimeout(() => {
        progreso.style.width = '100%';
        setTimeout(() => {
          barra.classList.add('oculto');
          mostrarResultados(data);
        }, 2000);
      }, 500);
    } catch (e) {
      alert("El archivo no es un JSON válido.");
    }
  };
  reader.readAsText(fileInput.files[0]);
}

function mostrarResultados(data) {
  const resultados = document.getElementById('resultados');
  resultados.classList.remove('oculto');
  resultados.innerHTML = "<h2>Información del Dispositivo</h2>";

  const info = data.info_dispositivo || {};

  resultados.innerHTML += `
    <p><b>Unidad:</b> ${info.letra_unidad || 'N/D'}</p>
    <p><b>Etiqueta:</b> ${info.etiqueta_volumen || 'N/D'}</p>
    <p><b>Sistema de archivos:</b> ${info.sistema_archivos || 'N/D'}</p>
    <p><b>Espacio total:</b> 
      ${info.espacio_total_MB ?? 'N/D'} MB 
      (${info.espacio_total_MB ? (info.espacio_total_MB / 1024).toFixed(2) + ' GB' : 'N/D'})
    </p>
    <p><b>Espacio libre:</b> 
      ${info.espacio_libre_MB ?? 'N/D'} MB 
      (${info.espacio_libre_MB ? (info.espacio_libre_MB / 1024).toFixed(2) + ' GB' : 'N/D'})
    </p>
    <p><b>Porcentaje usado:</b> ${info.porcentaje_usado ?? 'N/D'}%</p>
    <hr>
    <h2>Archivos encontrados</h2>
  `;

  if (!Array.isArray(data.archivos)) {
    resultados.innerHTML += `<p style="color:red;"><b>No se encontraron archivos en el JSON.</b></p>`;
    return;
  }

  data.archivos.forEach(item => {
    const vt = item.virustotal || {};
    let vt_html = '';

    if (vt.detecciones) {
      const detecciones = vt.detecciones;
      const totalMaliciosos = detecciones.malicious || 0;
      const color = totalMaliciosos > 0 ? 'red' : 'green';

      vt_html = `
        <p><b style="color:${color};">🔍 VirusTotal:</b></p>
        <ul>
          <li><b>Maliciosos:</b> ${detecciones.malicious}</li>
          <li><b>Sospechosos:</b> ${detecciones.suspicious}</li>
          <li><b>No detectados:</b> ${detecciones.undetected}</li>
          <li><b>Inofensivos:</b> ${detecciones.harmless}</li>
        </ul>
      `;
    } else if (vt.estado === "no_encontrado" || vt.error) {
      vt_html = `
        <p style="color: gray;"><b>VirusTotal:</b> No encontrado o error (${vt.codigo_http || "sin código"})</p>
      `;
    }

    resultados.innerHTML += `
      <details>
        <summary><b>${item.archivo}</b> (${item.ext || 'sin extensión'})</summary>
        <p><b>Ruta:</b> ${item.ruta}</p>
        <p><b>Tamaño:</b> ${item.tamaño_bytes} bytes</p>
        <p><b>MD5:</b> ${item.md5}</p>
        <p><b>SHA1:</b> ${item.sha1}</p>
        <p><b>SHA256:</b> ${item.sha256}</p>
        <p><b>Creación:</b> ${item.fecha_creacion}</p>
        <p><b>Modificación:</b> ${item.fecha_modificacion}</p>
        <p><b>Acceso:</b> ${item.fecha_acceso}</p>
        <p><b>Oculto:</b> ${item.oculto}</p>
        <p><b>Sistema:</b> ${item.sistema}</p>
        <p><b>Solo lectura:</b> ${item.solo_lectura}</p>
        <p><b>Ejecutable:</b> ${item.es_ejecutable}</p>
        ${vt_html}
      </details>
    `;
  });
}

function reiniciarAnalisis() {
  document.getElementById('step1').classList.remove('oculto');
  document.getElementById('step2').classList.add('oculto');
  document.getElementById('step3').classList.add('oculto');
  document.getElementById('barraCarga').classList.add('oculto');
  document.getElementById('progreso').style.width = '0%';
  document.getElementById('resultados').classList.add('oculto');
  document.getElementById('resultados').innerHTML = "";
  document.getElementById('jsonFile').value = null;
}
