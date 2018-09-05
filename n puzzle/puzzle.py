import random

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

    
    def goal_test(self):
        pass


if __name__ == "__main__":
    
    g = Grid(4)
    g.print_grid()

    g.move(Grid.UP)
    g.print_grid()
    g.move(Grid.DOWN)
    g.print_grid()
    g.move(Grid.LEFT)
    g.print_grid()
    g.move(Grid.RIGHT)
    g.print_grid()


