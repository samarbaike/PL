import random

def generate_ships():
    b = [['~' for _ in range(10)] for _ in range(10)]
    ships = [3, 2, 2, 1, 1, 1, 1]


    def can_place_ship(back, x, y, size, alignment):
        sur=[-1, 0, 1]
        for i in range(size):
            if alignment == 'h':
                new_x, new_y = x+i, y
                if new_x >= 8 or new_y >= 8 or back[new_x][new_y] != '~':
                    return False
            else:
                new_x, new_y = x, y+i
                if new_x >= 8 or new_y >= 8 or back[new_x][new_y] != '~':
                    return False
            for ch_x in sur:
                for ch_y in sur:
                    adj_x, adj_y = new_x + ch_x, new_y + ch_y
                    if 0 <= adj_x < 8 and 0 <= adj_y < 8 and back[adj_x][adj_y] != '~':
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

g = generate_ships()
for row in g:
    print(' '.join(row))