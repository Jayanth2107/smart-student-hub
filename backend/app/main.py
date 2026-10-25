from fastapi import FastAPI

app = FastAPI(title="Smart Student Hub API")


@app.get("/")
def home():
    return {
        "message": "Welcome to Smart Student Hub API"
    }