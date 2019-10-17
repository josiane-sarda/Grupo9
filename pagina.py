from flask import Flask, render_template, request, redirect
import MySQLdb



pagina_nome = "HB FOOD"

app= Flask(__name__)
@app.route('/')
def inicio():
    return render_template('index.html', pagina_nome = pagina_nome)

@app.route('/login')
def login():
    return render_template('login.html', pagina_nome = pagina_nome)

@app.route('/login/cadastro')
def pedido():
    return render_template('pedido.html', pagina_nome = pagina_nome)


@app.route('/comida')
def comida():
    return render_template('comida.html', pagina_nome = pagina_nome)

@app.route('/bebida')
def babida():
    return render_template('bebida.html', pagina_nome = pagina_nome)

@app.route('/sobremesa')
def sobremesa():
    return render_template('sobremesa.html', pagina_nome = pagina_nome)

@app.route('/pedido')
def pedido():
    return render_template('pedido.html', pagina_nome = pagina_nome)


app.run()
