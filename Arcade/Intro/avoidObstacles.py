"""
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right.
You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.
"""
###SREEKANTH
def avoidObstacles(inputArray):
    #a=sorted(inputArray)
    o=[]
    for i in range(max(inputArray)):
        if i not in inputArray:
            o.append(i)
    i=1
    
    while i<=max(inputArray)+1:
        result=True
        j=1
        while j<=max(inputArray)+1:
            if i*j in inputArray:
                result=False
                break
            j+=1
        if result==True:
            return i
        i+=1
