from .livroService import LivroService

class LivroController:
    __livroService = None
    
    def __init__(self):
        self.__livroService = LivroService()
        
    async def livro_count(self):
        return await self.__livroService.livro_count()
    
    async def get_livros(self):
        return await self.__livroService.get_livros()
    
    async def get_livro(self, id_livro: int):
        return await self.__livroService.get_livro(id_livro)
    
    async def post_livro(self, novo_livro: dict):
        return await self.__livroService.post_livro(novo_livro)
    
    async def atualiza_livro(self, id_livro: int, novo_livro: dict):
        return await self.__livroService.atualiza_livro(id_livro, novo_livro)
    
    async def delete_livro(self, id_livro: int):
        return await self.__livroService.delete_livro(id_livro)