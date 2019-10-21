class Login :
    def __init__(self):
        self.__id= 0
        self.__email=''
        self.__senha=''
       

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nome(self):
        return self.__email
    @nome.setter
    def nome(self, email):
        self.__email = email

    @property
    def senha(self):
        return self.__senha
    @senha.setter
    def senha(self, senha):
        self.__senha = senha