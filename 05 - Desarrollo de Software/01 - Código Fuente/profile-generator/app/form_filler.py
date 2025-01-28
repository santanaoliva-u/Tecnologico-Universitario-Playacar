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
