import copy

ROWS = 6
COLUMNS = 7

start_state = [ ['E' for _ in range(COLUMNS)] for _ in range(ROWS)]


def print_world(state):
    
    print("-"*5*COLUMNS)

    for i in range(ROWS):
        for j in range(COLUMNS):

            if state[i][j] == 'E':
                print("|   ", end=' ')                
            else:
                print("| ",state[i][j], end=' ')
        
        print("|")
        print("-"*5*COLUMNS)


def find_empty_location(state, col):

    for i in range(ROWS-1, -1, -1):
        
        if state[i][col] == 'E':
            return i
    
    return -1


def move(state, col, player):
    
    next_state = copy.deepcopy(state)

    index = find_empty_location(state, col)
    
    if index != -1:
        next_state[index][col] = player

    # same state is returned as it is
    # if move is not possible    
    return next_state


def main():
    print_world(start_state)
    next_state = move(start_state, 1, "B")
    print_world(next_state)
    next_state = move(next_state, 1, "R")
    print_world(next_state)

if __name__ == '__main__':
    main()
