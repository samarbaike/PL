import random

# Number of random coordinates to generate
num_coordinates = 5

# Generate a list of random coordinates
coordinates = [(random.randint(0, 7), random.randint(0, 7)) for _ in range(num_coordinates)]

print("Random coordinates:", coordinates)

