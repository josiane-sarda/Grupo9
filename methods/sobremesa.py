# from flask import Flask, render_template, request, redirect
# # import MySQLdb

# class Sobremesa:
#     def __init__(self):
#         self.__id= 0
#         self.__sorvete=''
#         self.__acai=''
#         self.__chocolate=''
#         self.__shake=''
#         self.__salada_frutas=''

#     @property
#     def id(self):
#         return self.__id

#     @id.setter
#     def id(self, id):
#         self.__id = id

#     @property
#     def sorvete(self):
#         return self.__sorvete

#     @sorvete.setter
#     def sorvete(self, sorvete):
#         self.__sorvete = sorvete

#     @property
#     def acai(self):
#         return self.__acai

#     @acai.setter
#     def acai(self, acai):
#         self.__acai = acai

#     @property
#     def chocolate(self):
#         return self.__chocolate

#     @chocolate.setter
#     def chocolate(self, chocolate):
#         self.__chocolate = chocolate

#     @property
#     def shake(self):
#         return self.__shake

#     @shake.setter
#     def shake(self, shake):
#         self.__shake = shake

#     @property
#     def salada_frutas(self):
#         return self.__salada_frutas

#     @salada_frutas.setter
#     def salada_frutas(self, salada_frutas):
#         self.__salada_frutas = salada_frutas

    
# def listar_sobremesa_db():
#     conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
#     cursor = conexao.cursor()
#     cursor.execute("select * from SOBREMESA") 
#     listar_sobremesa = []
#     for i in cursor.fetchall():
#         sobremesa = Sobremesa()
#         sobremesa.id = i[0]
#         sobremesa.sorvete = i[1]
#         sobremesa.acai = i[2]
#         sobremesa.chocolate = i[3]
#         sobremesa.shake = i[4]
#         sobremesa.salada_frutas = i[5]
        
#     conexao.close()
#     return listar_sobremesa

# def editar_sobremesa_db(sobremesa):
#     conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
#     cursor = conexao.cursor()
#     cursor.execute("UPDATE SOBREMESA SET NOME = '{}', QUANTIDADE = '{}' WHERE ID = {}"
#     .format(sobremesa.nome, sobremesa.quantidade, sobremesa.id))
#     conexao.commit()
#     conexao.close()   

# def deletar_sobremesa(id):
#     conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
#     cursor = conexao.cursor()
#     cursor.execute("DELETE FROM Sobremesa WHERE id={}".format(id))
#     conexao.commit()
#     conexao.close()



