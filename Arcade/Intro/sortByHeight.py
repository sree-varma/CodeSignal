"""
Some people are standing in a row in a park.
There are trees between them which cannot be moved.
Your task is to rearrange the people by their heights in a non-descending order without moving the trees.
People can be very tall!
"""
def sortByHeight(a):
    o=[i for i in a if i>0]
    o.sort()
    count=0
    for i in range(len(a)):
        if a[i]>0:
            a[i]=o[count]
            count+=1
    return a
