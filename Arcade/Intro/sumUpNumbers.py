"""
CodeMaster has just returned from shopping. He scanned the check of the items he bought and gave the resulting string to Ratiorg to figure out the total number of purchased items. Since Ratiorg is a bot he is definitely going to automate it, so he needs a program that sums up all the numbers which appear in the given input.

Help Ratiorg by writing a function that returns the sum of numbers that appear in the given inputString.


"""

def sumUpNumbers(inputString):
    
    o=[]
    n=''
    
    for i,j  in enumerate((inputString)):

        if j.isdigit()==True:
            n+=j
        if i+1<len(inputString) and (inputString[i+1].isdigit()==True and j.isdigit()==True):
                
                continue
        if j.isdigit()==False:
            
            n=''
        o.append(n)
        
    
    num=[int(i) for i in o if i.isdigit()==True]
    
    return sum(num)
