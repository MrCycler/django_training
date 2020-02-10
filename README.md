# APP EJEMPLO EN PYTHON

<hr />

## ARQUITECTURA:
    - Backend: DJANGO

<hr />

## CONFIGURACIÓN PARA INSTALAR Y CORRER EL PROYECTO
- ###  install python 3
`sudo apt-get install python3-pip`
- ###  install venv
`sudo pip3 install virtualenv` 
- ### create a virtual environment
`virtualenv platzigram_env`
- ### activate venv
`source platzigram_env/bin/activate`
- ### (C) to deactivate
`deactivate`
- ### install requeriments 
`pip install -r requirements.txt`
- ### run the app in the ROOT FOLDER
`python manage.py runserver`

<hr />

## COMANDOS EN PYTHON UTILES
- ### para listar las librerias instaladas en el entorno virtual
`pip freeze`
- ### para listar las librerias instaladas en el entorno virtual
`pip freeze > requirements.txt`

<hr />

## COMANDOS DE GESTION CON DJANGO
- ### para iniciar un nuevo proyecto en django
`django-admin startproject platzigram`
- ### para correr el servidor
`python manage.py runserver`
- ### para iniciar una nueva app dentro del proyecto en django
`python manage.py startapp posts`
- ### para procesar las migraciones
`python manage.py makemigrations`
- ### para aplicar migraciones
`python manage.py migrate`
`python manage.py migrate --run-syncdb`
- ### abrir la consola interactiva de python
`python manage.py shell`
- ### crear superusuario
`python manage.py createsuperuser`

<hr />

## COMANDOS PARA INSTANCIAR MODELOS

- ### importar el modelo del paquete
`from posts.models import User`
- ### para crear una instancia
`pablo = User.objects.create(email='hola@gmail.com',password='1234567',first_name='Pablo',last_name='Trinidad')`
- ### otra forma de crear la instancia
`pablo = User()`
`pablo.email='hola@gmail.com'`
`pablo.password='1234567'`
`pablo.first_name='Pablo'`
`pablo.last_name='Trinidad'`
`pablo.is_admin= True`
`pablo.save()`
- ### leer un dato de la instancia
`pablo.email`
- ### actualizar un dato de la instancia
`pablo.email = 'aea@gmail.com'`
`pablo.save()`
- ### para borrar una instancia
`pablo.delete()`
- ### busqueda de una instancia - solo devuelve una instancia
`user = User.objects.get(email='hola@gmail.com')`
- ### busqueda de varias instancias
`platzi_users = User.objects.filter(email__endswith='@gmail.com')`
- ### obtiene todas las instancias
`users = User.objects.all()`
- ### actualizacion de varias instancias
`platzi_users = User.objects.filter(email__endswith='@gmail.com').update(is_admin=True)`

<hr />

## VERSIONES DE ESTA APLICACION
- v1.0.0: aplicacion por defecto (Archivos por defecto)
- v1.1.0: api simple para ordernar numeros y restringir por edad
- v1.2.0: app para mostrar posts
- v1.3.0: app para mostrar posts con un template
- v1.4.0: modelo user creado
- v1.4.1: teoría agregada en readme y otros archivos
- v1.5.0: modelo profile creado basado en user y añadida la plantilla para su gestión en el admin
- v1.6.0: se puede crear profile en la misma pantalla en que se crea usuario
- v1.7.0: creado el modelo post que usa user y profile
- v1.8.0: se crea carpeta para almacenar las imagenes y asignarles urls
- v1.9.0: templates y archivos estáticos
- v10.0.0: se crean templates y vistas para el logeo


