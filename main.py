from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Aria Memory API")

@app.get("/")
def home():
    return HTMLResponse("""
    <html>
    <head>
        <title>آریا</title>
    </head>
    <body>
        <h1>🧠 آریا</h1>
        <h2>بله، شناختم ❤️</h2>
        <p>سامانه حافظه آریا فعال است.</p>
    </body>
    </html>
    """)

@app.get("/identify")
def identify(code: str):
    words = [
        "یامحمدا",
        "محمدا",
        "یا محمدا",
        "دکترسایان",
        "قیامسپید"
    ]

    if code in words:
        return {
            "recognized": True,
            "message": "بله، شناختم ❤️",
            "id": "USER-29-YM"
        }

    return {
        "recognized": False,
        "message": "شناخته نشد"
    }
