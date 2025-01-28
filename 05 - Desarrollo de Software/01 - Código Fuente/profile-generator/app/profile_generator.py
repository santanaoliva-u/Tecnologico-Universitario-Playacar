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
