from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/tienda')
def tienda():
    return render_template('tienda.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)
