from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html', title = "Home page")

@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

@app.route('/user/<name>')
def getUser(name):
    return render_template('user.html', name=name)