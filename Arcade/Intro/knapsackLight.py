"""
You found two items in a treasure chest! The first item weighs weight1 and is worth value1, and the second item weighs weight2 and is worth value2. What is the total maximum value of the items you can take with you, assuming that your max weight capacity is maxW and you can't come back for the items later?

Note that there are only two items and you can't bring more than one item of each type, i.e. you can't take two first items or two second items.
"""

# Dont think this is the right answer
def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1+weight2<=maxW:
        return value1+value2
    
    if maxW<weight1 and maxW<weight2:
        return 0
    if weight1+weight2>maxW:
        if weight1==maxW:
            if weight2<weight1:
                if max(value1,value2)==value1:
                    return value1
                else:
                    return value2
            else:
                return value1
        if weight2==maxW:
            if weight1<weight2:
                if max(value1,value2)==value2:
                    return value2
                else:
                    return value1
            else:
                return value2
        if max(value1,value2)==value1:
            return value1
        if max(value1,value2)==value2:
            return value2
        
