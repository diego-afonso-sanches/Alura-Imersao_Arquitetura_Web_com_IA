# Importa o módulo os para manipulação de caminhos do sistema operacional
import os
# Importa o módulo glob para busca de arquivos correspondentes a padrões
import glob
# Importa as classes necessárias do FastAPI
from fastapi import FastAPI, HTTPException
# Importa a resposta de arquivo para servir imagens
from fastapi.responses import FileResponse
# Importa o middleware CORS para permitir requisições de outras origens
from fastapi.middleware.cors import CORSMiddleware

# Cria a instância da aplicação FastAPI
app = FastAPI()

# Configura o middleware CORS para permitir requisições de qualquer origem (frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define o caminho absoluto para a pasta onde as imagens estão salvas
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Lista de figurinhas em memória (simulando um banco de dados simples)
# Deixe ativas apenas as figurinhas cujas imagens existem na pasta figurinhas/
# NOTA: Como todas as 30 imagens existem na pasta local, todas foram deixadas ativas.
# Se alguma estivesse faltando, bastaria comentá-la na lista abaixo.
figurinhas = [
    {
        "id": 1,
        "nome": "Alan Turing",
        "categoria": "IA",
        "imagem_url": "/figurinhas/1/imagem"
    },
    {
        "id": 2,
        "nome": "John McCarthy",
        "categoria": "IA",
        "imagem_url": "/figurinhas/2/imagem"
    },
    {
        "id": 3,
        "nome": "Sam Altman",
        "categoria": "IA",
        "imagem_url": "/figurinhas/3/imagem"
    },
    {
        "id": 4,
        "nome": "Geoffrey Hinton",
        "categoria": "IA",
        "imagem_url": "/figurinhas/4/imagem"
    },
    {
        "id": 5,
        "nome": "Yann LeCun",
        "categoria": "IA",
        "imagem_url": "/figurinhas/5/imagem"
    },
    {
        "id": 6,
        "nome": "Guido van Rossum",
        "categoria": "PYTHON",
        "imagem_url": "/figurinhas/6/imagem"
    },
    {
        "id": 7,
        "nome": "Tim Peters",
        "categoria": "PYTHON",
        "imagem_url": "/figurinhas/7/imagem"
    },
    {
        "id": 8,
        "nome": "Raymond Hettinger",
        "categoria": "PYTHON",
        "imagem_url": "/figurinhas/8/imagem"
    },
    {
        "id": 9,
        "nome": "Travis Oliphant",
        "categoria": "PYTHON",
        "imagem_url": "/figurinhas/9/imagem"
    },
    {
        "id": 10,
        "nome": "Wes McKinney",
        "categoria": "PYTHON",
        "imagem_url": "/figurinhas/10/imagem"
    },
    {
        "id": 11,
        "nome": "Edgar F. Codd",
        "categoria": "BANCO DE DADOS",
        "imagem_url": "/figurinhas/11/imagem"
    },
    {
        "id": 12,
        "nome": "Larry Ellison",
        "categoria": "BANCO DE DADOS",
        "imagem_url": "/figurinhas/12/imagem"
    },
    {
        "id": 13,
        "nome": "Michael Widenius",
        "categoria": "BANCO DE DADOS",
        "imagem_url": "/figurinhas/13/imagem"
    },
    {
        "id": 14,
        "nome": "Salvatore Sanfilippo",
        "categoria": "BANCO DE DADOS",
        "imagem_url": "/figurinhas/14/imagem"
    },
    {
        "id": 15,
        "nome": "Eliot Horowitz",
        "categoria": "BANCO DE DADOS",
        "imagem_url": "/figurinhas/15/imagem"
    },
    {
        "id": 16,
        "nome": "Linus Torvalds",
        "categoria": "SISTEMAS OPERACIONAIS",
        "imagem_url": "/figurinhas/16/imagem"
    },
    {
        "id": 17,
        "nome": "Dennis Ritchie",
        "categoria": "SISTEMAS OPERACIONAIS",
        "imagem_url": "/figurinhas/17/imagem"
    },
    {
        "id": 18,
        "nome": "Richard Stallman",
        "categoria": "SISTEMAS OPERACIONAIS",
        "imagem_url": "/figurinhas/18/imagem"
    },
    {
        "id": 19,
        "nome": "Bill Gates",
        "categoria": "SISTEMAS OPERACIONAIS",
        "imagem_url": "/figurinhas/19/imagem"
    },
    {
        "id": 20,
        "nome": "Steve Jobs",
        "categoria": "SISTEMAS OPERACIONAIS",
        "imagem_url": "/figurinhas/20/imagem"
    },
    {
        "id": 21,
        "nome": "Paulo Silveira",
        "categoria": "BRASIL",
        "imagem_url": "/figurinhas/21/imagem"
    },
    {
        "id": 22,
        "nome": "Guilherme Silveira",
        "categoria": "BRASIL",
        "imagem_url": "/figurinhas/22/imagem"
    },
    {
        "id": 23,
        "nome": "Gustavo Guanabara",
        "categoria": "BRASIL",
        "imagem_url": "/figurinhas/23/imagem"
    },
    {
        "id": 24,
        "nome": "Maurício Aniche",
        "categoria": "BRASIL",
        "imagem_url": "/figurinhas/24/imagem"
    },
    {
        "id": 25,
        "nome": "Andre David",
        "categoria": "BRASIL",
        "imagem_url": "/figurinhas/25/imagem"
    },
    {
        "id": 26,
        "nome": "Guilherme Lima",
        "categoria": "BRASIL",
        "imagem_url": "/figurinhas/26/imagem"
    },
    {
        "id": 27,
        "nome": "Gi Space Coding",
        "categoria": "BRASIL",
        "imagem_url": "/figurinhas/27/imagem"
    },
    {
        "id": 28,
        "nome": "Vinicius Neves",
        "categoria": "BRASIL",
        "imagem_url": "/figurinhas/28/imagem"
    },
    {
        "id": 29,
        "nome": "Rafaela Ballerini",
        "categoria": "BRASIL",
        "imagem_url": "/figurinhas/29/imagem"
    },
    {
        "id": 30,
        "nome": "Diego Sanches",
        "categoria": "BRASIL",
        "imagem_url": "/figurinhas/30/imagem"
    }
]

# Define a rota para o método GET em "/figurinhas"
@app.get("/figurinhas")
def listar_figurinhas():
    """
    Função que responde ao endpoint '/figurinhas'.
    Retorna a lista de todas as figurinhas ativas.
    """
    return figurinhas

# Define a rota para o método GET em "/figurinhas/{id}/imagem"
@app.get("/figurinhas/{id}/imagem")
def obter_imagem_figurinha(id: int):
    """
    Função que busca o arquivo da imagem correspondente ao ID informado.
    Utiliza glob para buscar o arquivo com prefixo formatado de dois dígitos.
    Retorna o arquivo de imagem se encontrado, ou erro 404 se não existir.
    """
    # Define o padrão de busca (ex: 01[!0-9]*)
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    arquivos_encontrados = glob.glob(padrao)

    if not arquivos_encontrados:
        raise HTTPException(status_code=404, detail="Imagem não encontrada.")

    # Retorna o primeiro arquivo correspondente encontrado
    caminho_imagem = arquivos_encontrados[0]
    return FileResponse(caminho_imagem)
