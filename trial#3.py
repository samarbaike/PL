import random

# Function to clear and print the battleboard
def clear():
    """
    Creates and prints an empty 8x8 battleboard with labeled rows and columns.
    """
    a = [['~' for _ in range(8)] for _ in range(8)]
    a.insert(0, [' '] + [str(i) for i in range(1, 8)])  # Add column labels
    for i in range(1, 8):
        a[i].insert(0, chr(64 + i))  # Add row labels
    print("\n".join(" ".join(str(cell) for cell in row) for row in a))

# Function to generate ships on the board
def generate_ships():
    """
    Randomly places ships on a 7x7 battlefield.
    Ships cannot touch each other, even at corners.
    """
    board = [[' ' for _ in range(7)] for _ in range(7)]  # Create a 7x7 board
    ships = [3, 2, 2, 1, 1, 1, 1]  # List of ship sizes

    def can_place_ship(board, x, y, size, alignment):
        """
        Checks if a ship can be placed starting at (x, y) with the given size
        and alignment ('h' for horizontal, 'v' for vertical).
        """
        for i in range(size):
            # Calculate current ship segment position
            nx, ny = (x + i, y) if alignment == 'v' else (x, y + i)
            if nx >= 7 or ny >= 7 or board[nx][ny] != ' ':  # Out of bounds or already occupied
                return False

            # Check adjacent cells for conflicts
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    adj_x, adj_y = nx + dx, ny + dy
                    if 0 <= adj_x < 7 and 0 <= adj_y < 7 and board[adj_x][adj_y] == 'S':
                        return False
        return True

    for size in ships:
        placed = False
        while not placed:
            x, y = random.randint(0, 6), random.randint(0, 6)
            alignment = random.choice(['h', 'v'])
            if can_place_ship(board, x, y, size, alignment):
                for i in range(size):
                    nx, ny = (x + i, y) if alignment == 'v' else (x, y + i)
                    board[nx][ny] = 'S'
                placed = True

    return board

# Function to print the visible field
def print_visible_board(board):
    """
    Prints the player's visible battleboard with labeled rows and columns.
    """
    print("  " + " ".join(str(i) for i in range(1, 8)))
    for i, row in enumerate(board):
        print(chr(65 + i) + " " + " ".join(row))

# Function to handle player's turn
def player_turn(hidden_board, visible_board):
    """
    Handles player's shot and updates the visible and hidden boards.
    """
    while True:
        shot = input("Enter your shot (e.g., A3): ").strip().upper()
        if len(shot) == 2 and shot[0] in "ABCDEFG" and shot[1].isdigit():
            x, y = ord(shot[0]) - 65, int(shot[1]) - 1
            if 0 <= x < 7 and 0 <= y < 7:
                if visible_board[x][y] != '~':  # Check if the cell is already shot
                    print("You already shot there. Try again.")
                else:
                    if hidden_board[x][y] == 'S':  # Hit
                        visible_board[x][y] = 'X'
                        hidden_board[x][y] = 'X'
                        print("Hit!")
                        return True
                    else:  # Miss
                        visible_board[x][y] = 'O'
                        print("Miss!")
                        return False
        print("Invalid input. Please try again.")

# Function to check if all ships are sunk
def all_ships_sunk(hidden_board):
    """
    Returns True if all ships have been sunk.
    """
    for row in hidden_board:
        if 'S' in row:
            return False
    return True

# Main game function
def play_game():
    """
    Main game loop. Initializes boards and handles game progression.
    """
    print("Welcome to Battleship!")
    name = input("Please enter your name: ")

    # Initialize boards
    hidden_board = generate_ships()
    visible_board = [['~' for _ in range(7)] for _ in range(7)]
    shots = 0

    # Game loop
    while not all_ships_sunk(hidden_board):
        print_visible_board(visible_board)
        print(f"{name}, take your shot!")
        if player_turn(hidden_board, visible_board):
            print("Great! Keep going.")
        else:
            print("Better luck next time.")
        shots += 1

    print(f"Congratulations, {name}! You sunk all the ships in {shots} shots!")

# Run the game
play_game()
