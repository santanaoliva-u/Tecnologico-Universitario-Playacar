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
