n = int ( input("> ") )

for i in range (n):
    
    for s in range (n):
        
        print( "|" , end="")
        
        for h in range (n):
            
            print( (i+h+s) % n + 1 , end="" )
            
    print("|")
