n = int ( input ( "> ") )

for i in range ( 2*n-1 , -1 , -1 ) :
        
    for j in range ( 1 , -2 , -1) :
                
        if i :

            if j == 0 :
               
                print( " "*i + "/"  + "  "*( 2*n - 1 - i ) +  "\\" + " "*i , end="" )

            else :

                if i < n :
                
                    print( " "*i + "/" + "  "*( n - 1 - i ) + "\\" + " "*i , end="" )

                else :

                    print( "  "*n , end="" )    

        else :
        
            print( "/" + "__"*( n-1 if j else 2*n-1 ) + "\\", end = "" )

    print()
 
print()
print()

for i in range(2*n) :

    #print(i , end="   +" )

    for j in range(3) :

        if j == 1 :

            print( " "*(2*n-i-1) + "/" + ("  "*i if i != 2*n - 1 else "__"*i) + "\\" + " "*(2*n-i-1) , end=""  )

        else :

            if i < n :

                print( "  "*n , end="" )

            else :

                print( " "*(2*n-i-1) + "/" + ("  "*(i-n) if i != 2*n - 1 else "__"*(i-n)) + "\\" + " "*(2*n-i-1)  , end = "" )

    print()
