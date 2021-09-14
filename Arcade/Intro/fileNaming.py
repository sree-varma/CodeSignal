"""
You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names, the one which comes later will have an addition to its name in a form of (k), where k is the smallest positive integer such that the obtained name is not used yet.

Return an array of names that will be given to the files.
"""
#Sreekanth
def fileNaming(names):
    o=[]
    
    for i,j in enumerate(names):
       if j not in o:
           o.append(j)
       else:
            c=1
            while True:
                if j+'('+str(c)+')' not in o:
                    o.append(j+'('+str(c)+')')
                    break
                c+=1 
    return o
