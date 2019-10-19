class Cadastro:
    def __init__(self):
        self.__id= 0
        self.__nome=''
        self.__senha=''
        self.__cpf=''
        self.__endereco=''

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def senha(self):
        return self.__senha
    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def endereco(self):
        return self.__endereco
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco