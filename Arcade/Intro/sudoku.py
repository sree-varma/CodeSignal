"""
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.
"""

def sudoku(grid):

    num=[i for i in range(1,10)]
    for i in range(len(grid)):
        
        if sorted(grid[:][i])!=num:
            return False
    column=0
    
    while column<9:
        row=0
        temp=[]
        while row<9:
            temp.append(grid[row][column])
            row+=1
        if sorted(temp)!=num:
            return False
        column+=1
    
    row=0
    column=0
    i=0
      
    
    while i<9:
        o=[]
        for r in range(i,i+3):
            j=0
            if j<9:
                for c in range(j,j+3):
                
                    o.append(grid[r][c])
                j+=3
        if sorted(o)!=num:
            return False
        i+=3
    return True
