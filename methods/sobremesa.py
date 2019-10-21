class Sobremesa: 
    def __init__(self, nome, quantidade, preco):
        self.__id= 0
        self.nome = nome 
        self.quantidade = quantidade
        self.preco = preco

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id        
   

   


