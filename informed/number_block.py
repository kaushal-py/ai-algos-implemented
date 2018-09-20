import random
import os

MAX_STEP = 3
WORLD_SIZE = 5
WORLD = list(range(WORLD_SIZE * WORLD_SIZE))

UP = 8
DOWN = 2
LEFT = 4
RIGHT = 6

for i in range(WORLD_SIZE*WORLD_SIZE):
    WORLD[i] = random.randint(1, 3)

WORLD[WORLD_SIZE*WORLD_SIZE -1] = 'G'

WORLD = [WORLD[i:i+WORLD_SIZE] for i in range(0, len(WORLD), WORLD_SIZE)]

start_location = [0, 0]


def print_grid(location):

    print("-"*16*WORLD_SIZE)

    for i in range(WORLD_SIZE):
        for j in range(WORLD_SIZE):
            if [i,j] == location:
                print("|\t", WORLD[i][j], "*", end='\t')
            else:
                print("|\t", WORLD[i][j], end='\t')
            
        print("|")
        print("-"*16*WORLD_SIZE)

print_grid(start_location)

def get_possible_moves(location):

    moves = []

    if location[0] - WORLD[location[0]][location[1]] >= 0:
        moves.append(UP)
    if location[0] + WORLD[location[0]][location[1]] < WORLD_SIZE:
        moves.append(DOWN)
    if location[1] - WORLD[location[0]][location[1]] >= 0:
        moves.append(LEFT)
    if location[1] + WORLD[location[0]][location[1]] < WORLD_SIZE:
        moves.append(RIGHT)

    return moves

def move(location, direction):

    if direction not in get_possible_moves(location):
        return location

    if direction == UP:
        location[0] -= WORLD[location[0]][location[1]]
    elif direction == DOWN:
        location[0] += WORLD[location[0]][location[1]]
    elif direction == LEFT:
        location[1] -= WORLD[location[0]][location[1]]
    elif direction == RIGHT:
        location[1] += WORLD[location[0]][location[1]]

    return location

def simulate():

    current_location = start_location
    
    os.system('clear')
    while(True):
        print_grid(current_location)
        direction = int(input("Enter direction to move: "))
        os.system('clear')
        # print(current_location)
        current_location = move(current_location, direction)
        
        if current_location[0] == WORLD_SIZE-1 and current_location[1] == WORLD_SIZE -1 :
            print("Goal reached!")
            break

simulate()