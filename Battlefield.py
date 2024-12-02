""""The game will be played on a single 7x7 field. First of all, the computer asks for the name of the player. 
Then the program secretly from the player must place ships on the field: 1 ship of 3 squares, 2 ships of 2 squares and 4 ships of 1 square. 
The ships must not touch each other, even at their corners. Example of the arrangement of ships:



After that, the battle itself begins. An empty field is displayed on the console. The player enters the coordinates of the shot. 
If he misses, this cell should be marked as "miss". In case of a hit, this cell should be marked as "hit". If the ship is completely sunk, this automatically should be shown.
The marks on the field "miss", "hit", "sunk", as well as the empty cell - all of this needs to be beautifully designed. 
But how? The programmer of this game should think about this aspect.
After each action, the screen must be cleared. Thus, each time the playing field will be displayed on a clean screen, instead of crawling down the console.
After the victory, the number of shots that the player made is displayed on the screen. The computer must also ask the player whether to start another game. 
If the player agrees, the game is repeated from the beginning. If the player refuses, then a sorted list of all players from best to worst is displayed on the screen and the program ends.                  

Bonus improvement (optional): it is required to make it so that not two digits are entered as the coordinates of the shot, but a letter and a digit. 
For example, instead of (2;5), it should be entered (B;5).

Bonus improvement (optional): do not allow the player to shoot out of the battlefield as well as at cells that have been shot at before.

"""

"""asking player's name"""
"""generating ships"""
"""the game itself"""
""""""
import random
        

def name(name):
    name=input('Please enter your name: ')
    return name
    
def clear():
    a = [['~' for k in range(8)] for k in range(8)]
    for i in range(8):
        a[i][0]=chr(64+i)
        for j in range(8):
            a[0][0]=' '
            a[0][j]=j
    return print('\n'.join(' '.join(str(a[i][j]) for j in range(8)) for i in range(8)))
  

def generate_ships():
    board=[[' ' for k in range(8)] for k in range(8)]
    ships=[3, 2, 2, 1, 1, 1, 1]

    
    for size in ships:
        alignment=random.choice([True, False])#True=horizontal / False=vertical
        if alignment==True:
            for i in range(size):
                x=random.sample(1, 8)
                y=random.sample(1, 8)
                board[x+i][y]=='sh'
                
                    


