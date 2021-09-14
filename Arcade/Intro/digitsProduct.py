"""
Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.
"""
# THIS IS A MODIFICATION OF THE MOST VOTED SOLUTION.
def digitsProduct(product):
      if product == 0:
        return 10
    elif product == 1:
        return 1
    i=9
    n=[]
    p=product
    while product>1:
        while i>1:
            
            if product%i==0:
                product=product/i
                n.append(i)
                
                break
            i-=1    
   
        else:
            return -1
    return int(''.join(map(str, sorted(n))))
   
