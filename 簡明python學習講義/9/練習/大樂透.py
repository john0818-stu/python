from random import *

def lottery( n , best ) :

    while 1 :

        best.add( randint(1,49) )
        if len(best) == 6 : return
            
def check_num( aset , bset ) :
    return aset & bset 
    
def main() :

    num = 6

    fset , cset = set() , set()

    lottery( num , fset ) #中獎號碼

    #print( " ".join( map( lambda x : "{:>2}".format(str(x)) , sorted(fset) )  ))

    print( " ".join( map( str , sorted(fset) ) ) )

    for i in range(10) :

        aset = set()
        lottery( num , aset )
        cset = check_num( fset , aset )

        print( " ".join( map( str , sorted(aset) ) ) ,
                ":" , len(cset) , "-->" , " ".join( map( str , sorted(cset) ) )
               )
        
main()
