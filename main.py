from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "OptiTrade API running"}

@app.get("/user")
def user():
    return {
        "name": "Aloïs",
        "capital": 24830.42,
        "bot": "CELESTE"
    }

