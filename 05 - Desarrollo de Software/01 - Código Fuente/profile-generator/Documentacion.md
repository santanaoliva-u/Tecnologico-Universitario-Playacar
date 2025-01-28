

### Estructura del Proyecto

```plaintext
instagram-profile-generator/
│
├── app/
│   ├── __init__.py
│   ├── profile_generator.py
│   ├── api_clients.py
│   ├── proxy_manager.py
│   ├── app_config.py
│   ├── form_filler.py
│   ├── session_manager.py
│   ├── utils.py
│   ├── logger.py
│   └── database.py
│
├── requirements.txt
├── main.py
└── README.md
```

---

### 1. **`app_config.py`** - Configuración General

```python
# app/app_config.py

import os

# API Keys
FAKER_API_KEY = os.getenv('FAKER_API_KEY', 'your_faker_api_key')
UNSPLASH_API_KEY = os.getenv('UNSPLASH_API_KEY', 'your_unsplash_api_key')

# Proxy settings
PROXY_LIST = [
    'http://proxy1:port',
    'http://proxy2:port',
    'http://proxy3:port'
]

# General settings
MAX_RETRIES = 3  # Max retries for failed requests
TIMEOUT = 10  # Timeout for requests
```

---

### 2. **`proxy_manager.py`** - Manejo de Proxies

```python
# app/proxy_manager.py

import random
import requests

class ProxyManager:
    def __init__(self, proxy_list):
        self.proxy_list = proxy_list
    
    def get_random_proxy(self):
        return random.choice(self.proxy_list)
    
    def make_request(self, url, params=None, headers=None):
        proxy = self.get_random_proxy()
        proxies = {
            "http": proxy,
            "https": proxy
        }
        try:
            response = requests.get(url, params=params, headers=headers, proxies=proxies, timeout=10)
            response.raise_for_status()  # Raise exception for bad responses
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error using proxy {proxy}: {e}")
            return None
```

---

### 3. **`api_clients.py`** - Clientes para APIs Externas

```python
# app/api_clients.py

import requests
from app.app_config import UNSPLASH_API_KEY, FAKER_API_KEY

# Generate random photo using Unsplash API
def get_random_photo():
    url = "https://api.unsplash.com/photos/random"
    headers = {
        "Authorization": f"Client-ID {UNSPLASH_API_KEY}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()[0]['urls']['small']
    return None

# Generate random name using Faker API
def get_random_name():
    url = f"https://fakerapi.it/api/v1/persons?quantity=1&seed={FAKER_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['data'][0]['name']['first'] + " " + response.json()['data'][0]['name']['last']
    return None
```

---

### 4. **`form_filler.py`** - Llenado Automático de Formularios

```python
# app/form_filler.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class FormFiller:
    def __init__(self, url, proxy=None):
        self.url = url
        self.proxy = proxy
        self.driver = None

    def start_browser(self):
        options = webdriver.ChromeOptions()
        
        # Use proxy if available
        if self.proxy:
            options.add_argument(f'--proxy-server={self.proxy}')
        
        # Open the browser and load the URL
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.url)

    def fill_form(self, profile):
        try:
            # Locate form fields
            name_field = self.driver.find_element(By.NAME, "name")
            email_field = self.driver.find_element(By.NAME, "email")
            phone_field = self.driver.find_element(By.NAME, "phone")
            dob_field = self.driver.find_element(By.NAME, "birth_date")
            photo_field = self.driver.find_element(By.NAME, "photo")

            # Fill form with random profile data
            name_field.send_keys(profile['name'])
            email_field.send_keys(profile['email'])
            phone_field.send_keys(profile['phone'])
            dob_field.send_keys(profile['birth_date'])
            photo_field.send_keys(profile['photo'])

            # Submit the form
            submit_button = self.driver.find_element(By.NAME, "submit")
            submit_button.click()

            print("Formulario enviado exitosamente.")
        except Exception as e:
            print(f"Error al llenar el formulario: {e}")

    def stop_browser(self):
        time.sleep(5)  # Wait for results
        self.driver.quit()
```

---

### 5. **`session_manager.py`** - Manejo de Sesiones

```python
# app/session_manager.py

import requests

class SessionManager:
    def __init__(self):
        self.session = requests.Session()

    def login(self, login_url, credentials):
        try:
            response = self.session.post(login_url, data=credentials)
            response.raise_for_status()
            print("Login exitoso.")
        except requests.exceptions.RequestException as e:
            print(f"Error al hacer login: {e}")

    def post_data(self, url, data):
        try:
            response = self.session.post(url, data=data)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error al enviar datos: {e}")
            return None
```

---

### 6. **`profile_generator.py`** - Generación de Perfiles

```python
# app/profile_generator.py

from app.api_clients import get_random_name, get_random_photo
import random

class ProfileGenerator:
    def __init__(self, proxy_manager):
        self.proxy_manager = proxy_manager
    
    def generate_profile(self):
        name = get_random_name()
        photo = get_random_photo()
        email = self.generate_random_email()
        phone = self.generate_random_phone()
        birth_date = self.generate_random_date()

        profile = {
            "name": name,
            "photo": photo,
            "email": email,
            "phone": phone,
            "birth_date": birth_date
        }

        return profile
    
    def generate_random_email(self):
        return f"{random.randint(1000, 9999)}@example.com"
    
    def generate_random_phone(self):
        return f"+1{random.randint(1000000000, 9999999999)}"
    
    def generate_random_date(self):
        return f"{random.randint(1, 31)}-0{random.randint(1, 9)}-199{random.randint(0, 9)}"
```

---

### 7. **`logger.py`** - Configuración de Logs

```python
# app/logger.py

import logging

def setup_logger():
    logger = logging.getLogger('ProfileGeneratorLogger')
    handler = logging.FileHandler('app.log')
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = setup_logger()
```

---

### 8. **`database.py`** - Manejo de Base de Datos (Opcional)

```python
# app/database.py

import sqlite3

def create_db():
    conn = sqlite3.connect('profiles.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            photo TEXT,
            email TEXT,
            phone TEXT,
            birth_date TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_profile(profile):
    conn = sqlite3.connect('profiles.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO profiles (name, photo, email, phone, birth_date) 
        VALUES (?, ?, ?, ?, ?)
    ''', (profile['name'], profile['photo'], profile['email'], profile['phone'], profile['birth_date']))
    conn.commit()
    conn.close()
```

---

### 9. **`main.py`** - Aplicación Principal

```python
# main.py

from app.profile_generator import ProfileGenerator
from app.proxy_manager import ProxyManager
from app.form_filler import FormFiller
from app.session_manager import SessionManager
from app.logger import logger

def main():
    url = input("Introduce la URL para crear el perfil: ")
    proxy_manager = ProxyManager(proxy_list=["http://proxy1:port", "http://proxy2:port"])
    session_manager = SessionManager()
    
    # Iniciar sesión si es necesario
    login_url = input("Introduce la URL de login (si es necesario): ")
    credentials = {"username": "your_username", "password": "your_password"}
    session_manager.login(login_url, credentials)
    
    # Configuración del generador de perfiles
    profile_generator = ProfileGenerator(proxy_manager)
    profile = profile_generator.generate_profile()
    
    # Llenar el formulario con los datos generados
    form_filler = FormFiller(url, proxy=proxy_manager.get_random_proxy())
    form_filler.start_browser()
    form_filler.fill_form(profile)
    form_filler.stop_browser()

    logger.info(f"Perfil generado y enviado a {url}.")
    print("Perfil generado con éxito.")

if __name__ == "__main__":
    main()
```

---

### 10. **`requirements

.txt`**

```txt
requests
selenium
```

---

### 11. **`README.md`** - Guía de Usuario


# Instagram Profile Generator

Una herramienta automatizada para generar y enviar perfiles a una URL dada.

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/instagram-profile-generator.git
    cd instagram-profile-generator
    ```

2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

3. Descarga el [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) para Selenium y colócalo en tu PATH.

## Uso

1. Ejecuta el script principal:
    ```bash
    python main.py
    ```

2. Introduce la URL donde quieres crear el perfil.

3. La aplicación generará automáticamente un perfil y lo enviará al formulario de la página.

## Contribuciones

1. Abre un *Issue* o un *Pull Request* si deseas realizar cambios o mejoras.


---

### Conclusión

Esta aplicación está estructurada de manera modular, lo que facilita futuras modificaciones o mejoras. Puedes expandirla fácilmente para soportar más funcionalidades, como integración con bases de datos o la creación de perfiles más complejos. También incluye un sistema de logs, manejo de proxies y sesiones, y automatiza el llenado de formularios en cualquier URL.

# Docker
Para instalar y ejecutar tu aplicación en Docker, primero necesitas crear un contenedor que contenga todos los requisitos necesarios para que tu aplicación funcione correctamente. Aquí están los pasos detallados para hacerlo.

### 1. **Preparar los Archivos de la Aplicación**

Asegúrate de que tu aplicación esté completa con todos los archivos que mencionamos antes (como `main.py`, `requirements.txt`, etc.).

### 2. **Crear un Dockerfile**

El `Dockerfile` es un archivo de configuración que indica cómo se construye el contenedor para tu aplicación. Debes crear este archivo en la raíz de tu proyecto (en el mismo directorio donde están los archivos de tu aplicación).

Aquí tienes un ejemplo de `Dockerfile` que puedes usar:

```Dockerfile
# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos y la aplicación
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código de la aplicación al contenedor
COPY . .

# Expone el puerto (si tu aplicación usa uno, si no puedes omitirlo)
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]
```

### 3. **Crear el archivo `requirements.txt`**

En tu archivo `requirements.txt`, asegúrate de que están las bibliotecas necesarias. Aquí tienes un ejemplo de cómo debe verse:

```txt
requests
selenium
```

### 4. **Construir la Imagen Docker**

En tu terminal, navega al directorio donde se encuentran tu `Dockerfile` y la aplicación. Luego, ejecuta el siguiente comando para construir la imagen de Docker:

```bash
docker build -t profile-generator .
```

Este comando creará una imagen de Docker llamada `instagram-profile-generator` con todos los archivos necesarios y las dependencias instaladas.

### 5. **Ejecutar el Contenedor Docker**

Una vez que la imagen ha sido construida correctamente, puedes ejecutar un contenedor con esta imagen. Usa el siguiente comando:

```bash
docker run --name profile-generator-container -it profile-generator
```

El parámetro `-it` permite ejecutar el contenedor de manera interactiva para que puedas ver la salida de tu aplicación en la terminal. Si tu aplicación no requiere entrada interactiva, puedes usar solo `-d` para ejecutarla en segundo plano:

```bash
docker run --name profile-generator-container -d profile-generator
```

### 6. **Verificar que el Contenedor Está Funcionando**

Puedes verificar si el contenedor está corriendo con el siguiente comando:

```bash
docker ps
```

Esto mostrará una lista de los contenedores en ejecución. Si todo está bien, deberías ver tu contenedor en la lista.

### 7. **Ver los Registros del Contenedor**

Si necesitas ver los registros de lo que está sucediendo dentro del contenedor (como si se están creando los perfiles correctamente), puedes usar:

```bash
docker logs profile-generator-container
```

### 8. **Detener y Eliminar el Contenedor**

Si necesitas detener el contenedor, usa el siguiente comando:

```bash
docker stop profile-generator-container
```

Y si luego deseas eliminar el contenedor:

```bash
docker rm profile-generator-container
```

### 9. **Guardar la Imagen Docker (Opcional)**

Si deseas compartir la imagen de Docker o mantenerla para usarla más tarde, puedes guardarla como un archivo `.tar`:

```bash
docker save -o profile-generator.tar profile-generator
```

Y luego puedes cargarla en otro entorno usando:

```bash
docker load -i profile-generator.tar
```

para  correr nuestra app con el comando :
```
docker run -it profile-generator 
```

---

### Resumen de los Pasos:

1. Crear el archivo `Dockerfile` en el directorio de tu proyecto.
2. Construir la imagen de Docker con `docker build -t instagram-profile-generator .`
3. Ejecutar el contenedor con `docker run -it instagram-profile-generator`.
4. Verificar que el contenedor esté funcionando con `docker ps`.
5. Ver los logs con `docker logs instagram-profile-generator-container`.
6. Detener y eliminar el contenedor cuando ya no lo necesites.

Siguiendo estos pasos, tu aplicación estará lista para ejecutarse dentro de un contenedor Docker.