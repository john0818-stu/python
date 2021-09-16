n = int ( input ( "> ") )

for i in range (n):
    
    for j in range( 1 , n +1 ):
        
        print( str(j)*i + "\\" + " "*2*(n-i-1) + "/" +  str(j+1)*i , end="")
        
    print()
    
for i in range (n-1,-1,-1):
    
    for j in range ( 1 , n +1):
        
        print( str(j)*i + "/" + " "*2*(n-i-1) + "\\" + str(j+1)*i , end="")
        
    print()

print()
print()

for i in range(n) :

    for j in range(n) :

        print( str(j+1)*i + "\\" + "  "*(n-i-1) + "/" + str(j+2)*i , end="" )

    print()

for i in range(n) :

    for j in range(n) :

        print( str(j+1)*(n-i-1) + "/" + "  "*i + "\\" + str(j+2)*(n-i-1) , end="" )

    print()
