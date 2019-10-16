from flask import Flask, render_template
from methods.comida import Comida
from methods.bebida import Bebida
from methods.sobremesa import Sobremesa
import MySQLdb

def listar_comida_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae14", passwd="grupo09", database="zuplae14")
    cursor = conexao.cursor()
    cursor.execute("select * from COMIDA") 
    listar_comida = []
    for i in cursor.fetchall():
        produto = Produto()
        produto.id = i[0]
        produto.nome = i[1]
        produto.descricao = i[2]
        produto.categoria_id = i[3]
        produto.estoque_id = i[4]
        listar_produto.append(produto)

    conexao.close()
    return listar_produto


pagina_nome = "Nome da pagina"


app = Flask(__name__)
@app.route('/')


def inicio():
    return render_template('/index.html', pagina_nome = pagina_nome)

@app.route('/login')
def login():
    return render_template('/login.html', pagina_nome = pagina_nome)

@app.route('/login/cadastro')
def cadastro():
    return render_template('/cadastro.html', pagina_nome = pagina_nome)


@app.route('/comida')
def comida():
    return render_template('/comida.html', pagina_nome = pagina_nome)

@app.route('/bebida')
def babida():
    return render_template('/bebida.html', pagina_nome = pagina_nome)

@app.route('/sobremesa')
def sobremesa():
    return render_template('/sobremesa.html', pagina_nome = pagina_nome)

@app.route('/pedido')
def pedido():
    return render_template('/pedido.html', pagina_nome = pagina_nome)


app.run()
