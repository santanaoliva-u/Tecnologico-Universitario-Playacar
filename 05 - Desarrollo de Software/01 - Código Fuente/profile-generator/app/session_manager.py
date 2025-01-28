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
