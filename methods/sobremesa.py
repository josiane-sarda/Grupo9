class Comida:
    def __init__(self):
        self.__id= 0
        self.__sorvete=''
        self.__acai=''
        self.__chocolate=''
        self.__shake=''
        self.__salada_frutas=''

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def sorvete(self):
        return self.__sorvete

    @sorvete.setter
    def sorvete(self, sorvete):
        self.__sorvete = sorvete

    @property
    def acai(self):
        return self.__acai

    @acai.setter
    def acai(self, acai):
        self.__acai = acai

    @property
    def chocolate(self):
        return self.__chocolate

    @chocolate.setter
    def chocolate(self, chocolate):
        self.__chocolate = chocolate

    @property
    def shake(self):
        return self.__shake

    @shake.setter
    def shake(self, shake):
        self.__shake = shake

    @property
    def salada_frutas(self):
        return self.__salada_frutas

    @salada_frutas.setter
    def salada_frutas(self, salada_frutas):
        self.__salada_frutas = salada_frutas

    



