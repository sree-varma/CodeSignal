"""
Given array of integers, remove each kth element from it.
"""
def extractEachKth(inputArray, k):
    a=[]
    count=1
    for i,j in enumerate(inputArray):
        print(count,j,count%k)
        if count!=k and (count%k)!=0:
            a.append(j)
        count+=1
    
    return a
