


def main() :

    wstr = ( "Sun" , "Mon" , "Tue" , "Wed" , "Thu" , "Fri" , "Sat"  )
    w = 4

    fmt = "{:>" + str(w) + "}"
    while 1 :

        y = int( input( "輸入西元年> " ) )

        for m in range( 1 , 13 ) :

            print( " "*12 , m , "月" )

            for s in wstr :

                print( fmt.format(s) , end="" )

            print()

            wday , mdays = weekday( y , m , 1 ) , monday( y , m )

            print( " "*int( w*wday ) , end="" )

            for d in range( mdays ) :

                print( fmt.format(d+1) , end=( "" if wday<6 else "\n" ) )
                wday = (wday + 1 if wday<6 else 0 )

            print()

def isleap(y) : #判斷閏年

    return True if y%400 == 0 or ( y%100 and y%4 ) else False

def monday( y , m ) : # 某年某月

    day = [31,28,31,30,31,30,31,31,30,31,30,31]

    if m == 2 :

        return 29 if isleap(y) else 28

    else :

        return day[m-1]

def weekday( y , m , d ) :

    ( y , m ) = ( y-1 , m+10 ) if m < 3 else ( y , m-2 )
    return ( y + y//4 -y//100 +y//400 + int(2.6*m-0.2) + d )%7
main()
