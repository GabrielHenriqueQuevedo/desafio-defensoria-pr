import requests
from fastapi import FastAPI
from datetime import date

# Cria um objeto do tipo "FastApi" e configura a documentação
app: FastAPI = FastAPI(
    title = "Desafio Defensoria PR",
    description = "API de consumação de uma API externa de preços de tapetes.",
    version = "1.0.0",
    redoc_url = None
)

# Cria o endpoint "/rugs" e o coloca na tag "Endpoint" do swagger
@app.get("/rugs", tags=["Endpoint"])

# Cria a função executada ao acessar o endpoint "/rugs"
# Função consome uma API externa, caso tenha sucesso retorna um dicionário contendo a data atual
# Junto com as informações dos tapetes
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