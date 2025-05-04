# Sistema de Diagnóstico Simple con Flask y Docker

Esta aplicación web, desarrollada con **Flask**, permite realizar un diagnóstico básico ingresando tres signos vitales: temperatura corporal, frecuencia cardíaca y saturación de oxígeno. El sistema se ejecuta dentro de un contenedor **Docker** para facilitar su despliegue.

---

## Estructura del Proyecto

```
.
├── app.py
├── templates/
│   └── index.html
├── Dockerfile
├── README.md
└── requirements.txt
```

- `app.py`: Código principal de la aplicación Flask (rutas y lógica del diagnóstico).
- `templates/index.html`: Interfaz web con un formulario para ingresar los signos vitales.
- `Dockerfile`: Define cómo construir la imagen Docker para la aplicación.
- `requirements.txt`: Lista de dependencias de Python necesarias.
- `README.md`: Documento actual con información sobre el proyecto.

---

## Prerrequisitos

Antes de comenzar, asegúrate de tener instalado:

- [**Docker**](https://www.docker.com/get-started): Plataforma para contenerización de aplicaciones.

---

## Instrucciones para Ejecutar la Aplicación

### 1. Construir la Imagen de Docker

Abre una terminal y navega al directorio del proyecto. Luego ejecuta:

```bash
docker build -t sistema-diagnostico .
```

**Explicación del comando:**
- `docker build`: Inicia el proceso de construcción.
- `-t sistema-diagnostico`: Asigna el nombre `sistema-diagnostico` a la imagen.
- `.`: Usa el directorio actual como contexto de construcción.

---

### 2. Ejecutar el Contenedor

Inicia la aplicación en un contenedor con:

```bash
docker run -p 5000:5000 sistema-diagnostico
```

**Detalles:**
- `-p 5000:5000`: Mapea el puerto 5000 del contenedor al de tu máquina local.
- `sistema-diagnostico`: Imagen creada en el paso anterior.

---

### 3. Acceder a la Aplicación

Abre tu navegador y visita:

```
http://localhost:5000/
```

Deberías ver el formulario para ingresar los signos vitales.

---

### 4. Detener el Contenedor

Primero, obtén el ID del contenedor en ejecución:

```bash
docker ps
```

Luego detén el contenedor con:

```bash
docker stop <ID_DEL_CONTENEDOR>
```

Reemplaza `<ID_DEL_CONTENEDOR>` con el ID mostrado por el comando anterior.