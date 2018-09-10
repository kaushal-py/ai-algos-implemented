import random
import time
import copy

class Grid:

    # define static variables for directions
    UP = 0
    LEFT = 1
    RIGHT = 2
    DOWN = 3


    '''
    Initialise the grid
    size : size of the n puzzle problem grid.
    grid : a 2 dimensional matrix representing the grid
    '''
    def __init__(self, size):

        self.size = size
        self.grid = [[0 for x in range(self.size)] for y in range(self.size)]
        self.blank = self._generate_random_grid()

        # a set which contains a set of all visited states
        self.visited_states = set()


    '''
    A private helper method to generate a 
    random start sequence of the grid.
    A random shuffle of values of range(1,n+1) is generated.
    '''
    def _generate_random_grid(self):

        _values = list(range(1, self.size*self.size + 1))

        random.shuffle(_values)
        
        # location of blank
        blank = [0,0]

        index = 0
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i][j] = _values[index]

                if _values[index] == self.size*self.size:
                    blank = [i, j]

                index += 1

        return blank
        #value_string = ''.join(str(e) for e in _values)
        #print(value_string)



    '''
    Helper function to calculate hash of a state.
    Logic used for calculating hash -
    Sum over all i,j -> ( tile_value[i][j]*(i+j) )
    '''
    def _calc_hash(self, state):

        hash = 0

        for i in range(self.size):
            for j in range(self.size):
                hash += state[i][j]*(i+j)

        return hash        


    '''
    Helper function to print the grid to the console.
    '''
    def print_grid(self):

        print("-"*16*self.size)

        for i in range(self.size):
            for j in range(self.size):

                if self.grid[i][j] != self.size*self.size:
                    print("|\t", self.grid[i][j], end='\t')
                else:
                    print("|\t", end='\t')
                
            print("|")
            print("-"*16*self.size)

   

    '''
    Move the blank in one of the four directions
    The direction is specified using integer values 
    as given below -

    UP = 0
    LEFT = 1
    RIGHT = 2
    DOWN = 3
    '''
    def move(self, direction):
        
        if direction == self.UP:
            
            if self.blank[0] != 0:
                self.grid[self.blank[0]][self.blank[1]], self.grid[self.blank[0] -1 ][self.blank[1]] = self.grid[self.blank[0] -1 ][self.blank[1]], self.grid[self.blank[0]][self.blank[1]] 
                self.blank[0] -= 1


        if direction == self.DOWN:
            
            if self.blank[0] != self.size - 1:
                self.grid[self.blank[0]][self.blank[1]], self.grid[self.blank[0] +1 ][self.blank[1]] = self.grid[self.blank[0] +1 ][self.blank[1]], self.grid[self.blank[0]][self.blank[1]] 
                self.blank[0] += 1

        if direction == self.LEFT:
            
            if self.blank[1] != 0:
                self.grid[self.blank[0]][self.blank[1]], self.grid[self.blank[0]][self.blank[1] -1 ] = self.grid[self.blank[0]][self.blank[1] -1 ], self.grid[self.blank[0]][self.blank[1]] 
                self.blank[1] -= 1

        if direction == self.RIGHT:
            
            if self.blank[1] != self.size -1:
                self.grid[self.blank[0]][self.blank[1]], self.grid[self.blank[0]][self.blank[1] +1 ] = self.grid[self.blank[0]][self.blank[1] +1 ], self.grid[self.blank[0]][self.blank[1]] 
                self.blank[1] += 1
    
    
    '''
    Move without affecting state
    P.S. This funciton is a result of bad code design.
    Global variables are changed by internal functions, which
    is sometimes not required.
    '''
    def _move_non_affecting(self, direction):
        
        temp_state = copy.deepcopy(self.grid)
        self.move(direction)
        moved_state = copy.deepcopy(self.grid)
        self.grid = copy.deepcopy(temp_state)
        return moved_state

    
    '''
    Test for goal condition, ie.
    the state where all the tiles are arranged in ascending order.
    '''
    def goal_test(self, state):
        
        test_value = 1

        for i in range(self.size):
            for j in range(self.size):
                if state[i][j] != test_value:
                    return False
                test_value += 1
        return True
    
    
    '''
    Perform a bfs search to find the goal
    '''
    def bfs(self):
        
        # a temp variable to hold the current state
        curr_state = copy.deepcopy(self.grid)

        # a queue for bfs that holds states
        bfs_queue = []
        bfs_queue.append(curr_state)
        self.visited_states.add(self._calc_hash(curr_state))

        count_visited_states = 0

        # bfs algorithm starts here
        while ((not self.goal_test(curr_state)) and (len(bfs_queue)!= 0)):
                
                curr_state = bfs_queue.pop(0)
                print(bfs_queue)
                self.grid = copy.deepcopy(curr_state)

                for direction in [Grid.UP, Grid.DOWN, Grid.LEFT, Grid.RIGHT]:
            
                    neighbour_state = self._move_non_affecting(direction)
                    if self._calc_hash(neighbour_state) not in self.visited_states:
                        bfs_queue.append(neighbour_state)
                        self.visited_states.add(self._calc_hash(neighbour_state))
                        print(neighbour_state)
                
                count_visited_states += 1
                print("Visited states : {}".format(count_visited_states))

                self.print_grid()
                time.sleep(1)
        
        if self.goal_test(self.grid):
            print("Yay goal reached!")



if __name__ == "__main__":
    
    g = Grid(3)
    g.print_grid()

    g.bfs()

    


