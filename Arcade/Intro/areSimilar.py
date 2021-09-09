"""
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.
"""
def areSimilar(a, b):
    count = 0
    A = []
    B = []
    for i in range(len(a)):
        if (a[i]!= b[i]):
            count +=1
            A.append(a[i])
            B.append(b[i])

    if (count ==0):
        return True 

    elif count ==2: 
        return set(A)==set(B)

    else:
        return False
