# 🔍 Consulta de IP con Django


<p align="center">
  <img src="https://res.cloudinary.com/dry8bdxce/image/upload/v1748924393/principal_rdj07l.png" width="45%" alt="Captura 1" />
</p>
<p align="center">
  <em>Captura de pantalla Consultar IP</em>
</p>

<p align="center">
  <img src="https://res.cloudinary.com/dry8bdxce/image/upload/v1748924393/resultados_k4dwi1.png" width="45%" alt="Captura 2" />
</p>
<p align="center">
  <em>Captura de pantalla Resultado(s) Obtenido(s)</em>
</p>

---

## 📝 Descripción 

Este proyecto es una aplicación web desarrollada con **Django** que permite a los usuarios ingresar una dirección IP y obtener información detallada utilizando la API de [ipwhois.io](https://ipwhois.io/). La aplicación consulta datos como ubicación, país, ciudad, proveedor de internet (ISP), tipo de conexión, y más.

---

## 🎯 Características principales

- Ingreso manual de direcciones IP.
- Consulta en tiempo real usando la API pública de ipwhois.io.
- Visualización clara y estructurada de los datos obtenidos.
- Descarga de la información en un archivo CSV.
- Interfaz sencilla y responsive.

---

## 🗂️ Tecnologías utilizadas

- **Django** (framework backend)
- **HTML / CSS / Bootstrap** (frontend básico)
- **API REST** con `requests` (consumo desde el backend)
- **Python 3**

---

## 📥 Instalación y configuración

1️⃣ Clona el repositorio:

   - git clone https://github.com/larzdz/IPLookUp.git
   - cd IPLookUp
   
2️⃣ Crea y activa un entorno virtual:
   - En Linux / macOS:
     - python3 -m venv env
     - source env/bin/activate
    
   - En Windows:
     - python -m venv env
     - env\Scripts\activate
 
3️⃣ Instala las dependencias

   - pip install -r requirements.txt

4️⃣ Corre el servidor local

   - python manage.py runserver

5️⃣ Abre tu navegador y visita

   - http://localhost:8000/

---

## 🚀 Uso
- Ingresa las direcciones IPs válidas en el formulario.

- Consulta la información detallada que se mostrará en pantalla.

- Descarga la información en formato CSV si lo deseas.

---

## 📄 Licencia
Este proyecto es de uso personal y educativo.
