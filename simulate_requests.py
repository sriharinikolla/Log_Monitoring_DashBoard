import requests
import random
import time

endpoints = [
    "http://localhost:5000/api/login",
    "http://localhost:5000/api/logout",
    "http://localhost:5000/api/products",
    "http://localhost:5000/api/orders",
    "http://localhost:5000/api/status"
]

while True:
    endpoint = random.choice(endpoints)
    try:
        r = requests.get(endpoint)
        print(f"Requested {endpoint} → {r.status_code}")
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(1)
