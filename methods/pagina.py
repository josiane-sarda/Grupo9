from flask import Flask, render_template
from comida import Comida
from bebida import Bebida
from sobremesa import Sobremesa


pagina_nome = "Nome da pagina"


app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template('index.html')


app.run()
