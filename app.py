from flask import Flask, render_template
from game.game import displayPositions,logic

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Tutorial')
def tutorial():
    return render_template('Tutorial/tutorial.html') 

@app.route('/PVE')
def PVE():
    return render_template('PVE/pve.html')

@app.route('/PVP')
def PVP():
    def game():
        board = [['-','-','-'],['-','-','-'],['-','-','-']]
        win = False
        winner = None
        positions = [1,2,3,4,5,6,7,8,9]
        turn = 'X'
        count = 0

        while not win:
            user_choise = int(input('Select a position: '))
            if user_choise in positions:
                displayPositions(turn, user_choise)
                count += 1
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
                positions.remove(user_choise)
                logic(board)

                if win:
                    print(f"{winner} is the winner")
                    break
            else:
                print("Invalid Position")
                continue
            if count == 9:
                print('Game draw')
                break
        return game()
    return render_template('PVP/pvp.html', game=game())

@app.route('/Multiplayer')
def Multiplayer():
    return render_template('Multiplayer/multiplayer.html')

if __name__ == 'main':
    app.run(debug=True)