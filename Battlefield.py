#1 asking player's name
#2 generating places for ships 1 ship of 3 squares, 2 ships of 2 squares, 4 ships of 1 square wihtout them touching each other
#3 the process of battling, 

import os
import random
import string


def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def create_empty_board(size):
    """Creates an empty game board."""
    return [['~' for _ in range(size)] for _ in range(size)]


def display_board(board, hidden=False):
    """Displays the game board."""
    clear_screen()
    print("  " + " ".join(string.ascii_uppercase[:len(board)]))  # Column labels
    for i, row in enumerate(board):
        print(f"{i + 1} " + " ".join(cell if not hidden or cell in ['~', 'M', 'H', 'S'] else '~' for cell in row))


def place_ships_randomly(board, ships):
    """Randomly places ships on the board."""
    directions = [(0, 1), (1, 0)]  # Horizontal, Vertical
    for ship_size in ships:
        placed = False
        while not placed:
            direction = random.choice(directions)
            start_row = random.randint(0, len(board) - 1)
            start_col = random.randint(0, len(board) - 1)
            ship_coordinates = []
            for i in range(ship_size):
                row = start_row + direction[0] * i
                col = start_col + direction[1] * i
                if 0 <= row < len(board) and 0 <= col < len(board) and board[row][col] == '~':
                    ship_coordinates.append((row, col))
                else:
                    break
            if len(ship_coordinates) == ship_size and no_ship_conflict(board, ship_coordinates):
                for row, col in ship_coordinates:
                    board[row][col] = 'S'
                placed = True


def no_ship_conflict(board, ship_coordinates):
    """Checks if a ship conflicts with existing ships."""
    for row, col in ship_coordinates:
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                nr, nc = row + dr, col + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board) and board[nr][nc] == 'S':
                    return False
    return True


def parse_shot_input(input_str, size):
    """Parses shot input and converts to board coordinates."""
    try:
        col = string.ascii_uppercase.index(input_str[0].upper())
        row = int(input_str[1:]) - 1
        if 0 <= row < size and 0 <= col < size:
            return row, col
    except (ValueError, IndexError):
        pass
    return None


def all_ships_sunk(board):
    """Checks if all ships are sunk."""
    return all(cell != 'S' for row in board for cell in row)


def play_game():
    """Main function to play a single game."""
    size = 7
    ships = [3, 2, 2, 1, 1, 1, 1]
    player_name = input("Enter your name: ")

    # Initialize boards
    player_board = create_empty_board(size)
    computer_board = create_empty_board(size)
    place_ships_randomly(computer_board, ships)

    # Game loop
    shots_fired = 0
    while True:
        display_board(player_board)
        shot = input("Enter your shot (e.g., B5): ").strip()
        coordinates = parse_shot_input(shot, size)

        if not coordinates:
            print("Invalid input. Try again.")
            continue

        row, col = coordinates
        if player_board[row][col] in ['H', 'M']:
            print("You already shot here. Try again.")
            continue

        shots_fired += 1
        if computer_board[row][col] == 'S':
            print("Hit!")
            player_board[row][col] = 'H'
            computer_board[row][col] = 'H'
            if check_and_sink_ship(player_board, computer_board, row, col):
                print("You sunk a ship!")
        else:
            print("Miss!")
            player_board[row][col] = 'M'

        if all_ships_sunk(computer_board):
            display_board(player_board)
            print(f"Congratulations, {player_name}! You won in {shots_fired} shots.")
            break


def check_and_sink_ship(player_board, computer_board, row, col):
    """Checks if a ship is completely sunk and marks it."""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dr, dc in directions:
        r, c = row, col
        while 0 <= r < len(computer_board) and 0 <= c < len(computer_board):
            if computer_board[r][c] == 'S':
                return False
            if computer_board[r][c] == '~':
                break
            r += dr
            c += dc
    return True


def main():
    """Main menu for the game."""
    scores = []
    while True:
        play_game()
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay != 'yes':
            print("Thanks for playing! Here are the scores:")
            for name, shots in sorted(scores, key=lambda x: x[1]):
                print(f"{name}: {shots} shots")
            break


if __name__ == "__main__":
    main()


