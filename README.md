# tic-tac-toe
Building a website where you can play TIC TAC TOE with your friends


# Starting up the app

first create a .env file:
$ virtualenv env

activate the env file:
$ source env/bin/activate

install the requirements:
$ pip install -r requirements.txt

the final step is to just run the app:
$ flask run


# Exporting ENV variables

$ export FLASK_APP=wsgi.py
$ source .env
$ export $(cut -d= -f1 .env)