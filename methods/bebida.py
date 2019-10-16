# from flask import Flask, render_template, request, redirect
# # import MySQLdb


# class Bebida:
#     def __init__(self):
#         self.__id= 0
#         self.__agua=''
#         self.__suco=''
#         self.__refrigerante=''
#         self.__cerveja=''
#         self.__cha=''
#         self.__cafe=''
#         self.__achocolatado=''

#     @property
#     def id(self):
#         return self.__id

#     @id.setter
#     def id(self, id):
#         self.__id = id

#     @property
#     def agua(self):
#         return self.__agua

#     @agua.setter
#     def agua(self, agua):
#         self.__agua = agua

#     @property
#     def suco(self):
#         return self.__suco

#     @suco.setter
#     def suco(self, suco):
#         self.__suco = suco

#     @property
#     def refrigerante(self):
#         return self.__refrigerante

#     @refrigerante.setter
#     def refrigerante(self, refrigerante):
#         self.__refrigerante = refrigerante
        
#     @property
#     def cerveja(self):
#         return self.__cerveja

#     @cerveja.setter
#     def cerveja(self, cerveja):
#         self.__cerveja = cerveja

#     @property
#     def cha(self):
#         return self.__cha

#     @cha.setter
#     def cha(self, cha):
#         self.__cha = cha

#     @property
#     def cafe(self):
#         return self.__cafe

#     @cafe.setter
#     def cafe(self, cafe):
#         self.__cafe = cafe

#     @property
#     def achocolatado(self):
#         return self.__achocolatado

#     @achocolatado.setter
#     def achocolatado(self, achocolatado):
#         self.__achocolatado = achocolatado


# def listar_bebida_db():
#     conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
#     cursor = conexao.cursor()
#     cursor.execute("select * from BEBIDA") 
#     listar_bebida = []
#     for i in cursor.fetchall():
#         bebida = Bebida()
#         bebida.id = i[0]
#         bebida.agua = i[1]
#         bebida.suco = i[2]
#         bebida.refrigerante = i[3]
#         bebida.cerveja = i[4]
#         bebida.cha = i[5]
#         bebida.cafe = i[6]
#         bebida.achocolatado = i[7]
#         listar_bebida.append(bebida)

#     conexao.close()
#     return listar_bebida

# def editar_bebida_db(bebida):
#     conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
#     cursor = conexao.cursor()
#     cursor.execute("UPDATE BEBIDA SET NOME = '{}', QUANTIDADE = '{}' WHERE ID = {}"
#     .format(bebida.nome, bebida.quantidade, bebida.id))
#     conexao.commit()
#     conexao.close()   

# def deletar_bebida(id):
#     conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
#     cursor = conexao.cursor()
#     cursor.execute("DELETE FROM Bebida WHERE id={}".format(id))
#     conexao.commit()
#     conexao.close()



    

    
    

    