import copy
import os

ROWS = 6
COLUMNS = 7
INFINITY = 10

PLAYERS = ("R", "B")

LOOKUP_DEPTH = 4

# set 1 if you want to move first, 
# else 0 if you want pc to make move first.
FIRST_MOVE = 1

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


def simulate_2_player():

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
        

def utility_basic(state, player):

    utility = 0

    for i in range(ROWS):
        for j in range(COLUMNS):
            utility = max(utility, max_connect_val(state, (i,j), player))

    return utility


def utility(state, player):

    if PLAYERS[0] == player:
        opponent = PLAYERS[1]
    else:
        opponent = PLAYERS[0]
    
    empty_spaces_player = 0
    empty_spaces_opponent = 0

    if utility_basic(state, player) >= 4:
        return 100
    if utility_basic(state, opponent) >= 4:
        return -100

    for i in range(ROWS):
        for j in range(COLUMNS):

            if state[i][j] != 'E':

                count_spaces = 0

                # top
                if i-1 >=0 and state[i-1][j] == 'E':
                    count_spaces += 1

                # right
                try:
                    if j+1 < COLUMNS and state[i][j+1] == 'E' and state[i+1][j+1] != 'E':
                        count_spaces += 1
                except:
                    count_spaces += 1
                
                # left
                try:
                    if j-1 >= 0 and state[i][j-1] == 'E' and state[i+1][j-1] != 'E':
                        count_spaces += 1
                except:
                    count_spaces += 1
                # top right
                #if i-1 >= 0 and j+1 < COLUMNS and state[i-1][j+1] == 'E'

                if state[i][j] == player:
                    empty_spaces_player += count_spaces
                else:
                    empty_spaces_opponent += count_spaces
    
    return empty_spaces_player - empty_spaces_opponent





def max_value(state, alpha, beta, depth, player, column):

    if depth == 0:
        return {
            "value" : utility(state, player),
            "column" : column
        }
    

    v = {
        "value" : -INFINITY,
        "column" : -1
    }

    for col in range(COLUMNS):
        neighbour, _ = move(state, col, player)

        max_val = min_value(neighbour, alpha, beta, depth-1, player, col)
        
        if v["value"] < max_val["value"]:
            v["value"] = max_val["value"]
            v["column"] = col

        if v["value"] >= beta:
            return v
        
        alpha = max(alpha, v["value"])
    
    #print(v)
    return v



def min_value(state, alpha, beta, depth, player, column):

    if depth == 0:
        return {
            "value" : utility(state, player),
            "column" : column
        }
    

    v = {
        "value" : INFINITY,
        "column" : -1
    }

    for col in range(COLUMNS):
        neighbour, _ = move(state, col, player)
        
        min_val = max_value(neighbour, alpha, beta, depth-1, player, col)
        
        if v["value"] > min_val["value"]:
            v["value"] = min_val["value"]
            v["column"] = col

        if v["value"] <= alpha:
            return v
        
        alpha = max(alpha, v["value"])
    
    #print(v)
    return v



def alpha_beta_search(state, depth, player):

    v = max_value(state, -INFINITY, INFINITY, depth, player, -1)

    return v["column"]


def simulate_VS_pc():

    os.system('clear')

    curr_state = start_state

    turn = FIRST_MOVE

    while(True):

        print_world(curr_state)


        if turn == 1:
            col = int(input("Enter the column: "))
        else:
            col = alpha_beta_search(curr_state, 3, PLAYERS[turn])

        os.system('clear')
        next_state, connect_val = move(curr_state, col, PLAYERS[turn])

        if next_state == curr_state:
            continue
        curr_state=next_state

        if connect_val == 4:
            print_world(curr_state)
            print(PLAYERS[turn], "won!")
            break
        
        turn = 1-turn


def main():
    
    simulate_VS_pc()

if __name__ == '__main__':
    main()
