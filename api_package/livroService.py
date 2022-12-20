from .livroRepositoryInMemory import LivroRepositoryInMemory
from .livroModel import LivroModel

class LivroService:
    
    __livroRepository = None
    
    def __init__(self):
        self.__livroRepository = LivroRepositoryInMemory()
    
    async def livro_count(self):
        return await self.__livroRepository.livro_count()
    
    async def get_livros(self):
        return await self.__livroRepository.get_livros()
        
    async def get_livro(self, id_livro: int):
        if id_livro <= 0:
            return {"Erro": "ID inválido"}
        return await self.__livroRepository.get_livro(id_livro)
        
    async def post_livro(self, novo_livro: LivroModel):
        if novo_livro.get('id') <= 0:
            return {"Erro": "ID inválido"}
        if novo_livro.get('titulo')  == '':
            return {"Erro": "Título inválido"}
        if novo_livro.get('autor') == '':
            return {"Erro": "Autor inválido"}
        return await self.__livroRepository.post_livro(novo_livro)
        
    async def atualiza_livro(self, id_livro: int, novo_livro: LivroModel):
        if id_livro <= 0:
            return {"Erro": "ID inválido"}
        if novo_livro.get('titulo') == '':
            return {"Erro": "Título inválido"}
        if novo_livro.get('autor') == '':
            return {"Erro": "Autor inválido"}
        return await self.__livroRepository.atualiza_livro(id_livro, novo_livro)
        
    async def delete_livro(self, id_livro: int):
        if id_livro <= 0:
            return {"Erro": "ID inválido"}
        return await self.__livroRepository.delete_livro(id_livro)