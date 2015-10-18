import random
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.axis('off')


class GameOfLife:
    """
    Conway's Game of Life.

    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

    Representations => 0 : dead, 1 : alive, 2 : dying, 3 : spawing
    """
    def __init__(self,board=None,size=None,iterations=None):
        if board is None:
            board = self.generate_board(size)
        if iterations is None:
            iterations = 100
        self.iterations = iterations
        self.board = board
        self.cmap = mpl.colors.ListedColormap(['#290000','#CC0000','#800000','#E68A00'])
        self.update_rules = {0:0,1:1,2:0,3:1}
        try:
            self.plot_board(0)
            self.play_game()
        except:
            print('invalid board')

    def generate_board(self,size=None):
        """
        Generate a random game board of the requested size
        """
        if size is None:
            size = 100 
        board = []
        while len(board) < size:
            row = []
            while len(row) < size:
                boo = random.randint(0, 1)
                row.append(boo)
            board.append(row)
        return board
             
    def play_game(self):
        """
        Play the game for as many iterations as requested
        """
        i = 1
        # check back here later...
        while i <= (self.iterations * 2 - 1):
            self.start_update()
            self.plot_board(i)
            i += 1
            self.finish_update()
            self.plot_board(i)
            i += 1

    def plot_board(self,iteration):
        """
        Output a plot of the board to an image file according to the iteration
        """
        img = plt.imshow(self.board,interpolation='nearest',cmap = self.cmap)
        fig = plt.figure(1)
        fig.savefig("output/t" + str(iteration) + ".png")

    def start_update(self):
        """
        Update the game board in-place to show spawning and dying cells
        """
        self.num_rows = len(self.board)
        self.num_cols = len(self.board[0])
        for i,row in enumerate(self.board):
            i_opts = self.get_opts(i,self.num_rows)
            for j,col in enumerate(row):
                j_opts = self.get_opts(j,self.num_cols)
                pos = [i,j]
                nbs = self.get_neighbors(i_opts,j_opts,pos)
                self.update_tile_value(nbs,i,j)

    def finish_update(self):
        """
        Update the game board in-place to show only living and non-living cells
        """
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.board[i][j] = self.update_rules[self.board[i][j]]

    def update_tile_value(self,neighbors,i,j):
        """
        Replace all spawning / dying cells with living / non-living cells
        """
        if self.board[i][j] == 0:
            if neighbors == 3:
                self.board[i][j] = 3
        else:
            if neighbors not in [2,3]:
                self.board[i][j] = 2

    def get_opts(self,pos,lim):
        """
        Get all possible options surrounding a cell along one dimension
        """
        opts = [pos]
        if pos < lim - 1:
            opts.append(pos + 1)
        if pos > 0:
            opts.append(pos - 1)
        return opts

    def get_neighbors(self,row_opts,col_opts,pos):
        """
        Count the number of living cells surrounding a cell
        """
        neighbors = 0
        for e in row_opts:
            for f in col_opts:
                if [e,f] != pos:
                    tile = self.board[e][f]
                    if tile in [1,2]:
                        neighbors += 1
        return neighbors

sample_board = [[0,1,0,1],[1,0,0,1],[1,0,1,0],[1,0,0,1]]
sample_board = [[0,1,0,1,0],[1,0,0,1,1],[1,0,1,0,0],[1,0,0,1,1],[0,1,0,1,0]]
GameOfLife()
