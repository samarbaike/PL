import random

def generate_ships():
    board = [[' ' for _ in range(7)] for _ in range(7)]
    ships_to_place = [(3, 1), (2, 2), (1, 4)]  # (size, count)

    def can_place_ship(x, y, size, direction):
        dx, dy = (1, 0) if direction == 'H' else (0, 1)
        for i in range(size):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < 7 and 0 <= ny < 7) or board[ny][nx] != ' ':
                return False
            # Check surrounding cells for adjacent ships
            for xx in range(-1, 2):
                for yy in range(-1, 2):
                    sx, sy = nx + xx, ny + yy
                    if 0 <= sx < 7 and 0 <= sy < 7 and board[sy][sx] != ' ':
                        return False
        return True

    def place_ship(x, y, size, direction):
        dx, dy = (1, 0) if direction == 'H' else (0, 1)
        for i in range(size):
            nx, ny = x + i * dx, y + i * dy
            board[ny][nx] = 'S'

    for size, count in ships_to_place:
        for _ in range(count):
            while True:
                x, y = random.randint(0, 6), random.randint(0, 6)
                direction = random.choice(['H', 'V'])
                if can_place_ship(x, y, size, direction):
                    place_ship(x, y, size, direction)
                    break

    return board
for row in generate_ships():
    print(' '.join(row))
