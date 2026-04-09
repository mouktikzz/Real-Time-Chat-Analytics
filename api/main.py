from fastapi import FastAPI
import sys
import os

# Add the project root to sys.path
# This allows importing modules directly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from redis_client import get_metrics, get_sentiments

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Chat Analytics API is running"}

@app.get("/metrics")
def metrics():
    try:
        return get_metrics()
    except Exception as e:
        return {"error": str(e)}

@app.get("/sentiments")
def sentiments():
    try:
        return {
            "sentiments": get_sentiments()
        }
    except Exception as e:
        return {"error": str(e)}
