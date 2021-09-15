"""
n children have got m pieces of candy. They want to eat as much candy as they can, 
but each child must eat exactly the same amount of candy as any other child.
Determine how many pieces of candy will be eaten by all the children together.
Individual pieces of candy cannot be split.
"""
def candies(n, m):
    if m<n:
        return 0
    while True:
        if m%n==0:
            return m
        
        m=m-1
