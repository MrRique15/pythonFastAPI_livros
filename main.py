# API PARA CONSTULTA, INSERÇÃO, REMOÇÃO E ATUALIZAÇÃO DE LIVROS
# Endpoints:
# GET /livros - Retorna todos os livros
# POST /livros - Insere um novo livro
# GET /livros/{id} - Retorna um livro específico
# PUT /livros/{id} - Atualiza um livro específico
# DELETE /livros/{id} - Remove um livro específico
import uvicorn
from fastapi import FastAPI
from api_package.livroController import LivroController
from api_package.livroModel import LivroModel

app = FastAPI()
livroController = LivroController()

#Home page
@app.get("/")
async def home():
    return await livroController.livro_count()

#Listar todos os livros
@app.get("/livros")
async def get_livros():
    return await livroController.get_livros()

#Inserir novo livro
@app.post("/livros")
async def post_livro(novo_livro: LivroModel):
    return await livroController.post_livro(novo_livro)

#Consultar um livro com ID
@app.get("/livros/{id_livro}")
async def get_livro(id_livro: int):
    return await livroController.get_livro(id_livro)

#Atualizar um livro com ID
@app.put("/livros/{id_livro}")
async def atualiza_livro(id_livro: int, novo_livro: LivroModel):
    return await livroController.atualiza_livro(id_livro, novo_livro)

#Deletar um livro com ID
@app.delete("/livros/{id_livro}")
async def delete_livro(id_livro: int):
    return await livroController.delete_livro(id_livro)


if __name__ == '__main__':
    uvicorn.run("main:app", host='localhost', port=7779, reload='true')