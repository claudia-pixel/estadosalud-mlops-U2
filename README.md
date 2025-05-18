
# 🩺 Sistema de Diagnóstico Simple con Flask y Docker

Esta aplicación web, desarrollada con **Flask**, permite realizar un diagnóstico básico de salud ingresando tres signos vitales: temperatura corporal, frecuencia cardíaca y saturación de oxígeno. El sistema no solo provee un diagnóstico instantáneo, sino que también ofrece un reporte de las predicciones almacenadas. Está configurado para un flujo de trabajo **CI/CD** robusto utilizando **GitHub Actions** y **Docker**.

---

## 🚀 Funcionalidad

La aplicación consta de dos funcionalidades principales:

### 1. Diagnóstico Interactivo

A través de una interfaz web simple, los usuarios pueden ingresar sus signos vitales:

- Temperatura corporal  
- Latidos por minuto  
- Saturación de oxígeno  

El sistema devuelve uno de los siguientes diagnósticos:

- `NO ENFERMO`
- `ENFERMO LEVE`
- `ENFERMEDAD AGUDA`
- `ENFERMEDAD CRÓNICA`
- `ENFERMEDAD TERMINAL`
- `Valores fuera de rango, consulte a un médico.`

Cada diagnóstico realizado es registrado en un archivo de log llamado `diagnostics.log`.

### 2. Reporte de Diagnósticos

Ruta: `http://localhost:5000/report`

Incluye:

- El número total de cada tipo de diagnóstico
- Las **últimas 5 predicciones** realizadas
- La **fecha y hora de la última predicción**

---

## 📁 Estructura del Proyecto

```
.
├── .github/
│   └── workflows/
│       └── workflow.yaml         # Configuración de GitHub Actions para CI/CD
├── app.py                        # Lógica principal de la aplicación Flask
├── templates/
│   └── index.html                # Interfaz web del formulario de diagnóstico
├── tests/
│   ├── test_app_diag.py          # Pruebas para la lógica de diagnóstico
│   └── test_app_rep.py           # Pruebas para el reporte
├── Dockerfile                    # Define cómo construir la imagen Docker
├── README.md                     # Este documento
├── requirements.txt              # Dependencias de Python
└── diagnostics.log               # Log de diagnósticos generados
```

---

## ✅ Prerrequisitos

Antes de comenzar, asegúrate de tener instalado:

- [**Docker**](https://www.docker.com/get-started)  
- [**Python 3.9+**](https://www.python.org/downloads/)  
- [**pip**](https://pip.pypa.io/en/stable/installation/)  
- [**Git**](https://git-scm.com/downloads)  

---

## 🧪 Instrucciones para Ejecutar la Aplicación Localmente

### 1. Clonar el Repositorio

```bash
git clone https://github.com/tu_usuario/estadosalud-mlops-U2.git
cd estadosalud-mlops-U2
```

> Reemplaza `tu_usuario` y `estadosalud-mlops-U2` si tu repositorio tiene otro nombre.

---

### 2. Construir la Imagen de Docker

```bash
docker build -t sistema-diagnostico .
```

> `-t sistema-diagnostico`: Nombra la imagen  
> `.`: Usa el directorio actual como contexto de construcción

---

### 3. Ejecutar el Contenedor

```bash
docker run -p 5000:5000 sistema-diagnostico
```

- `-p 5000:5000`: Expone el puerto local  
- `sistema-diagnostico`: Imagen creada previamente

---

### 4. Acceder a la Aplicación

- Formulario de diagnóstico: [http://localhost:5000](http://localhost:5000)  
- Reporte: [http://localhost:5000/report](http://localhost:5000/report)

---

### 5. Detener el Contenedor

```bash
docker ps
docker stop <ID_DEL_CONTENEDOR>
```

> Reemplaza `<ID_DEL_CONTENEDOR>` con el ID que aparece en el primer comando.

---

## 🧪 Pruebas Unitarias

El proyecto incluye pruebas unitarias con `pytest`.

### Instalar Dependencias

```bash
pip install -r requirements.txt
pip install pytest
```

### Ejecutar Pruebas

```bash
pytest tests/
```

> Esto ejecutará todas las pruebas dentro de la carpeta `tests`.

---

## 🔁 CI/CD con GitHub Actions

El flujo de trabajo (`.github/workflows/workflow.yaml`) está configurado para dos eventos:

### 🔀 Pull Requests a la rama `main`

- Ejecuta el job `pruebas`
- Instala dependencias y corre pruebas
- Comenta el estado de las pruebas en el PR

### 💾 Commits (Push) a la rama `main`

- Ejecuta `pruebas`  
- Si pasa, ejecuta `pruebas_y_publicacion` que:
  - Autentica con GitHub Packages
  - Construye la imagen Docker
  - Publica la imagen en GitHub Packages como `latest`

### 📦 Imagen Docker Publicada

Consulta tu imagen en la sección **"Packages"** del repositorio:  
`ghcr.io/tu_usuario/tu_repositorio:latest`

---

## 🤝 Contribuciones

¡Contribuciones bienvenidas! Para colaborar:

```bash
# Hacer fork
git checkout -b feature/nueva-funcionalidad
# Realiza tus cambios
git commit -m 'feat: Añadir nueva funcionalidad X'
git push origin feature/nueva-funcionalidad
```

Luego abre un Pull Request a la rama `main`.

---

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT**. Consulta el archivo `LICENSE` para más detalles.
