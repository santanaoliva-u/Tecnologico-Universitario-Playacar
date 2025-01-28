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
