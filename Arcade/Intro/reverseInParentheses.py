"""
Write a function that reverses characters in (possibly nested) parentheses in the input string.
Input strings will always be well-formed with matching ()s.
"""

def reverseInParentheses(inputString):
    
    s=''
    e=''
    c=0
    r=inputString
    l=True
    while l==True:
        for i,j in enumerate(r):
            if j=='(':
                s=i
                c=1
                o=[]
                continue
            if j==')':
                c=0
                e=i
                a="("+"".join(o)+")"
                o=o[::-1]
                b="".join(o)
                
                
                r=r.replace(a,b)
                
                
                
            if c==1:
                o.append(j)
        
           
        if "(" in r and ")" in r:
            l=True
        else:
            l=False
    return r
