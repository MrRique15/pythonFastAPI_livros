from .livroModel import LivroModel

class LivroRepositoryInMemory:
    
    __livros = []
    
    def __init__(self):
        self.__livros = [
            LivroModel(id=1, titulo='O Senhor dos Anéis - A Sociedade do Anel', autor='J.R.R Tolkien'),
            LivroModel(id=2, titulo='Harry Potter e a Pedra Filosofal', autor='J.K Howling'),
            LivroModel(id=3, titulo='Hábitos Atômicos', autor='James Clear'),
        ]
        
    def livro_count(self):
        return {"Livros Cadastrados": len(self.__livros)}
    
    def get_livros(self):
        return self.__livros
    
    def get_livro(self, id_livro: int):
        for livro in self.__livros:
            if livro.id == id_livro:
                return livro
        return {"Erro": "Livro não encontrado"}
    
    def post_livro(self, novo_livro: LivroModel):
        for livro in self.__livros:
            if livro.id == novo_livro.id:
                return {"Erro": "ID de livro já cadastrado"}
        self.__livros.append(novo_livro)
        return novo_livro
    
    def atualiza_livro(self, id_livro: int, novo_livro: LivroModel):
        for indice,livro in enumerate(self.__livros):
            if livro.id == id_livro:
                self.__livros[indice] = novo_livro
                return self.__livros[indice]
        return {"Erro": "Livro não encontrado"}
    
    def delete_livro(self, id_livro: int):
        for indice,livro in enumerate(self.__livros):
            if livro.id == id_livro:
                del self.__livros[indice]
                return self.__livros
        return {"Erro": "Livro não encontrado"}
