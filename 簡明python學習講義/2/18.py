n = int ( input ( "> ") )

hh,vv,nw,ne,sw,se=chr(9472),chr(9474),chr(9484),chr(9488),chr(9492),chr(9496)

for i in range ( n , -n-1 , -1 ) :

    for j in range (n):

        if i :

            if abs(i) == n :
    
                print( "    "*( abs(i) - 1 ) + ( nw if i > 0 else sw ) + hh*2  + ( ne if i > 0 else se ) + "    "*( abs(i) - 1 ) , end=" " )

            else  :

                print( "    "*( abs(i) - 1 ) + ( nw if i > 0 else sw ) + hh + ( se if i > 0 else ne ) + "    "*( 2*(n-abs(i)) - 1) + ( sw if i > 0 else nw ) + hh + ( ne if i > 0 else se ) + "    "*( abs(i) - 1 ) , end=" " )

        else :

            print( vv , "  "*( 2*n + 5 ) , vv , end=" " )
            
    print()
    

    

