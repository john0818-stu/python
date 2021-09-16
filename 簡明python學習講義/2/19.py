n = int ( input ( "> ") )

for s in range(3):
    
    for i in range(n):
        
        for t in range(3):
            
            a = ( 3*s + t )//2 + 1 
                
            print( ( str(a) if t==s or t+s == 2 else " " )*n  , end="" )
    
        print()
