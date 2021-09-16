n = int ( input ( "> ") )

for i in range(n):
    
    for j in range(n):
        
        print(" "*i + "\\" + " "*2*(n-i-1) + "/" + " "*i , end="")
        
    print()
    
for i in range(n-1,-1,-1):
    
    for j in range(n):
        
        print(" "*i + "/" + " "*2*(n-i-1) + "\\" + " "*i , end="")
        
    print()

print()

print()

for i in range(n) :

    for j in range(n) :

        print( " "*i + "\\" + "  "*(n-1-i) + "/" + " "*i  , end="" )

    print()
for i in range(n) :
    for j in range(n) :

        print( " "*(n-i-1) + "/" + "  "*i + "\\" + " "*(n-i-1) , end="" )
    print()
