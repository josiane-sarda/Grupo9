from flask import Flask, render_template, request, redirect
import MySQLdb
from methods.prato import Prato
from methods.bebida import Bebida
from methods.sobremesa import Sobremesa

#################### PRATO ##########################################

def salvar_prato_db(nome, preco, quantidade):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO `PRATOS` (`NOME`, `QUANTIDADE`, `PRECO`)" + 
    " VALUES ('{}', '{}', '{}')".format(nome, preco, quantidade))
    conexao.commit()
    conexao.close()

def listar_prato_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
    cursor = conexao.cursor()
    cursor.execute("select * from `PRATOS`") 
    listar_prato = []
    for i in cursor.fetchall():
        novo_prato = Prato()
        novo_prato.id = i[0]
        novo_prato.nome = i[1] 
        novo_prato.quantidade = i[2]
        novo_prato.preco = i[3]      
        listar_prato.append(novo_prato)
    conexao.close()
    return listar_prato

def editar_prato_db(id, nome, quantidade, preco):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
    cursor = conexao.cursor()
    cursor.execute("UPDATE `PRATOS` SET `NOME` = '{}', `QUANTIDADE` = {}, `PRECO` = {} WHERE `ID` = {}"
    .format(nome, quantidade, preco ,id))
    conexao.commit()
    conexao.close()   

def deletar_prato(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM `PRATOS` WHERE `ID`={}".format(id))
    conexao.commit()
    conexao.close()


def buscar_em_prato(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
    cursor = conexao.cursor()
    cursor.execute("select * from `PRATOS` WHERE `ID` ={}".format(id))
    p = Prato()
    for i in cursor.fetchall():
        p.id = i[0]
        p.nome = i[1] 
        p.quantidade = i[2]
        p.preco = i[3]      
    conexao.commit()
    conexao.close()
    return p    



#################### BEBIDA ##########################################


def salvar_bebida_db(nome, preco, quantidade):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO `BEBIDAS` (`NOME`, `PRECO`, `QUANTIDADE`)" + 
    " VALUES ('{}', '{}', '{}')".format(nome, preco, quantidade))
    conexao.commit()
    conexao.close()

def listar_bebida_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
    cursor = conexao.cursor()
    cursor.execute("select * from `BEBIDAS`") 
    listar_bebida = []
    for i in cursor.fetchall():
        nova_bebida = Bebida()
        nova_bebida.id = i[0]
        nova_bebida.nome = i[1] 
        nova_bebida.preco = i[3]      
        nova_bebida.quantidade = i[2]
        listar_bebida.append(nova_bebida)
    conexao.close()
    return listar_bebida

def editar_bebida_db(id, nome, quantidade, preco):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
    cursor = conexao.cursor()
    cursor.execute("UPDATE `BEBIDAS` SET `NOME` = '{}', PRECO = {}, `QUANTIDADE` = {} WHERE `ID` = {}"
    .format(nome, quantidade, preco ,id))
    conexao.commit()
    conexao.close()   

def deletar_bebida(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM `BEBIDAS` WHERE `ID`={}".format(id))
    conexao.commit()
    conexao.close()


def buscar_em_bebida(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
    cursor = conexao.cursor()
    cursor.execute("select * from `BEBIDAS` WHERE `ID` ={}".format(id))
    b = Bebida()
    for i in cursor.fetchall():
        b.id = i[0]
        b.nome = i[1] 
        b.preco = i[3]      
        b.quantidade = i[2]
    conexao.commit()
    conexao.close()
    return b    

#################### SOBREMESA ##########################################

def salvar_sobremesa_db(nome, preco, quantidade):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO `SOBREMESAS` (`NOME`, `PRECO`, `QUANTIDADE`)" + 
    " VALUES ('{}', '{}', '{}')".format(nome, preco, quantidade))
    conexao.commit()
    conexao.close()


def listar_sobremesa_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
    cursor = conexao.cursor()
    cursor.execute("select * from `SOBREMESAS`") 
    listar_sobremesa = []
    for i in cursor.fetchall():
        nova_sobremesa = Sobremesa()
        nova_sobremesa.id = i[0]
        nova_sobremesa.nome = i[1] 
        nova_sobremesa.preco = i[3]      
        nova_sobremesa.quantidade = i[2]
        listar_sobremesa.append(nova_sobremesa)
    
    conexao.close()
    return listar_sobremesa

def editar_sobremesa_db(id, nome, quantidade, preco):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
    cursor = conexao.cursor()
    cursor.execute("UPDATE `SOBREMESAS` SET `NOME` = '{}', `PRECO` = {}, `QUANTIDADE` = {} WHERE `ID` = {}"
    .format(nome, quantidade, preco , id))
    conexao.commit()
    conexao.close()   

def deletar_sobremesa(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM `SOBREMESAS` WHERE `ID`={}".format(id))
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
        s.preco = i[3]
        s.quantidade = i[2]
    conexao.commit()
    conexao.close()
    return s                


################################-ROTAS-############################################################

app= Flask(__name__)
pagina_nome = 'HB FOOD'

@app.route('/')
def inicio():
    return render_template('home.html', pagina_nome = pagina_nome)

@app.route('/home')
def principal():
    
    return render_template('home.html', pagina_nome = pagina_nome)

@app.route('/prato')
def comida():
    guto = listar_prato_db()
    return render_template('prato.html', pagina_nome = pagina_nome, lista_html = guto)

@app.route('/prato/salvar', methods = ['POST'])
def salvar_prato():
    nome = request.form['item'] 
    preco = request.form['preco']
    quantidade = request.form['quant']
    novo_prato = Sobremesa()
    novo_prato.nome = nome
    novo_prato.preco = preco
    novo_prato.quantidade = quantidade
    salvar_prato_db(novo_prato.nome, novo_prato.preco, novo_prato.quantidade)    
    return redirect('/prato')

@app.route('/deletar/prato')
def apagar_prato():
    id = request.args['id']
    deletar_prato(id)
    return redirect('/prato')

@app.route('/alterar/prato')
def alterar_prato():
    id = request.args['id']
    alteracao_prato = buscar_em_prato(id)
    return render_template('alterar_prato.html', alterar_prato = alteracao_prato)    

@app.route('/alterar/salvar/prato', methods=['POST'])
def salvar_alteracao_prato():
    id = request.form['id']
    nome = request.form['nome']     
    preco = request.form['preco']
    quantidade = request.form['quantidade'] 
    editar_prato_db(id, nome, preco, quantidade)
    return redirect('/prato') 


@app.route('/bebida')
def babida():
    lenda = listar_bebida_db()
    return render_template('bebida.html', pagina_nome = pagina_nome, listas_html = lenda)

@app.route('/bebida/salvar', methods = ['POST'])
def salvar_bebida():
    nome = request.form['item'] 
    preco = request.form['preco']
    quantidade = request.form['quant']
    nova_bebida = Bebida()
    nova_bebida.nome = nome
    nova_bebida.preco = preco
    nova_bebida.quantidade = quantidade
    salvar_bebida_db(nova_bebida.nome, nova_bebida.preco, nova_bebida.quantidade)    
    return redirect('/bebida')

@app.route('/deletar/bebida/')
def apagar_bebida():
    id = request.args['id']
    deletar_bebida(id)
    return redirect('/bebida')

@app.route('/alterar/bebida/')
def alterar_bebida():
    id = request.args['id']
    alteracao_bebida = buscar_em_bebida(id)
    return render_template('alterar_bebida.html', alterar_bebida = alteracao_bebida)    

@app.route('/alterar/salvar/bebida', methods=['POST'])
def salvar_alteracao_bebida():
    id = request.form['id']
    nome = request.form['nome']     
    preco = request.form['preco']
    quantidade = request.form['quantidade'] 
    editar_bebida_db(id, nome,preco, quantidade)

    return redirect('/bebida') 


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
    preco = request.form['preco']
    quantidade = request.form['quantidade'] 
    editar_sobremesa_db(id, nome, preco, quantidade)
    return redirect('/sobremesa') 


app.run(debug=True)
