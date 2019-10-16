from flask import Flask, render_template
from comida import Comida
from bebida import Bebida
from sobremesa import Sobremesa
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
    return render_template('index.html')


app.run()
