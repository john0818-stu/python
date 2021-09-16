from random import *

cards = [ i for i in range (52) ] # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ...

shuffle(cards)

color = "CDHS"

four_peoples = [[] for i in range(4)]

for i , ch in enumerate ( cards ) :
    
    #顏色 數字
    four_peoples[i%4] += [[ ch//13 , ch%13 , ch//13 + 1 + 5*(ch%13 + 1 ) ]]

for people in four_peoples :

    for lis in sorted( people , key = lambda x : -x[2])  :

        if lis[1] == 0  :
        
            b = "A"

        elif lis[1] == 10 :

            b = "J"

        elif lis[1] == 11 :

            b  = "Q"

        elif lis[1] == 12 :

            b  = "K"

        else :

            b = lis[1] + 1 
            
        print( color[ lis[0] ] + "{:<2}".format( b ) , end=" " )

    print()
