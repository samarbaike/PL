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
        
    if guesses == box_distances:
        print("Congratulations! You found all the boxes.")
        print(f"Box weights: {box_weights}")
    
        if sum(box_weights) == 713:
            print("The total weight is correct: 713 kg.")
            break
        else:
            print("The total weight does not match 713 kg. Try again!")
            weight = [randrange (1, 300) for i in range(3)]
    else:
        print("Wrong guesses! The boxes have relocated.")
        distance = relocate(distance, previous)
