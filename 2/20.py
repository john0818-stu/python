n = int ( input ( "> ") )

for s in range(3):
    
    for i in range(n):
        
        for t in range(3):

            for j in range(n):
                
                if 0 < i < n-1 and 0 < j < n-1 :
                    
                    print( " " , end="" )
                    
                elif t==s or t+s == 2 :

                    a = ( 3*s + t )//2 + 1 
                    
                    print( str(a)  , end="" )
                    
                else :

                    print( " "  , end="" )
                
        print()

