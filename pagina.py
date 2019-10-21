from flask import Flask, render_template, request, redirect
import MySQLdb
from methods.cadastro import Cadastro
from methods.prato import Prato
from methods.bebida import Bebida
from methods.sobremesa import Sobremesa

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

def salvar_sobremesa_db(nome, preco, quantidade):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO `SOBREMESAS` (`NOME`, `QUANTIDADE`, `PRECO`)" + 
    " VALUES ('{}', '{}', '{}')".format(nome, preco, quantidade))
    conexao.commit()
    conexao.close()


def listar_sobremesa_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
    cursor = conexao.cursor()
    cursor.execute("select * from SOBREMESAS") 
    listar_sobremesa = []
    for i in cursor.fetchall():
        nova_sobremesa = Sobremesa()
        nova_sobremesa.id = i[0]
        nova_sobremesa.nome = i[1] 
        nova_sobremesa.quantidade = i[2]
        nova_sobremesa.preco = i[3]      
        listar_sobremesa.append(nova_sobremesa)
    
    conexao.close()
    return listar_sobremesa

def editar_sobremesa_db(id, nome, quantidade, preco):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
    cursor = conexao.cursor()
    cursor.execute("UPDATE `SOBREMESAS` SET `NOME` = '{}', `QUANTIDADE` = {}, `PRECO` = {} WHERE `ID` = {}"
    .format(nome, quantidade, preco , id))
    conexao.commit()
    conexao.close()   

def deletar_sobremesa(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM `SOBREMESAS` WHERE id={}".format(id))
    conexao.commit()
    conexao.close()

def buscar_em_sobremesa(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
    cursor = conexao.cursor()
    cursor.execute("select * from `SOBREMESAS` WHERE `ID` ={}".format(id))
    s = Sobremesa()
    for i in cursor.fetchall():
        s.id = i[0]
        s.nome = i[1]
        s.quantidade = i[2]
        s.preco = i[3]
    conexao.commit()
    conexao.close()
    return s                

############################### PEDIDO ##########################################






################################-ROTAS-############################################################

app= Flask(__name__)
pagina_nome = 'nome'

@app.route('/')
def inicio():
    return render_template('home.html', pagina_nome = pagina_nome)

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

@app.route('/sobremesa/salvar', methods = ['POST'])
def salvar_sobremesa():
    nome = request.form['item'] 
    preco = request.form['preco']
    quantidade = request.form['quant']
    nova_sobremesa = Sobremesa()
    nova_sobremesa.nome = nome
    nova_sobremesa.preco = preco
    nova_sobremesa.quantidade = quantidade
    salvar_sobremesa_db(nova_sobremesa.nome, nova_sobremesa.preco, nova_sobremesa.quantidade)    
    return redirect('/sobremesa')

@app.route('/deletar/sobremesa')
def apagar_sobremesa():
    id = request.args['id']
    deletar_sobremesa(id)
    return redirect('/sobremesa')

@app.route('/alterar/sobremesa')
def alterar_sobremesa():
    id = request.args['id']
    alteracao_sobremesa = buscar_em_sobremesa(id)
    return render_template('alterar.html', alterar_sobremesa = alteracao_sobremesa)    

@app.route('/alterar/salvar/sobremesa', methods=['POST'])
def salvar_alteracao_sobremesa():
    id = request.form['id']
    nome = request.form['nome']     
    quantidade = request.form['quantidade'] 
    preco = request.form['preco']
    editar_sobremesa_db(id, nome, quantidade, preco)
    return redirect('/sobremesa') 

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
