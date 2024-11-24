from random import sample
from random import randrange
distance = sample(range(1, 8), 3) 
weight = sample(range(1, 713), 3) 

while sum(weight) != 713:
    weight = [randrange (1, 300) for i in range(3)]

def relocate(current):
    
    new_locations = []
    for l in current:
        while True:
            new = randrange(1, 7)
            if new not in current and new not in new_locations:
                new_locations.append(new)
                break
    return new_locations

while True:
    g=[]
    for i in range(3):
        gues=int(input(f'Enter the location for box {i + 1} (1-7): '))
        g.append(gues)
        
    if g == distance:
        print("Congratulations! You found all the boxes.")
        print(f"Box weights: {weight}")
    
        if sum(weight) == 713:
            print("The total weight is correct: 713 kg.")
            break
        else:
            print("The total weight does not match 713 kg. Try again!")
    else:
        print("Wrong guesses! The boxes have relocated.")
        distance = relocate(distance, previous)
        previous.update(distance)   
