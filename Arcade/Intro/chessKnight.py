"""
Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.

Ref: https://github.com/pace-noge/code-fights/blob/master/chessKnight.py
"""
def chessKnight(cell):
    r=int(ord(cell[0]))
    c=int(cell[1])
    
    valid = [[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]
    s = 0

    for i in range(len(valid)):
        tr = r +valid[i][0]
        tc =  c + valid[i][1] 
        if (tr >= 97 and tr <= 104 and tc >= 1 and tc <= 8):
            s += 1

    return s
