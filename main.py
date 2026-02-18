from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "OptiTrade API running"}


@app.get("/account")
def account():
    return {
        "user": "Alois",
        "balance": 12450,
        "currency": "USD",
        "status": "active"
    }


@app.get("/bots")
def bots():
    return [
        {
            "name": "Celeste",
            "status": "running",
            "profit": 245.50
        },
        {
            "name": "Nova",
            "status": "stopped",
            "profit": 0
        }
    ]


@app.get("/trades")
def trades():
    return [
        {
            "pair": "BTC/USD",
            "profit": 45.2,
            "date": "2026-02-18"
        },
        {
            "pair": "GOLD",
            "profit": -12.4,
            "date": "2026-02-17"
        }
    ]

