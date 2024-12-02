import random

# Generate all possible coordinates in an 8x8 grid
all_coordinates = [(row, col) for row in range(1, 7) for col in range(1, 7)]

# Shuffle the coordinates and select as many as you need
unique_coordinates = random.sample(all_coordinates, 4)  # Adjust 'k' as needed

print("Non-repeating random coordinates:", unique_coordinates)
