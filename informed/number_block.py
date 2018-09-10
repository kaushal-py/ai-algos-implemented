import random

MAX_STEP = 3
WORLD_SIZE = 5
WORLD = list(range(WORLD_SIZE * WORLD_SIZE))

for i in range(WORLD_SIZE*WORLD_SIZE):
    WORLD[i] = random.randint(1, 3)

WORLD[WORLD_SIZE*WORLD_SIZE -1] = 'G'

WORLD = [WORLD[i:i+WORLD_SIZE] for i in range(0, len(WORLD), WORLD_SIZE)]

current_location = [0, 0]


def print_grid():

    print("-"*16*WORLD_SIZE)

    for i in range(WORLD_SIZE):
        for j in range(WORLD_SIZE):
            if [i,j] == current_location:
                print("|\t", WORLD[i][j], "*", end='\t')
            else:
                print("|\t", WORLD[i][j], end='\t')
            
        print("|")
        print("-"*16*WORLD_SIZE)

print_grid()
