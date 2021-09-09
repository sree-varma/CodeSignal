"""
Given two cells on the standard chess board, determine whether they have the same color or not.
"""
def chessBoardCellColor(cell1, cell2):
    
    if ord(cell1[0])%2==ord(cell2[0])%2:
        if int(cell1[1])%2==int(cell2[1])%2:
            return True
    

    if ord(cell1[0])%2!=ord(cell2[0])%2:
        if int(cell1[1])%2!=int(cell2[1])%2:
            return True
    return False

