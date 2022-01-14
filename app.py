from flask import Flask, render_template
from jinja2 import Template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Tutorial')
def tutorial():
    return render_template('Tutorial/tutorial.html') 

@app.route('/PVE')
def PVE(board,winner,win,):
    board = [['-','-','-'],['-','-','-'],['-','-','-']]

    return render_template('PVE/pve.html')

@app.route('/PVP')
def PVP():
    return render_template('PVP/pvp.html')

@app.route('/Multiplayer')
def Multiplayer():
    return render_template('Multiplayer/multiplayer.html')

if __name__ == 'main':
    app.run(debug=True)