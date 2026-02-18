from fastapi import FastAPI

app = FastAPI()


# ROOT
@app.get("/")
def root():
    return {"message": "OptiTrade API running"}


# USER
@app.get("/user")
def get_user():
    return {
        "name": "Aloïs",
        "capital": 24830.42,
        "bot": "CELESTE"
    }


# NOVA
@app.get("/nova")
def get_nova():
    return {
        "status": "ACTIVE",
        "ai": "NOVA",
        "version": "1.0"
    }


# TRADES
@app.get("/trades")
def get_trades():
    return [
        {"pair": "BTC/USD", "profit": 420},
        {"pair": "XAU/USD", "profit": 210}
    ]

