"""
Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.
"""
#Sreekanth
def differentSquares(matrix):
    
    c=0
    s=[]
    while c<len(matrix)-1:
    
        r=0
        
        while r<len(matrix[0])-1:
        
            s.append([matrix[c][r], matrix[c][r+1], matrix[c+1][r], matrix[c+1][r+1]])
            r+=1       
            
       
        
        c+=1
    return len(set(tuple(i) for i in s))
