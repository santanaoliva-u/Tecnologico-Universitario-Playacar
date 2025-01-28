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
