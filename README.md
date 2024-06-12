# Sistema de Gestión de Usuarios y Vehículos

Este proyecto es un sistema de gestión de usuarios y vehículos desarrollado como parte de un trabajo práctico para la asignatura de Desarrollo de Aplicaciones Web.

## Descripción

El sistema permite a los usuarios registrarse, iniciar sesión, crear y buscar vehículos, así como también ver la lista de usuarios registrados. Proporciona una interfaz fácil de usar para la administración de datos y la interacción con la base de datos.

## Características Principales

- Registro de Usuarios: Los usuarios pueden registrarse proporcionando su nombre, apellido, edad y contraseña.
- Inicio de Sesión: Los usuarios pueden iniciar sesión con su nombre de usuario y contraseña.
- Creación de Vehículos: Los usuarios pueden crear vehículos proporcionando la marca, modelo, tipo de combustible y año de fabricación.
- Búsqueda de Vehículos: Los usuarios pueden buscar vehículos por marca, modelo o año de fabricación.
- Ver Usuarios: Los administradores pueden ver la lista de usuarios registrados en el sistema.

## Instalación

1. Clona el repositorio en tu máquina local:

```bash
git clone https://github.com/tu_usuario/tu_proyecto.git
Accede al directorio del proyecto:
bash
Copiar código
cd tu_proyecto
Crea un entorno virtual e instala las dependencias:
bash
Copiar código
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
Ejecuta las migraciones de la base de datos:
bash
Copiar código
python manage.py migrate
Inicia el servidor de desarrollo:
bash
Copiar código
python manage.py runserver
Accede al sistema desde tu navegador web en la dirección http://localhost:8000.
Contribución
Las contribuciones son bienvenidas. Si deseas contribuir al proyecto, sigue estos pasos:

Haz un 'Fork' del proyecto.
Crea una rama de características (git checkout -b feature/nueva_caracteristica).
Realiza tus cambios y haz un 'commit' (git commit -m 'Agrega nueva característica').
Sube tu rama (git push origin feature/nueva_caracteristica).
Abre un 'Pull Request' en GitHub.
Tecnologías Utilizadas
Django: Framework de desarrollo web en Python.
HTML/CSS: Lenguajes de marcado y estilos para la interfaz de usuario.
JavaScript: Lenguaje de programación para la interactividad en el frontend.
Bootstrap: Framework CSS para el diseño y la maquetación de páginas web.
Copiar código

¡Espero que te sea útil!







