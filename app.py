from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Tutorial')
def tutorial():

    return render_template('tutorial.html') 
    #return 'This is the tutorial'

@app.route('/PVE')
def PVE():
    return "this is the pve"

@app.route('/PVP')
def PVP():
    return "this is the pvp"

@app.route('/Multiplayer')
def Multiplayer():
    return "this is multiplayer"

if __name__ == 'main':
    app.run(debug=True)