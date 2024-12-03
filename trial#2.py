import random

# Initialize the board
board = [['~' for _ in range(8)] for _ in range(8)]
ships = [3, 2, 2, 1, 1, 1, 1]

#function to check if a ship and its surrounding area are clear
def can_place_ship(board, x, y, size, horizontal):
    sur = [-1, 0, 1]
    for i in range(size):
        if horizontal:
            new_x, new_y = x + i, y
        else:
            new_x, new_y = x, y + i

        # Check if the ship part is out of bounds or overlaps another ship
        if new_x >= 8 or new_y >= 8 or board[new_x][new_y] != '~':
            return False

        # Checking the surrounding cells
        for ch_x in sur:
            for ch_y in sur:
                adj_x, adj_y = new_x + ch_x, new_y + ch_y
                if 0 <= adj_x < 8 and 0 <= adj_y < 8:
                    if board[adj_x][adj_y] != '~':
                        return False
    return True


for size in ships:
    placed = False
    while not placed:
        alignment = random.choice(['h', 'v'])  # 'h' = horizontal, 'v' = vertical
        x = random.randint(1, 8)
        y = random.randint(1, 8)

       
        if can_place_ship(board, x, y, size, alignment == 'h'):
            for i in range(size):
                if alignment == 'h': 
                    new_x, new_y = x + i, y
                else:  
                    new_x, new_y = x, y + i
                board[new_x][new_y] = 's'  
            placed = True

# Display the board
for row in board:
    print(' '.join(row))

