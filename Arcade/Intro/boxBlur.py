"""
Last night you partied a little too hard.
Now there's a black and white photo of you that's about to go viral! You can't let this ruin your reputation,
so you want to apply the box blur algorithm to the photo to hide its content.

The pixels in the input image are represented as integers.
The algorithm distorts the input image in the following way: 
Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3 square that has its center at x,
including x itself. All the pixels on the border of x are then removed.

Return the blurred image as an integer, with the fractions rounded down.
"""
def boxBlur(image):
    
    c=0
    
    s=0
    o=[]
    while c+2<len(image):
        ss=[]
        r=0
        while r+2<len(image[0]):
            s=0
            for i in range(c,c+3):
                
                s+=sum(image[i][r:r+3])
            ss.append(int(s/9))
            r+=1       
                
        o.append(ss)
           
        c+=1
    
    return o
