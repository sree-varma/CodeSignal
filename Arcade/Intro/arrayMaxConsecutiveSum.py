"""
Given array of integers, find the maximal possible sum of some of its k consecutive elements.
"""
def arrayMaxConsecutiveSum(inputArray, k):
    s=[]
    i=k
    maxx=sum(inputArray[0:k])
    temp=maxx
    
    while i<len(inputArray):
        temp+=inputArray[i]
        temp-=inputArray[i-k]
        if temp>maxx:
            maxx=temp
        i+=1 
    return maxx  
