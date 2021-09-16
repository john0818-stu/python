n=int(input("> "))

from random import*

vals = [ randint(2,9) for i in range (n)]

for s in range (9,-2,-1):

    print(" "*(s+1),end="")
    
    for val in vals:
        
        if s ==val or s == -1:
            
            print( "*" if s == val else val , end=" " )
            
        elif s > val:
            
            print( " " , end=" ")

        else:
            
            print( "/" , end=" ")
        
    print()
    


