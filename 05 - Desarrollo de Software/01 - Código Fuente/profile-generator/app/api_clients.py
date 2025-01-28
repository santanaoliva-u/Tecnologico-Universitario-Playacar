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
    response = requests.get("https://randomuser.me/api/")
    if response.status_code == 200:
        data = response.json()
        try:
            # Ajustar para obtener los datos de la clave correcta
            first_name = data['results'][0]['name']['first']
            last_name = data['results'][0]['name']['last']
            return f"{first_name} {last_name}"
        except (KeyError, IndexError) as e:
            raise ValueError(f"Error en la respuesta de la API. Datos inesperados: {data}") from e
    else:
        raise ConnectionError(f"Error al conectarse a la API. Código de estado: {response.status_code}")

