# Sistema de Gestión de Usuarios y Vehículos

Este proyecto es un sistema de gestión de usuarios y vehículos desarrollado como parte de un trabajo práctico para CoderHouse.

## Descripción

El sistema permite a los usuarios registrarse, iniciar sesión, crear, buscar vehículos y editarlos; así como también ver la lista de usuarios registrados. Proporciona una interfaz fácil de usar para la administración de datos y la interacción con la base de datos.

## Características Principales

- Registro de Usuarios: Los usuarios pueden registrarse proporcionando su nombre, apellido, edad y contraseña.
- Inicio de Sesión: Los usuarios pueden iniciar sesión con su nombre de usuario y contraseña.
- Creación de Vehículos: Los usuarios pueden crear vehículos proporcionando la marca, modelo, tipo de combustible y año de fabricación.
- Búsqueda de Vehículos: Los usuarios pueden buscar vehículos por marca, modelo o año de fabricación.
- Edición de Perfil: Los usuarios pueden editar su perfil y agregar un avatar.
- Sistema de Mensajería: Los usuarios pueden enviar y recibir mensajes dentro del sistema.

## Instalación

### 1. Clona el repositorio en tu máquina local:

```sh
$ git clone https://github.com/fedesosa4848/Tercera-Pre-Entrega-Sosa-Federico.git
```
```sh
$ cd Tercera-Pre-Entrega-Sosa-Federico
```
```sh
$ git fetch -a
```
```sh
$ git checkout develop
```

### 2.Crea un entorno virtual e instala las dependencias:

```sh
$ python -m venv venv
```
```sh
$ source venv/bin/activate  # Linux/macOS
```
```sh
$ venv\Scripts\activate     # Windows
```
```sh
$ pip install -r requirements.txt
```

### 3. Ejecuta las migraciones de la base de datos:

```sh
$ python manage.py migrate
```

### 4. Inicia el servidor de desarrollo:

```sh
$ python manage.py runserver
```

### 5. Accede al sistema 
```sh
desde tu navegador web en la dirección http://127.0.0.1:8000/.
```

## Contribución
Las contribuciones son bienvenidas. Si deseas contribuir al proyecto, sigue estos pasos:

1. Haz un 'Fork' del proyecto.
2. Crea tu rama de características (`git checkout -b feature/AmazingFeature`).
3. Realiza tus cambios y haz un 'commit' (`git commit -m 'Add some AmazingFeature'`).
4. Sube tu rama (`git push origin feature/AmazingFeature`).
5. Abre un 'Pull Request'.


## Tecnologías Utilizadas

1. Django: Framework de desarrollo web en Python.
2. HTML/CSS: Lenguajes de marcado y estilos para la interfaz de usuario.
3. JavaScript: Lenguaje de programación para la interactividad en el frontend.
4. Bootstrap: Framework CSS para el diseño y la maquetación de páginas web.








