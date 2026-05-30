import requests
from fastapi import FastAPI
from datetime import date

app: FastAPI = FastAPI()

@app.get("/rugs")
async def get_rugs(date: date = date.today()) -> dict:
    url: str = "https://testedefensoriapr.pythonanywhere.com/precos"
    response: requests.models.Response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        result = { 
                    "sucesso": True,
                    "data_atual": date,
                    "tapetes": data
                } 
        
        return result
    else:
        result = {
                    "sucesso": False, 
                    "mensagem": "Não foi possível consumir a API de preços de tapetes.", 
                    "erro": response.reason
                }
        
        return result