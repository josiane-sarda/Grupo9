class Bebida:
    def __init__(self):
        self.__id= 0
        self.__agua=''
        self.__suco=''
        self.__refrigerante=''
        self.__cerveja=''
        self.__cha=''
        self.__cafe=''
        self.__achocolatado=''

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def agua(self):
        return self.__agua

    @agua.setter
    def agua(self, agua):
        self.__agua = agua

    @property
    def suco(self):
        return self.__suco

    @suco.setter
    def suco(self, suco):
        self.__suco = suco

    @property
    def refrigerante(self):
        return self.__refrigerante

    @refrigerante.setter
    def refrigerante(self, refrigerante):
        self.__refrigerante = refrigerante
        
    @property
    def cerveja(self):
        return self.__cerveja

    @cerveja.setter
    def cerveja(self, cerveja):
        self.__cerveja = cerveja

    @property
    def cha(self):
        return self.__cha

    @cha.setter
    def cha(self, cha):
        self.__cha = cha

    @property
    def cafe(self):
        return self.__cafe

    @cafe.setter
    def cafe(self, cafe):
        self.__cafe = cafe

    @property
    def achocolatado(self):
        return self.__achocolatado

    @achocolatado.setter
    def achocolatado(self, achocolatado):
        self.__achocolatado = achocolatado

    

    
    

    