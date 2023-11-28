from datetime import datetime
from typing import List
from math import sqrt

# Generic Sudoku Solver
# ******************************
# A sudoku puzzle is one such that given a set of unique characters, each row, column, and 
# square grid can only have 1 each character. See https://masteringsudoku.com/sudoku-rules-beginners/
# for more information on how to play.
#
# Your job is to write a solver that takes a sudoku puzzle and fills in all the characters correctly.
# Puzzles for this assignment use any characters, not just traditional numbers 1-9, and the
# size can vary/is not always 9x9 (but side length will always be a square number). Spots that are not
# filled in have None in them.
#
# Tips:
# - Sets are your friend! Checking to see if something is in a set is an O(1) lookup. Leverage that
#   efficiency to make your code run within the hidden test case time limit.
# - It is worthwhile to consider what you should initialize before starting your recursive algorithm
#   (increased complexity inside your recursive calls can be really bad for efficiency!)
# - If you are not sure where to start, use previous backtracking exercises for inspiration (N-queens/ratmaze)
# 
# Extensions: 
# 1) If you are backtracking in empty cell order, try optimizing the solver by finding more optimal empty 
#    cells to use for your subsequent recursive calls. See how fast you can get the 16x16 test to finish!:)
#    Uncomment the 16x16 advanced test to put things to the test (see if you can get it to run in under 5s)
# 2) Use tkinter to put a UI around the solver, where you can type in your own puzzles to solve!
# 3) Write a Sudoku puzzle creator

class SudokuSolver:

    # Constructor
    # ************************
    # cell_options param might look like ["W", "L", "F", "S", "T", "R", "N", "G", "P"]
    # The size of the grid will always be the length of cell_options  
    def __init__(self, cell_options:List[str]) -> None:
        self.cell_options = cell_options

    
    # solve
    # *************************
    # Takes a sudoku grid with some values filled in (2D array) and returns a solution grid 
    # with all cells filled in (also a 2D array).  Empty cell values are None.
    #
    # Reminder: Don't change this function signature. This is a "wrapper" that is called by the test. 
    # Modify solve_recursive to include needed parameters, and call that inside this function.   
    def solve(self, grid:List[List[str]]) -> List[List[str]]:
        self.grid = grid
        self.size = len(grid)
        self.size_root = int(sqrt(self.size))
        self.cells_remaining = self.size * self.size

        self.rows = [set()]
        self.cols = [set()]
        self.squares = [set()]
        for i in range(self.size):
            self.rows.append(set())
            self.cols.append(set())
            self.squares.append(set())

        self.empty_x_cells = []
        self.empty_y_cells = []
        self.total_empty = 0
        self.index = 0

        for y in range(self.size):
            for x in range(self.size):
                if grid[y][x] == None:
                    self.empty_x_cells.append(x)
                    self.empty_y_cells.append(y)
                    self.total_empty += 1
                else:
                    self.rows[y].add(grid[y][x])
                    self.cols[x].add(grid[y][x])
                    self.squares[self.get_square(y, x)].add(grid[y][x])
                    self.cells_remaining -= 1

        self.solve_recursive(self.empty_y_cells[0], self.empty_x_cells[0])
        if self.cells_remaining > 0:
            print("Puzzle is impossible.")
        return self.grid
    

    # A recursive function used to solve the puzzle. This is NOT used by any test cases, so 
    # modify parameters to include whatever you need!
    def solve_recursive(self, y:int, x:int) -> List[List[str]]:
        if self.cells_remaining == 0:
            return

        for char in self.cell_options:
            if (char in self.rows[y]) or (char in self.cols[x]) or (char in self.squares[self.get_square(y, x)]):
                continue
            else:
                self.rows[y].add(char)
                self.cols[x].add(char)
                self.squares[self.get_square(y, x)].add(char)
                self.grid[y][x] = char
                self.cells_remaining -= 1

                self.index += 1
                if self.index == self.total_empty:
                    return
                self.solve_recursive(self.empty_y_cells[self.index], self.empty_x_cells[self.index])
                if self.cells_remaining == 0:
                    return
                self.index -= 1

                self.rows[y].remove(char)
                self.cols[x].remove(char)
                self.squares[self.get_square(y, x)].remove(char)
                self.grid[y][x] = None
                self.cells_remaining += 1


    def get_square(self, y:int, x:int) -> int:
        return (self.size_root * (y // (self.size_root))) + (x // (self.size_root))
