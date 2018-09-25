import random
import os
import heapq 
import copy

MAX_STEP = 3
WORLD_SIZE = 5
WORLD = list(range(WORLD_SIZE * WORLD_SIZE))

UP = 8
DOWN = 2
LEFT = 4
RIGHT = 6
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

# A max int value for heuristic, i.e unreachable state.
INFINITY = WORLD_SIZE*WORLD_SIZE + 1

# instead of calculating the value dynamically, which is asymtotically slower.
H_MEM = [[INFINITY for _ in range(WORLD_SIZE)] for _ in range(WORLD_SIZE)]
H_MEM[WORLD_SIZE-1][WORLD_SIZE-1] = 0

start_location = [0, 0]


def generate_hueristics():

    global H_MEM, INFINITY, WORLD, WORLD_SIZE

    # instead of calculating the value dynamically, which is asymtotically slower.
    H_MEM = [[INFINITY for _ in range(WORLD_SIZE)] for _ in range(WORLD_SIZE)]
    H_MEM[WORLD_SIZE-1][WORLD_SIZE-1] = 0
    
    for i in range(WORLD_SIZE):
        for j in range(WORLD_SIZE):
            
            for k in range(WORLD_SIZE):
                for l in range(WORLD_SIZE):
                    
                    if H_MEM[k][l] == INFINITY:
                        
                        for direction in DIRECTIONS:

                            neigh_location = move([k,l], direction)

                            if neigh_location != [k,l]:
                                neigh_heuristic = H_MEM[neigh_location[0]][neigh_location[1]]

                                if neigh_heuristic != INFINITY:
                                    H_MEM[k][l] = neigh_heuristic+1
    
    if H_MEM[0][0] < INFINITY:
        return True
    else:
        return False


def generate_world():

    global WORLD, WORLD_SIZE

    WORLD = list(range(WORLD_SIZE * WORLD_SIZE))

    for i in range(WORLD_SIZE*WORLD_SIZE):
        WORLD[i] = random.randint(1, 3)

    WORLD[WORLD_SIZE*WORLD_SIZE -1] = 'G'

    WORLD = [WORLD[i:i+WORLD_SIZE] for i in range(0, len(WORLD), WORLD_SIZE)]

    if not generate_hueristics():
        generate_world()



def print_grid(location):

    global WORLD, WORLD_SIZE

    print("-"*16*WORLD_SIZE)

    for i in range(WORLD_SIZE):
        for j in range(WORLD_SIZE):
            if [i,j] == location:
                print("|\t", WORLD[i][j], "*", end='\t')
            else:
                print("|\t", WORLD[i][j], end='\t')
            
        print("|")
        print("-"*16*WORLD_SIZE)



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


def move(curr_location, direction):

    location = copy.deepcopy(curr_location)

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


def  a_star():
    
    queue = []

    heapq.heappush( queue, (1+H_MEM[0][0], start_location, 1) )

    states_visited = []
    
    while( len(queue) != 0):

        current_element = heapq.heappop(queue)
        location = current_element[1]

        states_visited.append(location)

        if location == [WORLD_SIZE-1, WORLD_SIZE-1]:
            print("Goal Reached")

            print("States visited to Goal -- ")
            for state in states_visited:
                print(state, "=>", end=' ')

            break

        for direction in DIRECTIONS:

            neigh_location = move(location, direction)
            if neigh_location != location:

                heapq.heappush(queue, (current_element[2]+1 + H_MEM[neigh_location[0]][neigh_location[1]], 
                                       neigh_location, 
                                       current_element[2]+1))  
        


# print(calcDistanceToGoal())

if __name__ == "__main__":
    # simulate()
    generate_world()
    print_grid(start_location)
    print(H_MEM)
    a_star()
#simulate() 