n = int ( input ( "> ") )

for i in range (2) :
    
    for t in range (n) :
        
        for j in range (3) :
            
            for s in range (n) :
                
                if i == 1 and j == 0 :
                    
                    print( "+" , end=" " )
                    
                elif i==0 and j==0:
                    
                    print( "*" , end=" " )
                    
                else:
                    
                    print( "-" , end=" " )
                    
        print()
