from fastapi import FastAPI

app = FastAPI()


# ROOT
@app.get("/")
def root():
    return {"message": "OptiTrade API running"}


# ACCOUNT
@app.get("/account")
def get_account():
    return {
        "name": "Aloïs",
        "capital": 24830.42,
        "bot": "CELESTE"
    }


# BOT
@app.get("/bot")
def get_bot():
    return {
        "bot": "CELESTE",
        "status": "running",
        "mode": "Normal"
    }


# TRADES
@app.get("/trades")
def get_trades():
    return [
        {"pair": "XAU/USD", "result": "+0.18%"},
        {"pair": "XAU/USD", "result": "-0.06%"},
        {"pair": "XAU/USD", "result": "+0.27%"}
    ]

