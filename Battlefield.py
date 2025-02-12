""""The game will be played on a single 7x7 field. First of all, the computer asks for the name of the player. 
Then the program secretly from the player must place ships on the field: 1 ship of 3 squares, 2 ships of 2 squares and 4 ships of 1 square. 
The ships must not touch each other, even at their corners. Example of the arrangement of ships:



After that, the battle itself begins. An empty field is displayed on the console. The player enters the coordinates of the shot. 
If he misses, this cell should be marked as "miss". In case of a hit, this cell should be marked as "hit". If the ship is completely sunk, this automatically should be shown.
The marks on the field "miss", "hit", "sunk", as well as the empty cell - all of this needs to be beautifully designed. 
But how? The programmer of this game should think about this aspect.
After each action, the screen must be cleared. Thus, each time the playing field will be displayed on a clean screen, instead of crawling down the console.
After the victory, the number of shots that the player made is displayed on the screen. The computer must also ask the player whether to start another game. 
If the player agrees, the game is repeated from the beginning. If the player refuses, then a sorted list of all players from best to worst is displayed on the screen and the 
program ends.                  

Bonus improvement (optional): it is required to make it so that not two digits are entered as the coordinates of the shot, but a letter and a digit. 
For example, instead of (2;5), it should be entered (B;5).

Bonus improvement (optional): do not allow the player to shoot out of the battlefield as well as at cells that have been shot at before.

"""

"""asking player's name"""
"""generating ships"""
"""the game itself"""
""""""
import random
import os
        



#creating battleboard    
def clear():
    default = [['~' for k in range(8)] for k in range(8)]
    for i in range(8):
        default[i][0]=chr(64+i)
        for j in range(8):
            default[0][0]=' '
            default[0][j]=j
    return 


def clear_terminal():
    """
    Clears the terminal screen for a fresh display.
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # For Windows ('cls') and others ('clear')

#generating ships
def generate_ships():
    b = [[' ' for _ in range(9)] for _ in range(9)]
    ships = [3, 2, 2, 1, 1, 1, 1]


    def can_place_ship(back, x, y, size, alignment):
        sur=[-1, 0, 1]
        for i in range(size):
            if alignment == 'h':
                new_x, new_y = x+i, y
                if new_x >= 8 or new_y >= 8 or back[new_x][new_y] != ' ':
                    return False
            else:
                new_x, new_y = x, y+i
                if new_x >= 8 or new_y >= 8 or back[new_x][new_y] != ' ':
                    return False
            for ch_x in sur:
                for ch_y in sur:
                    adj_x, adj_y = new_x + ch_x, new_y + ch_y
                    if 0 <= adj_x < 8 and 0 <= adj_y < 8 and back[adj_x][adj_y] != ' ':
                        return False
        return True


    for size in ships:
        place=False
        while not place:
            alignment = random.choice(['h', 'v'])
            if alignment=='h':  # True=horizontal / False=vertical
                x = random.randint(1, 8)
                y = random.randint(1, 8)
            else:
                x = random.randint(1, 8)
                y = random.randint(1, 8)
            
            if can_place_ship(b, x, y, size, alignment):
                for i in range(size):
                    if alignment=='h':
                        new_x, new_y=x+i, y
                        b[new_x][new_y]='s' 
                    else:
                        new_x, new_y=x, y+i
                        b[new_x][new_y]='s'
                place=True
    return b

def user_board():
    f = [['~' for k in range(8)] for k in range(8)]
    for i in range(8):
        f[i][0]=str(chr(64+i))
        for j in range(8):
            f[0][0]=' '
            f[0][j]=str(j)
    return f

def all_ships_sunk(back):
    for row in back:
        if 's' in row:
            return False
    return True




def user_input(back, front):

    def totally_sunk(x, y, back):
        sur=[(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for ch_x, ch_y in sur:
            adj_x, adj_y = x + ch_x, y + ch_y
            if 0 <= adj_x < 8 and 0 <= adj_y < 8 and back[adj_x][adj_y] == 's':
                return False
        return True
    
    def sink_other_parts(x, y, back, front):
        sur=[(-1, 0), (0, -1), (0, 1), (1, 0)]
        for chx, chy in sur:
            arx, ary = x + chx, y + chy
            arrx, arry = arx + chx, ary + chy
            if 0 <= arrx < 8 and 0 <= arry < 8 and back[arx][ary] == 'O' and back[arrx][arry]=='s':
                front[arx][ary]='●'
            elif 0 <= arrx < 8 and 0 <= arry < 8 and back[arx][ary] == 'O' and back[arrx][arry]==' ':
                front[arx][ary]='●'
            elif 0 <= arrx < 8 and 0 <= arry < 8 and back[arx][ary] == 'O' and back[arrx][arry]=='O':
                front[arx][ary]='●'
                front[arrx][arry]='●'
        return front

   



    result=" "
    while True:
        print(f"\n{result}\n")
        shot = input('shot coordinates: ').strip().upper()
        if len(shot)==2 and shot[0] in 'ABCDEFG' and shot[1].isdigit():
            x, y= ord(shot[0])-64 , int(shot[1])
            if front[x][y] in ['O', 'X', '●']:
                print('you ALREADY SHOT there!')
                print('Try again')
                return True
            else: 
                if back[x][y]=='s':
                    if totally_sunk(x, y, back):
                        front[x][y]='●'
                        back[x][y]='O'
                        sink_other_parts(x, y, back, front)
                        result="let's gooo!"
                        return True
                    else:
                        front[x][y]='O'
                        back[x][y]='O'
                        sink_other_parts(x, y, back, front)
                        result='got it'
                        return True
                else:
                    front[x][y]='X'
                    print('miss')
                    result="missed. Think, bro, think"
                    return False
        else:
            print('Invalid input, try again')

    
        

def game(leaderboard):
    def find_max(list):
        max_number=list[0][0]
        for i in range(len(list)):
            if list[i][0] >= max_number:
                max_number=list[i][0]
                max_player=list[i]
        return max_player

    
    name=input('Enter your name: ')
    back=generate_ships()
    front=user_board()
    shots=0
    while not all_ships_sunk(back):
        clear_terminal()
        for row in front:
            print(' '.join(row))
        if user_input(back, front):
            print("Let's go! Keep that pace.")
        else: 
            print('Think, monki, think')
        shots+=1
    else:
        clear_terminal()
        print(f"Congrats, {name}! You sunk all the ships 'only' in {shots} shots :)")
        leaderboard.append((shots, name))
    

    question=input('Would like to start new round?(yes/no): ')
    if question=='yes':
        return game(leaderboard)
    elif question=='no':
        l=[]
        print('Leaderboard:')
        print(' ')
        for i in range(len(leaderboard)):
            n=find_max(leaderboard)
            l.append(n)
            leaderboard.remove(n)
            
        for row in l:
            print(' '.join(str(item) for item in row))

        
        print(' ')
        print(name, ', thanks, for playing the game!!!')
        print('hope you enjoyed it!')
        
    else:
        print('Invalid, respond using only "yes/no"')



leaderboard=[]
game(leaderboard)
