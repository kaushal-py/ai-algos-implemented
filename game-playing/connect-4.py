import copy
import os

ROWS = 6
COLUMNS = 7

PLAYERS = ("R", "B")


start_state = [ ['E' for _ in range(COLUMNS)] for _ in range(ROWS)]


def print_world(state):
    
    print("-"*5*COLUMNS)

    # Header
    for i in range(COLUMNS):
        print("| ", i, end=' ')
    print("|")
    print("-"*5*COLUMNS)
    
    # body
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
    
    connect_val = max_connect_val(next_state, (index, col), player)

    # same state is returned as it is
    # if move is not possible    
    return next_state, connect_val



def max_connect_val(state, pos, player):

    # Vertical Down
    (row, col) = pos
    count_down = 0
    while(row< ROWS and state[row][col] == player):
        row += 1
        count_down += 1
    
    # Horizontal Left
    (row, col) = pos
    count_left = 0
    while(col >= 0 and state[row][col] == player):
        col -= 1
        count_left += 1
    
    # Horizontal Right
    (row, col) = pos
    count_right = 0
    while(col < COLUMNS and state[row][col] == player):
        col += 1
        count_right += 1
    

    # Diagonal Left
    (row, col) = pos
    count_diag_left = 0
    while(row < ROWS and col >= 0 and state[row][col] == player):
        row += 1
        col -= 1
        count_diag_left += 1
    
    # Diagonal Right
    (row, col) = pos
    count_diag_right = 0
    while(row < ROWS and col < COLUMNS and state[row][col] == player):
        row += 1
        col += 1
        count_diag_right += 1
    
    return max(count_down, count_diag_left, count_diag_right, count_left+count_right-1)



def simulate():

    os.system('clear')

    curr_state = start_state

    turn = 0

    while(True):

        print_world(curr_state)

        print("--{}'s Turn--".format(PLAYERS[turn]))
        col = int(input("Enter the column: "))
        os.system('clear')
        curr_state, connect_val = move(curr_state, col, PLAYERS[turn])

        if connect_val == 4:
            print_world(curr_state)
            print(PLAYERS[turn], "won!")
            break
        
        turn = 1-turn
        


def main():
    
    simulate()

if __name__ == '__main__':
    main()
