# Vermillion Player - Panel de administración

Panel de administración para gestionar contenidos de Vermillion Player. 

## Tecnologías del proyecto

1. Django: template del panel Jazzmin.
2. PostgresSQL (pendiente - De momento utiliza SQLite)
3. Graphql
4. Autenticación JWT
5. Docker (pendiente)
6. Pytest (pendiente)

## ¿Que contenido gestiona este proyecto?

- Canales (crea canales personalizados para emitir diferente tipos de contenido)
- Programas (crea programas para emitirlos en diferentes canales)
- Temporadas (asocia estas temporadas a sus programas)
- Episodios (crea episodios vinculados a sus canales)
- Películas (crea películas para emitir)
- Videojuegos (proximamente)

NOTA: El contenido multimedia se guarda en un CDN y se asocia al contenido relacionado buscando por carpeta desde el panel (pendiente)


## Despliegue del proyecto (sin contenedores)

Para trabajar sin contenedores el proyecto hacemos lo siguiente en linux o utilizando la shell de Git:

1. Clonar o descargar proyecto en tu máquina: ``git clone https://github.com/Vermillion-Player/admin_panel.git``
2. Crear entorno virtual: ``python -m venv .env``
3. Arrancar entorno virtual: ``source .env/bin/activate``
4. Instalar dependencias: ``pip install -r requirements.txt``
5. Crear migraciones: ``python manage.py makemigrations``
6. Lanzar migraciones: ``python manage.py migrate``
7. Crear usuario admin: ``python manage.py createsuperuser``
8. Arrancar servidor: ``python manage.py runserver``

## Rutas de acceso

1. Panel: ``localhost:8000/admin``
2. Graphql: ``localhost:8000/graphql``
