from pydantic import BaseModel 

class LivroModel(BaseModel):
    id: int
    titulo: str
    autor: str
    
    def get(self, key):
        return self.__dict__[key]