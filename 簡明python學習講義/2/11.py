n = int ( input ( "> ") )

for i in range ( n-1 , -n , -1) :

    for j in range (n) :
                
        if i :
                
            print( " "*abs(i) + ( "/" if i > 0 else "\\" ) + "||"*( n - 1 - abs(i) ) + ( "\\" if i > 0 else "/" )  + " "*( abs(i) - 1 ) , end="" )

        else :
        
            print( "x" + "||"*(n-1) , end = "x" if j == n-1 else "" )



    print()
 
    
print()
print()
for i in range(n) :

    for j in range(n) :

        if i == n - 1 :

            print(  "x" + "||"*(n-1)  , end=("" if j != n - 1 else "x") )
        
        else :

            print( " "*(n-i-1) + "/" + "||"*(i) + "\\" + " "*(n-i-2) , end="" )

    print()

for i in range(n-1) :

    for j in range(n) :

        print( " "*(i+1) + "\\" + "||"*(n-i-2) + "/" + " "*i , end=""   )

    print()
