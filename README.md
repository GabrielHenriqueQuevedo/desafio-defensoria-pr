# Desafio Back-end: API de Integração Aladdin

## Sobre
Projeto de desenvolvimento de uma API com python para desafio da defensoria pública do Paraná.

## Funcionalidade
Cria uma API que consome uma API externa contendo preços de tapetes.

## Tecnologias
`Python 3.10` utilizando a biblioteca `FastApi` para criação da API e a biblioteca `Requests` para consumação da API externa.

## Como executar
Aqui vai o passo a passo de como executar esta aplicação.

### Instalações
Python deve estar instalado, versão 3.10.11, que se encontra neste link:

`https://www.python.org/downloads/release/python-31011/`

Também deve estar instalado duas bibliotecas. Execute os seguintes comando em um terminal:

- FastApi: `pip install "fastapi[standard]"`

- Requests: `python -m pip install requests`

### Execução
Depois de instalado, abra um terminal no mesmo diretório onde se encontra o arquivo `api.py`, e execute o seguinte comando:
`fastapi dev`

Então acesse o endpoint `http://127.0.0.1:8000/rugs` e `http://127.0.0.1:8000/docs` para acessar a documentação.
