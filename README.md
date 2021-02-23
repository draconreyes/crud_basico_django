Lo primero que se tiene que hacer cuando ya se clono el proyecto es crear el entorno virtual para esto nos pararemos en el proyecto con la consola y crearemos el entorno virtual
con los siguientes comandos.
```
python -m venv venv
venv\Scripts\activate.bat (en windows)
source venv/bin/activate(linux)
```


Despues de esto se tendra que installar todas las dependencias que se encuentran en el archivo requirements.txt para eso tendremos que posicionarnos en la ruta del proyecto
crud_basico_django\sap  y ejecuntamos el siguiente comando en la consola.
```
pip install -r requirements.txt
```


Cuando se instalen las dependencias se tiene que configurar el archivo sap/sap/settings.py en linea 85 DATABASES
ya esta configurado ENGINE para trabajar con postgrest solo es necesario que creen la base de datos y den los
valores como NAME (Nombre de la base de datos), USER (Nombre de usuario de postgres) , PASSWORD (Contraseña del usuario de postgres con el que ingresaras)
HOST (nombre del host donde esta la base de datos) y PORT (Puerto de la base de datos)

El siguiente ejemplo es la configuracion que tengo localmente en mi maquina.
        
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sap_db',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '5433',
        
Despues de eso nos dirigimos prueba crud_basic_django\sap y entramos en la terminal aqui ejecutamos el comando
```
python manage.py makemigrations
```
pare crear las migraciones y luego 
```
python manage.py migrate 
```
para ejecutar todas las migraciones de la base de datos y por ultimo corremos el servidor con el comando 
```
python manage.py runserver
```

La aplicacion es un pequeño CRUD para administrar la informacion del personal.
