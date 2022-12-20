from .livroService import LivroService

class LivroController:
    __livroService = None
    
    def __init__(self):
        self.__livroService = LivroService()
        
    def livro_count(self):
        return self.__livroService.livro_count()
    
    def get_livros(self):
        return self.__livroService.get_livros()
    
    def get_livro(self, id_livro: int):
        return self.__livroService.get_livro(id_livro)
    
    def post_livro(self, novo_livro: dict):
        return self.__livroService.post_livro(novo_livro)
    
    def atualiza_livro(self, id_livro: int, novo_livro: dict):
        return self.__livroService.atualiza_livro(id_livro, novo_livro)
    
    def delete_livro(self, id_livro: int):
        return self.__livroService.delete_livro(id_livro)