# Django REST Framework + Documentación + Pytest-django
----------------------------------------------
Creamos una REST API usando Django REST Framework. Mediante el protocolo HTTP usaremos los métodos GET, POST, PUT y DELETE con el formato JSON para enviar y recibir datos. 
Para ver la documentación de la API usaremos coreapi y usaremos para el testing pytest-django.
Te he dejado comentarios para que puedas comprender lo que estoy haciendo en cada línea del código. <br> 
<br>
![foto3](https://github.com/NikiDevelop/Django-rest-framework/assets/105102619/bd0ab78e-2687-4549-86a9-51b6043dbfce)

# Ejecutar proyecto
Primero, crear un entorno virtual:

```
$ python -m venv env
```
Tenemos que activar nuestro entorno virtual, tendremos que desplazarnos a la carpeta scripts.
```
.\env\scripts\activate
```
Ya tendríamos activado nuestro entorno virtual, debería salirte a la izquierda en color verde (env), eso quiere decir que está activado ya.

Ahora pasaremos a instalar las dependencias del proyecto.
```
$ pip install -r requirements.txt
```

Por último, ya solo te queda hacer las migraciones.
```
$ python manage.py makemigrations
```
```
$ python manage.py migarate
```
```
$ python manage.py runserver
```
Para poder agregar nuevos usuarios tendrás que crearte un super user. Rellena los datos que te pide, como nombre de usuario,
el email lo puedes dejar en blanco si quieres dándole a enter y por último introduce una contraseña y repítela.
También puedes acceder mediante la siguiente url `http://127.0.0.1:8000/api/User/` y crear uno nuevo en formato JSON.
```
$ python manage.py createsuperuser
```

# Instalar Rest Framework
```
$ pip install djangorestframework
```
Agregamos ```'rest_framework'``` en ```INSTALLED_APPS``` settings
```
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

#  Coreapi para documentar automáticamente
----------------------------------------------
Coreapi lo usaremos para ver la documentación que tiene la API. <br>
<br>
![foto1](https://github.com/NikiDevelop/Django-rest-framework/assets/105102619/7af0238e-aab0-4d94-8eae-39c4af1af81d)
Lo primero instalamos coreapi.
```
$ pip install coreapi
```
Agregamos ```'coreapi'``` en ```INSTALLED_APPS``` settings
```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'coreapi',
]
```
Agregamos el ```Auto Schema``` se puede agregar al final en settings o donde quieras.

```  
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}
```

Por último, nos vamos a ```urls.py``` del proyecto donde tenemos la configuración del proyecto.
Desde ```rest_framework``` vamos a importar ```include_docs_urls``` para ver la documentación de nuestra API que accederemos por la url ```docs/```.
Agregamos el nuevo ```path()```

```
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='api Documentation')),
]


```
#  Pytest-django para hacer testing de nuestra API
----------------------------------------------
Lo primero instalamos pytest-django.
```
$ pip install pytest-django
```
Creamos un archivo ```pytest.ini``` a la altura de nuestro proyecto.
Nos quedaría así: 
- api
- proyecto
- pytest.ini <br>
Dentro de ```pytest.ini``` le pasamos settings y los posibles nombres que puede tener nuestro test. En mi caso core se llama mi proyecto donde tengo la configuración.
```
[pytest]

DJANGO_SETTINGS_MODULE = core.settings

python_files = tests.py test_*.py *_test.py
```
Creamos una carpeta que la llamaremos ```test``` a la altura de nuestro proyecto, nos quedaría así:
- api
- proyecto
- pytest.ini 
- test <br>
Dentro de la carpeta creamos un archivo ```test_user.py``` <br>
Comprobamos si se crea un usuario y si tiene el mismo nombre que le pasamos.
```
import pytest
from api.models import User

@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create(
        name='Lucia',
        nickName='Luci30',
        age=30,
        is_active=True
    )
    assert user.name == 'Lucia'

```
Para ejecutar nuestro test solo tienes que escribir ```pytest``` en la terminal.
Si está todo bien tendría que decirte ```passed``` en color verde.
