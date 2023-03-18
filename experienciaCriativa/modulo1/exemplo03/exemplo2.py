from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def index():    
    return render_template('home.html')

@app.route('/pedidosFor')
def orders()
    pedidos = ["Combo 1, comanda 2","Executivo 2, comanda 3",
    "Refri laranja, comanda 134","Cerveja, comanda 12", "Batata Frita, comanda 14"]

    return render_template('orders.html', orders = pedidos)

if __name__  == '__main__':
    app.run()   