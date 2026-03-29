import requests

BASE_URL = "http://127.0.0.1:8000"

def fetch_metrics():
    try:
        return requests.get(f"{BASE_URL}/metrics", timeout=5).json()
    except:
        return {"total": 0, "spam": 0}

def fetch_sentiments():
    try:
        return requests.get(f"{BASE_URL}/sentiments", timeout=5).json()["sentiments"]
    except:
        return []