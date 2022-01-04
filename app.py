from flask import Flask, render_template
#First idea:
#from sites.Tutorial import tutorial_Site

#Second idea:
#with open('sites/Tutorial/tutorial.py') as f:
    #tutorial_site = f.read()
#this works but the problem is that the print() func prints it as well xD

app = Flask(__name__)
#app.register_blueprint(tutorial_Site)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Tutorial')
def tutorial():
    #First idea:
    #return tutorial_site
    #Second idea:
    #return render_template('tutorial.html') 
    return 'This is the tutorial'

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