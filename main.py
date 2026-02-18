from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "OptiTrade API running"}


@app.get("/dashboard")
def dashboard():

    return {

        "name": "Aloïs",
        "capital": 24830.42,
        "bot": "CELESTE",
        "market": "Gold (XAU/USD)",
        "ytd": 16.3,
        "subscription": "Core",
        "renewal": "12 April 2026",

        "trades": [

            {"type": "BUY", "pair": "XAU/USD", "result": 0.18},
            {"type": "SELL", "pair": "XAU/USD", "result": -0.06},
            {"type": "BUY", "pair": "XAU/USD", "result": 0.27}

        ]

    }


@app.get("/nova")
def nova():

    return {

        "capital": 175295.81,
        "bot": "ORION",
        "market": "Bitcoin (BTC/USD)",
        "ytd": 16.3

    }


@app.get("/profile")
def profile():

    return {

        "name": "Aloïs Truchet",
        "capital": 24830.42,
        "bots": ["Celeste", "Orion", "Astra", "Lyra"]

    }


@app.get("/market")
def market():

    return {

        "asset": "Bitcoin",
        "value": 69185.72,
        "performance": 53.65

    }

