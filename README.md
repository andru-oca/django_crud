Steps para Django
---

Que es Django? 

[DJANGO WEB SITE](https://www.djangoproject.com/)

- Es un framework, todo incluido.
- Servidores de Paginas estaticas, lo tiene!
- Seguridad? Lo tiene
- Templates? Lo tiene y usa uno de los mejorcitos templates engines : Jinja
- ORM? Lo tiene incluido
- Bases de datos? Podes usar el que viene por defecto en Dev, que es sqlite y despues migrar al recomendado que es PostgreSQL
- Puedo hacer una API? Se puede usando una herramienta(pack) llamado RestFramework con Serializadores incluidos


Para entender en primera instancia que hacer con Django, debo tener la version instalada en una VENV

Procesos Básicos para DJANGO
--- 

Entender lo que es un entorno virtual en python. 
Ejemplos de los mismos son virtualenv.

Entender lo que es pip >> es un modulo que me permite instalar paquetes de información 

para instalar pip si no se llega a tener: [PIP INSTALLER](https://programwithus.com/learn/python/pip-virtualenv-windows)

```
pip install django
```


* Generar primeras vistas
* Rutas
* Templates

Primera Clase Introduccion a Django
    Crear una Primera Plantilla y mostrarlo
    Proyecto de clase, una pagina organizadora de tareas

Arrancando proyecto: En este caso vamos a crear ese proyecto en la misma carpeta y la vamos a llamar crud_tareas.
init

```
django-admin startproject crud_tareas
```


miremos lo que tenemos en ese archivo

* manage.py => el corazon de django, es el que realiza muchos movimientos y tambien para correr el framework

- crud_tareas 
    Será el proyecto en sí, donde se alojaran varias instancias para poder mirar y asignar settings
    los paths 
    asgi y wsgi: web server gateway interface => 
    https://medium.com/@nachoad/que-es-wsgi-be7359c6e001
    una marca muy comun y de alto uso es gunicorn, que nos permite servir request y response de los elementos dinámicos (codigo python)
    asgi => Asynchronous Server GateWay Interface
    Es similar a la anterior pero te permite peticiones async, lo cual es genial para cuando tenés procesos que no deban ser "bloqueantes"
    https://asgi.readthedocs.io/en/latest/


- settings
    Por default Django tiene Sqlite, que es lo mismo que un SQL local pero en menor instancia
    
    Como buenas practias es excelente colocar la carpeta de Templates en el proyecto root.

```
/*python manage.py collectstatic*/
```

[Data extra](https://books.agiliq.com/projects/django-orm-cookbook/en/latest/table_name.html)

# PRIMERA PARTE DE django


PRIMERO CONOCER EL ENTORNO 
- REQUIREMENTS.txt

    **pip freeze > requirements.txt**

    | para usar esos paquetes:

    **pip install -r requirements.txt**

- CREAR UN ENTORNO VIRTUAL:

    **virtualenv venv**
    
    -En windows : _venv\Scripts\activate | venv\Scripts\deactivate.bat_

    -Linux || MAC  : _source venv/bin/activate | source venv/bin/deactivate_

- CREAR UN PROYECTO

    - django-admin startproject <nombre_proyecto>

    Levantar el servicio utilizando el runserver

        - python manage.py runserver | <PORT=8000>

- CREAR UN PAGINA DE INICIO
    
- METHODS RENDER , CONTEXTO, JINJA

- CREAR UNA PAGINA USANDO STATIC FILES

    [DOCUMENTACION STATICFILES](https://docs.djangoproject.com/en/4.1/howto/static-files/)


# SEGUNDA PARTE


- CREAR UNA APP
- FORMS (GET|POST|DELETE|UPDATE)
- CONECTAR A UNA BASE DE DATOS
    * RECOMENDACION SIEMPRE USAR UN .env file, por razones de seguridad.
    * CONECTAR A MYSQL :: LOCAL 
        
        [REFERENCIA MYSQL](https://www.geeksforgeeks.org/how-to-integrate-mysql-database-with-django/)

        _pip install mysqlclient_

        ```
        DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.mysql',
                        'NAME': ‘<database_name>’,
                        'USER': '<database_username>',
                        'PASSWORD': '<password>',
                        'HOST': '<database_hostname_or_ip>',
                        'PORT': '<database_port>',
                    }
                }
        ```

    * CONECTAR A POSTGRESQL :: USANDO RENDER

        [REFERENCIA POSTGRESQL](https://hevodata.com/learn/django-postgresql/)

        _pip install psycopg2_

        ```
        DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.postgresql',
                        'NAME': ‘<database_name>’,
                        'USER': '<database_username>',
                        'PASSWORD': '<password>',
                        'HOST': '<database_hostname_or_ip>',
                        'PORT': '<database_port>',
                        }
        }
        ```

- CREAR UN CRUD CON UNA TODO LIST


# TERCERA PARTE DJANGO

- [TUTORIAL DE DEPLOY](https://tutorial.djangogirls.org/es/)
- [DJANGO DEPLOY VIDEO](https://www.youtube.com/watch?v=FvsvjqOAOVg)
- HACER UN DEPLOY (IDEALMENTE ESPERAMOS)
- [DEPLOY ON RENDER](https://render.com/docs/deploy-django#deploy-to-render)
- [PYTHONANYWHERE](https://www.youtube.com/watch?v=FvsvjqOAOVg)


# CUARTA PARTE
- [media upload to profile](https://www.youtube.com/watch?v=aNk2CAkHvlE&t=924s)
- [EXTRA](https://testdriven.io/blog/django-static-files/)
- 


DJANGO
--- 

CREAR CRUD 

- crear una app 
    * django-admin startapp todo_list:

    * se debe generar el modelo para poder utilizarlo 
        models.Model
    * esta es una app que necesitamos registrar en la parte de admin
        admin.site.register(<modelo_creado>)

    * se debe setear en settings del proyecto 
        INSTALLED_APPS --> agregar la app creada

    * para visualizar el modelo es necesario hacer una migracion
        python manage.py makemigrations
        python manage.py migrate

    * vemos las configuraciones()
        Con esto seteado podemos empezar a trabajar los forms y el crud
        previo a esto me voy a saltar un paso para poder demostrar la sencillez con la
        que se puede generar una api con una libreria llamada restframework

        GOTO=> CREAR API REST



* crear un modelo

- generacion por medio de funciones

* Crear un formulario
    usando el concepto de modelForm

* Generar las views y los paths respectivos para realizar el crud respectivo



CREAR API REST
    pip install djangorestframework (django)
        posterior debemos iniciar los proyectos respectivos


    settings:
        - necesitamos instalar en los
        INSTALLED_APPS --agregar: rest_framework
    crear serializer
        pasos en la app.
        -   crear archivo serializer
        -   crear un viewsets (este me permite tener una vista para mirar de manera gráfica mi api).
            - PARA ESTE CASO ES IMPORTANTE CONTAR CON EL MODELO Y EL SERIALIZER
        -   crear un urls.py>> | caso particular prefiero llamar a un modulo router e importarlo| 
            * donde generaremos rutas donde se pueda generar los endpoints(o rutas por medio de un router) 

        -   crear un path en urls del project

        luego de incluir el api

```      
    path('api/', include('todo_list.urls'))
```

        empezamos a correr la api

DEPLOY

Es importante tenerlo en el main de tu repo GITHUB
usaremos PYTHONANYWHERE

importante no tener el venv
mejor tener el requirements


* Clonado de repo en el bash
* generar un venv 
    - python -m venv .virtualenvs/code
    - levantamos el venv
        - source ~/.virtualenvs/code/bin/activate
        - pip install -r requirements.txt


* WebApps
    - realizar una manual deploy
    <usuario>.pythonanywhere.com. 
    -  CODE : la ruta de la app
    - static_files
    - adicionales [EXTRA STATICS](https://stackoverflow.com/questions/25375448/django-rest-framework-missing-static-directory)
    - python manage.py collectstatic


DEPLOY REALIZADO: 
    [DEPLOY](ander1987.pythonanywhere.com)