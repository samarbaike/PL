from random import randrange
distance = [randrange (1, 7) for i in range(3)]
weight = [randrange (1, 300) for i in range(3)]

while sum(weight) != 713:
    weight = [randrange (1, 300) for i in range(3)]

previous = set(distance)

def relocate(current, used):
    
    new_locations = []
    for l in current:
        while True:
            new = randrange(1, 7)
            if new != l and new not in used:
                new_locations.append(new)
                used.add(new)  # Add to the set of used locations
                break
    return new_locations

while True:
    g=[]
    for i in range(3):
        gues=int(input(f'Enter the location for box {i + 1} (1-7): '))
        g.append(guess)