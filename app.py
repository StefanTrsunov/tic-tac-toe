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
    #here it needs to return the tutroial.py file which is in sites/Tutorial/tutorial.py
    #First idea:
    #return render_template('sites/Tutorial/tutorial.html')
    #Second idea:
    #return tutorial_site
    return 'This is the tutorial'

@app.route('/PVE')
def PVE():
    #here it needs to return the pve.py file which is in sites/PVE/pve.py
    return "this is the pve"

@app.route('/PVP')
def PVP():
    #here it needs to return the pvp.py file which is in sites/PVP/pvp.py
    return "this is the pvp"

@app.route('/Multiplayer')
def Multiplayer():
    #here it needs to return the multiplayer.py(or other file) file which is in sites/Tutorial/tutorial.py
    return "this is multiplayer"

if __name__ == 'main':
    app.run(debug=True)