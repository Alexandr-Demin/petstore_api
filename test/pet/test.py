# test.py
from clients.private_hhtps_bilder import get_private_https_client

client = get_private_https_client()
print(f"Base URL: {client.base_url}")
print(f"Timeout: {client.timeout}")
print(f"Headers: {client.headers}")