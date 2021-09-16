n = int ( input ( "> ") )

for i in range (n):
      
    for j in range(n):
        
        print(1,end=" ")
       
    print()
    
for s in range(1,3):
    
    print( end="\n" )
    
    for i in range(n):
        
        for t in range(s+1):
            
            for j in range(n):
                
                print( t+2*s , end=" " )

            print( end=" " )
            
        print()
