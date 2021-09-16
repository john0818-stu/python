n = int ( input ( "> ") )

for s in range (n-1,-n,-1):
    
    t=n-abs(s)-1

    for i in range (3):

        print(" "*3*(n-1-t),end="")

        for k in range (n-1,-n,-1) :
            
            h = n - abs(k) - 1
            
            b = abs( n - t - 1 - h ) + 1  #每列有幾個
            
            a = ( h + 1 ) #山高 - n + abs(k)  
            
            if   t >= n - a :
            
                for k in range (b) :
                                    
                    b = abs( n - t -2 - h ) #對應數字,寬度
        
                    print ( str(b)*5 , end=" " )

                for j in range (n-t-1):
                
                    print( " "*5 , end=" ")
                        
            else :
            
                b = abs( n - t - 1 - h )
                
                for k in range (b) :
                    
                    for i in range (5) :
                        
                        print ( "" , end="" )

                    print ( end="" )
                    
        print()
        



