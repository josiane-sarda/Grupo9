class Comida:
    def __init__(self):
        self.__id = 0
        self.__pizza = ''
        self.__hamburger = ''
        self.__sushi = ''
        self.__bixcoito = ''
        self.__batata = ''
        self.__pao = ''
        self.__frango = ''
        self.__lasanha = ''
        self.__fricasse = ''
        self.__tapioca = ''

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def pizza(self):
        return self.__pizza

    @pizza.setter
    def pizza(self, pizza):
        self.__pizza = pizza

    @property
    def hamburger(self):
        return self.__hamburger

    @hamburger.setter
    def hamburger(self, hamburger):
        self.__hamburguer = hamburger

    @property
    def sushi(self):
        return self.__sushi

    @sushi.setter
    def sushi(self, sushi):
        self.__sushi = sushi

    @property
    def bixcoito(self):
        return self.__bixcoito

    @bixcoito.setter
    def bixcoito(self, bixcoito):
        self.__bixcoito = bixcoito

    @property
    def batata(self):
        return self.__batata

    @batata.setter
    def __batata(self, batata):
        self.__batata = batata

    @property
    def pao(self):
        return self.__pao

    @pao.setter
    def pao(self, pao):
        self.__pao = pao

    @property
    def frango(self):
        return self.__frango

    @frango.setter
    def frango(self, frango):
        self.__frango = frango

    @property
    def lasanha(self):
        return self.__lasanha

    @lasanha.setter
    def lasanha(self, lasanha):
        self.__lasanha = lasanha

    @property
    def fricasse(self):
        return self.__fricasse

    @fricasse.setter
    def fricasse(self, fricasse):
        self.__fricasse = fricasse

    @property
    def tapioca(self):
        return self.__tapioca

    @tapioca.setter
    def tapioca(self, tapioca):
        self.__tapioca = tapioca 
    



