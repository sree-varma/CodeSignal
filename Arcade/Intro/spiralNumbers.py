"""
Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.
"""
def spiralNumbers(n):
    m=[[0 for i in range(n)] for i in range(n)]
    j=1
    r1=0
    
    c1=0
    
    k=n
    while n>0:        
        c2=n-1
        r2=n-1
        for c in range(c1,c2+1):
                
            m[r1][c]=j
            if j==k*k:
                return m
            j+=1
        r1+=1
        for r in range(r1,r2+1):
                
            m[r][c2]=j
            if j==k*k:
                return m
            j+=1
        c2-=1
        for c in range(c2,c1-1,-1):
                
            m[r2][c]=j
            if j==k*k:
                return m
            j+=1
        r2-=1
        for r in range(r2,r1-1,-1):
                
            m[r][c1]=j
            if j==k*k:
                return m
            j+=1
        c1+=1
        
        n=n-1
        
    return m
