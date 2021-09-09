"""
You are given an array of integers.
On each move you are allowed to increase exactly one of its element by one.
Find the minimal number of moves required to obtain a strictly increasing sequence from the input.
"""
def arrayChange(inputArray):
    count=0
    for i in range(1,len(inputArray)):
        if inputArray[i]<inputArray[i-1]:
            count+=abs(inputArray[i-1]-inputArray[i])
            
            inputArray[i]=inputArray[i]+abs(inputArray[i-1]-inputArray[i])
        if inputArray[i]==inputArray[i-1]:
            count+=1
            inputArray[i]=inputArray[i]+1
        
    return count
