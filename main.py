from fastapi import FastAPI
import requests
from datetime import date

app = FastAPI()

@app.get("/rugs")
async def get_rugs(today: date = date.today()):
    url = "https://testedefensoriapr.pythonanywhere.com/precos"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        data.append( { "data_atual": today } )
        return data
    else:
        return response.reason