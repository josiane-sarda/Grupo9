from flask import Flask, render_template, request, redirect
import MySQLdb
from methods.cadastro import Cadastro
from methods.prato import Prato
from methods.bebida import Bebida
from methods.sobremesa import Sobremesa

conexao_mysql  = MySQLdb.connect(host='mysql.zuplae.com', database='zuplae14', user='zuplae14', passwd='grupo09')
app= Flask(__name__)
pagina_nome = 'nome'
#################### CADASTRO ##########################################


def salvar_cliente_db(cliente):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
    cursor = conexao.cursor()
    cursor.execute("UPDATE CADASTRO SET nome='{}', senha='{}', cpf='{}', endereco='{}' WHERE ID={}"
    .format(cliente.nome, cliente.senha, cliente.cpf, cliente.endereco , cliente.id))
    conexao.commit()

@app.route('/login', methods=['POST'])
def salvar_cliente():
    id = request.form['id']
    nome = request.form['nome']
    senha = request.form['senha']
    cpf = request.form['cpf']
    endereco = request.form['endereco']
    cliente = Cadastro()
    cliente.id = id 
    cliente.nome = nome 
    cliente.senha = senha
    cliente.cpf = cpf
    cliente.endereco = endereco
    salvar_cliente_db(cliente)
    return redirect ('/home')


#################### PRATO ##########################################


def listar_prato_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
    cursor = conexao.cursor()
    cursor.execute("select * from PRATOS") 
    listar_prato = []
    for i in cursor.fetchall():
        prato = Prato(i[0],i[1],i[2],i[3])       
        listar_prato.append(prato)

    conexao.close()
    return listar_prato

def editar_prato_db(prato):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
    cursor = conexao.cursor()
    cursor.execute("UPDATE PRATO SET NOME = '{}', QUANTIDADE = '{}', PRECO = '{}' WHERE ID = {}"
    .format(prato.nome, prato.quantidade, prato.preco ,prato.id))
    conexao.commit()
    conexao.close()   

def deletar_prato(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Prato WHERE id={}".format(id))
    conexao.commit()
    conexao.close()


#################### BEBIDA ##########################################



def listar_bebida_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
    cursor = conexao.cursor()

    cursor.execute("select * from BEBIDAS") 
    listar_bebida = []
    for i in cursor.fetchall():
        bebida = Bebida(i[0],i[1],i[2],i[3])
        listar_bebida.append(bebida)

    conexao.close()
    return listar_bebida

def editar_bebida_db(bebida):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
    cursor = conexao.cursor()
    cursor.execute("UPDATE BEBIDAS SET NOME = '{}', QUANTIDADE = '{}', PRECO = '{}' WHERE ID = {}"
    .format(bebida.nome, bebida.quantidade,bebida.preco ,bebida.id))
    conexao.commit()
    conexao.close()   

def deletar_bebida(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM BEBIDAS WHERE id={}".format(id))
    conexao.commit()
    conexao.close()


#################### SOBREMESA ##########################################


def listar_sobremesa_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
    cursor = conexao.cursor()
    cursor.execute("select * from SOBREMESAS") 
    listar_sobremesa = []
    for i in cursor.fetchall():
        sobremesa = Sobremesa(i[0],i[1],i[2],i[3])       
        listar_sobremesa.append(sobremesa)
    
    conexao.close()
    return listar_sobremesa

def editar_sobremesa_db(sobremesa):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
    cursor = conexao.cursor()
    cursor.execute("UPDATE SOBREMESAS SET NOME = '{}', QUANTIDADE = '{}', PRECO = '{}' WHERE ID = {}"
    .format(sobremesa.nome, sobremesa.quantidade,sobremesa.preco ,sobremesa.id))
    conexao.commit()
    conexao.close()   

def deletar_sobremesa(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM SOBREMESAS WHERE id={}".format(id))
    conexao.commit()
    conexao.close()

############################### PEDIDO ##########################################






################################-ROTAS-############################################################


@app.route('/')
def inicio():
    return render_template('login.html', pagina_nome = pagina_nome)

@app.route('/home')
def principal():
    
    return render_template('home.html', pagina_nome = pagina_nome)

@app.route('/comida')
def comida():
    guto = listar_prato_db()
    return render_template('comida.html', pagina_nome = pagina_nome, lista_html = guto)

@app.route('/bebida')
def babida():
    lenda = listar_bebida_db()
    return render_template('bebida.html', pagina_nome = pagina_nome, lista_html = lenda)

@app.route('/sobremesa')
def sobremesa():
    carioca = listar_sobremesa_db()
    return render_template('sobremesa.html', pagina_nome = pagina_nome, lista_html = carioca)

@app.route('/pedido')
def pedido():
    return render_template('pedido.html', pagina_nome = pagina_nome)

@app.route('/pedido/confirmar', methods=['POST'])
def confirmar_pedido():
    return 'Pedido confirmado! - Seu pedido está a caminho!'

@app.route('/pedido/cancelar', methods=['POST'])
def cancelar_pedido():
    return 'Pedido cancelado!'


app.run()
