# 🩺 Sistema de Diagnóstico Simple con Flask y Docker

Esta aplicación web, desarrollada con **Flask**, permite realizar un diagnóstico básico de salud ingresando tres signos vitales: temperatura corporal, frecuencia cardíaca y saturación de oxígeno. El sistema no solo provee un diagnóstico instantáneo, sino que también ofrece un reporte de las predicciones almacenadas y está configurado para un flujo de trabajo CI/CD robusto utilizando **GitHub Actions** y **Docker**.

---

## 🩺 Funcionalidad

La aplicación consta de dos funcionalidades principales:

1.  **Diagnóstico Interactivo**: A través de una interfaz web simple, los usuarios pueden ingresar sus signos vitales (temperatura, latidos por minuto, saturación de oxígeno). El sistema procesa estos valores y devuelve uno de los siguientes diagnósticos:
    * "NO ENFERMO"
    * "ENFERMO LEVE"
    * "ENFERMEDAD AGUDA"
    * "ENFERMEDAD CRÓNICA"
    * "ENFERMEDAD TERMINAL"
    * "Valores fuera de rango, consulte a un médico."

    Cada diagnóstico realizado es registrado en un archivo de log (`diagnostics.log`).

2.  **Reporte de Diagnósticos**: Una ruta dedicada (`/report`) permite visualizar un resumen de todos los diagnósticos registrados, incluyendo:
    * El número total de cada tipo de diagnóstico.
    * Las últimas 5 predicciones realizadas con sus detalles completos.
    * La fecha y hora de la última predicción.

---

## 🗂️ Estructura del Proyecto

```
.
├── .github/
│   └── workflows/
│       └── workflow.yaml       # Configuración de GitHub Actions para CI/CD
├── app.py                      # Lógica principal de la aplicación Flask y función de diagnóstico
├── templates/
│   ├── index.html              # Interfaz web para el formulario de diagnóstico
│   └── report.html             # Plantilla HTML para la página de reporte de diagnósticos
├── tests/
│   ├── test_app_diag.py        # Pruebas unitarias para la lógica de diagnóstico en app.py
│   └── test_app_rep.py         # Pruebas unitarias para la funcionalidad de reporte en app.py
├── Dockerfile                  # Define cómo construir la imagen Docker para la aplicación
├── README.md                   # Documento actual con información sobre el proyecto
└── requirements.txt            # Lista de dependencias de Python necesarias
```

---

## 🛠️ Prerrequisitos

Antes de comenzar, asegúrate de tener instalado:

- [**Docker**](https://www.docker.com/get-started)
- [**Python 3.9+**](https://www.python.org/downloads/)
- [**pip**](https://pip.pypa.io/en/stable/installation/)
- [**Git**](https://git-scm.com/downloads)

---

## 🚀 Instrucciones para Ejecutar la Aplicación Localmente

### 1. Clonar el Repositorio

```bash
git clone https://github.com/tu_usuario/estadosalud-mlops-U2.git
cd estadosalud-mlops-U2
```

(Reemplaza `tu_usuario` con tu nombre de usuario de GitHub si es diferente).

### 2. Construir la Imagen de Docker

```bash
docker build -t sistema-diagnostico .
```

Explicación:
- `docker build`: Inicia el proceso de construcción.
- `-t sistema-diagnostico`: Nombra la imagen.
- `.`: Usa el directorio actual como contexto.

### 3. Ejecutar el Contenedor

```bash
docker run -p 5000:5000 sistema-diagnostico
```

### 4. Acceder a la Aplicación

- Diagnóstico: [http://localhost:5000](http://localhost:5000)
- Reporte: [http://localhost:5000/report](http://localhost:5000/report)

### 5. Detener el Contenedor

```bash
docker ps
docker stop <ID_DEL_CONTENEDOR>
```

---

## 🧪 Pruebas Unitarias

Este proyecto incluye pruebas con `pytest`.

### Ejecutar Pruebas Localmente

```bash
pip install -r requirements.txt
pip install pytest
pytest tests/
```

---

## 🧰 Integración Continua / Despliegue Continuo (CI/CD) con GitHub Actions

### Pull Requests a la rama `main`:

- Se ejecuta el job `pruebas`.
- Se ejecutan pruebas unitarias y se comenta el resultado.

### Commits a la rama `main`:

- Se ejecuta `pruebas` y, si pasa, continúa con:
  - `pruebas_y_publicacion`: construye la imagen Docker y la publica en GitHub Packages.

### Imagen Docker Publicada

Puedes obtener la imagen más reciente directamente con:

```
docker pull ghcr.io/claudia-pixel/estadosalud-mlops:latest
```

---

## 🤝 Contribuciones

¡Contribuciones son bienvenidas!

1. Haz un fork.
2. Crea una rama (`feature/nueva-funcionalidad`).
3. Haz tus cambios y asegura que las pruebas pasen.
4. Haz push y abre un Pull Request.

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
