# from flask import Flask, render_template, request, redirect
# # import MySQLdb

# class Comida:
#     def __init__(self):
#         self.__id = 0
#         self.__pizza = ''
#         self.__hamburguer = ''
#         self.__sushi = ''
#         self.__bixcoito = ''
#         self.__batata = ''
#         self.__pao = ''
#         self.__frango = ''
#         self.__lasanha = ''
#         self.__fricasse = ''
#         self.__tapioca = ''

#     @property
#     def id(self):
#         return self.__id

#     @id.setter
#     def id(self, id):
#         self.__id = id

#     @property
#     def pizza(self):
#         return self.__pizza

#     @pizza.setter
#     def pizza(self, pizza):
#         self.__pizza = pizza

#     @property
#     def hamburguer(self):
#         return self.__hamburguer

#     @hamburguer.setter
#     def hamburguer(self, hamburguer):
#         self.__hamburguer = hamburguer

#     @property
#     def sushi(self):
#         return self.__sushi

#     @sushi.setter
#     def sushi(self, sushi):
#         self.__sushi = sushi

#     @property
#     def bixcoito(self):
#         return self.__bixcoito

#     @bixcoito.setter
#     def bixcoito(self, bixcoito):
#         self.__bixcoito = bixcoito

#     @property
#     def batata(self):
#         return self.__batata

#     @batata.setter
#     def __batata(self, batata):
#         self.__batata = batata

#     @property
#     def pao(self):
#         return self.__pao

#     @pao.setter
#     def pao(self, pao):
#         self.__pao = pao

#     @property
#     def frango(self):
#         return self.__frango

#     @frango.setter
#     def frango(self, frango):
#         self.__frango = frango

#     @property
#     def lasanha(self):
#         return self.__lasanha

#     @lasanha.setter
#     def lasanha(self, lasanha):
#         self.__lasanha = lasanha

#     @property
#     def fricasse(self):
#         return self.__fricasse

#     @fricasse.setter
#     def fricasse(self, fricasse):
#         self.__fricasse = fricasse
       
#     @property
#     def tapioca(self):
#         return self.__tapioca

#     @tapioca.setter
#     def tapioca(self, tapioca):
#         self.__tapioca = tapioca 


# def listar_comida_db():
#     conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
#     cursor = conexao.cursor()
#     cursor.execute("select * from COMIDA") 
#     listar_comida = []
#     for i in cursor.fetchall():
#         comida = Comida()
#         comida.id = i[0]
#         comida.pizza = i[1]
#         comida.hamburguer = i[2]
#         comida.suchi = i[3]
#         comida.bixcoito = i[4]
#         comida.batata = i[5]
#         comida.pao = i[6]
#         comida.frango = i[7]
#         comida.lasanha = i[8]
#         comida.fricasse = i[9]
#         comida.tapioca = i[10]
#         listar_comida.append(comida)

#     conexao.close()
#     return listar_comida

# def editar_comida_db(comida):
#     conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
#     cursor = conexao.cursor()
#     cursor.execute("UPDATE COMIDA SET NOME = '{}', QUANTIDADE = '{}' WHERE ID = {}"
#     .format(comida.nome, comida.quantidade, comida.id))
#     conexao.commit()
#     conexao.close()   

# def deletar_comida(id):
#     conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
#     cursor = conexao.cursor()
#     cursor.execute("DELETE FROM Comida WHERE id={}".format(id))
#     conexao.commit()
#     conexao.close()
