class Comida:
    def __init__(self):
        self.__id = 0
        self.__pizza = ''
        self.__hamburger = ''
        self.__sushi = ''
        self.__picanha_defumada_com_risoto = ''
        self.__bixcoito_carioca = ''
        self.__batata_frita = ''
        self.__pao_de_queijo = ''
        self.__frango_frito = ''
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

    @tipo.setter
    def pizza(self, pizza):
        self.__tipo = __pizza

    @property
    def hamburger(self):
        return self.__hamburger

    @descricao.setter
    def hamburger(self, hamburger):
        self.__descricao = __hamburger
