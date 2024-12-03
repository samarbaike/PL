import random
def generate_ships():
    board = [[' ' for _ in range(8)] for _ in range(8)]
    ships = [3, 2, 2, 1, 1, 1, 1]


    def can_place_ship(board, x, y, size, h):
        sur=[-1, 0, 1]
        for i in range(size):
            if alignment == 'h':
                new_x, new_y = x+i, y
                if new_x >= 8 or new_y >= 8 or board[new_x][new_y] != ' ':
                    return False
            else:
                new_x, new_y = x, y+i
                if new_x >= 8 or new_y >= 8 or board[new_x][new_y] != ' ':
                    return False
            for ch_x in sur:
                for ch_y in sur:
                    adj_x, adj_y = new_x + ch_x, new_y + ch_y
                    if 0 <= adj_x < 8 and 0 <= adj_y < 8 and board[adj_x][adj_y] != ' ':
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
            
            if can_place_ship(board, x, y, size, alignment):
                for i in range(size):
                    if alignment=='h':
                        new_x, new_y=x+i, y
                        board[new_x][new_y]='s' 
                    else:
                        new_x, new_y=x, y+i
                        board[new_x][new_y]='s'
                place=True
    return board

def print_visible_board(board):
    """
    Prints the player's visible battleboard with labeled rows and columns.
    """
    print("  " + " ".join(str(i) for i in range(1, 8)))
    for i, row in enumerate(board):
        print(chr(65 + i) + " " + " ".join(row))
    return
generate_ships()
print_visible_board(board)