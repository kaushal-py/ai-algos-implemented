import random
import copy
import time

DEBUG = False
GRID_SIZE = 3

UP = 0
LEFT = 1
RIGHT = 2
DOWN = 3

USER_INPUT = True
INITIAL_STATE = list(range(GRID_SIZE*GRID_SIZE))


if USER_INPUT:
    INITIAL_STATE = [int(x) for x in input("Enter initial state: ").split()]
else:
    random.shuffle(INITIAL_STATE)

INITIAL_STATE = [INITIAL_STATE[i:i+GRID_SIZE] for i in range(0, len(INITIAL_STATE), GRID_SIZE)]

print(INITIAL_STATE)

def search_for_blank(state):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if state[i][j] == GRID_SIZE*GRID_SIZE -1:
                return (i,j)
    
    raise IndexError

def printd(*args, **kwargs):
    if DEBUG == True:
        print(args)

printd(search_for_blank(INITIAL_STATE))

def move(state, direction):

    next_state = copy.deepcopy(state)
    blank = search_for_blank(state)

    if direction == UP:
            
            if blank[0] != 0:
                next_state[blank[0]][blank[1]], next_state[blank[0] -1 ][blank[1]] = next_state[blank[0] -1 ][blank[1]], next_state[blank[0]][blank[1]] 

    if direction == DOWN:
        
        if blank[0] != GRID_SIZE - 1:
            next_state[blank[0]][blank[1]], next_state[blank[0] +1 ][blank[1]] = next_state[blank[0] +1 ][blank[1]], next_state[blank[0]][blank[1]] 

    if direction == LEFT:
        
        if blank[1] != 0:
            next_state[blank[0]][blank[1]], next_state[blank[0]][blank[1] -1 ] = next_state[blank[0]][blank[1] -1 ], next_state[blank[0]][blank[1]] 

    if direction == RIGHT:
        
        if blank[1] != GRID_SIZE -1:
            next_state[blank[0]][blank[1]], next_state[blank[0]][blank[1] +1 ] = next_state[blank[0]][blank[1] +1 ], next_state[blank[0]][blank[1]] 

    return next_state

printd(move(INITIAL_STATE, UP))
printd(move(INITIAL_STATE, DOWN))
printd(move(INITIAL_STATE, LEFT))
printd(move(INITIAL_STATE, RIGHT))

def calc_hash(state):
    hash_string = ""

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            hash_string += str(state[i][j]) + " "
    
    return hash_string

def goal_test(state):
    index = 0

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if state[i][j] != index:
                return False
            index += 1
    
    return True

printd(goal_test(INITIAL_STATE))

def ucs():

    queue = []
    visited_states = set()

    queue.append(INITIAL_STATE)
    visited_states.add(calc_hash(INITIAL_STATE))

    iteration = 0
    flag = False

    while len(queue) != 0:

        u_state = queue.pop(0)
        visited_states.add(calc_hash(u_state))

        if goal_test(u_state):
            flag = True
            break

        for direction in [UP, DOWN, LEFT, RIGHT]:

            neighbour = move(u_state, direction)
            if calc_hash(neighbour) not in visited_states:
                queue.append(neighbour)
                visited_states.add(calc_hash(neighbour))            

        iteration += 1
        print("States visited :", iteration)

    if flag:
        print("YAY! Goal reached")
    else:
        print("Could not find goal")

ucs()