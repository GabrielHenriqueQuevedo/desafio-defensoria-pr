from fastapi import FastAPI
from datetime import date
import requests

app = FastAPI()

@app.get("/rugs")
async def get_rugs(date: date = date.today()):
    url = "https://testedefensoriapr.pythonanywhere.com/precos"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        json =  { "sucesso" : True, "data_atual": date, "tapetes" : data } 
        return json
    else:
        return {"sucesso" : False, "mensagem" : "Não foi possível consumir a API de preços de tapetes.", "erro" : response.reason}