"""
Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement. Check out the example below to see how it can move:
"""
def bishopAndPawn(bishop, pawn):
    
    
    
    if ord(bishop[0])%2==ord(pawn[0])%2 and abs(ord(bishop[0])-ord(pawn[0]))%2==0:
        if int(bishop[1])%2==int(pawn[1])%2 and abs(int(bishop[1])-int(pawn[1]) )%2==0:
            if abs(ord(bishop[0])-ord(pawn[0]))!=0:
                return True
    

    if ord(bishop[0])%2!=ord(pawn[0])%2 and abs(ord(bishop[0])-ord(pawn[0]))%2!=0:
        if int(bishop[1])%2!=int(pawn[1])%2 and abs(int(bishop[1])-int(pawn[1]))%2!=0:
            return True
    return False

