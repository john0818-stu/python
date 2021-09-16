
wstrs = ( "Sun" , "Mon" , "Tue" , "Wed" , "Thu" , "Fri" , "Sat" , "Sun" , "Mon" , "Tue" , "Wed" , "Thu" , "Fri" , "Sat" )

w = 4

def main() :
    
    while 1 :
        
        n = int( input("輸入年分> ") )

        for m in range(1 , 13) :

            a = 0 if m <= 9 else ""

            print( "{}-{}{}".format( n , a ,  m ) )

            for s in wstrs :

                print( "{:>{}}".format( s , str(w)) , end="" )

            print()

            wday , mdays = weekday( n , m , 1 ) , day( n , m  )

            print( " "*int(w*wday) , end="" )

            for d in range(mdays) :

                print( "{:>{}}".format( d+1 , str(w) ) , end= ("" if wday<13 else "\n") )
                wday = ( wday+1 if wday< 13 else 0 )

            print("\n")

# 某年是否為閏年
def isyear( n ) :

# 被 4整除， 且 不能被 100整除 為閏年 或 
# 被 4整除， 且 能 被 400整除 為閏年
    return True if n%4 == 0 and ( n%100 or n%400 == 0 ) else False

    
# 判段 某年月有幾天
def day( n  , m ) :

    days = [ 31 , 28  , 31 , 30 , 31 , 30 , 31 , 31 , 30 , 31 , 30 , 31 ]

    days[1] = 29 if isyear(n) else 28

    return days[ m -1 ]

def weekday( n , m , d ) :

    ( n , m ) = ( n - 1 , m + 10 ) if m < 3 else ( n , m - 2 )

    return ( n + n //4 - n//100 + n//400 + int(2.6*m - 0.2) + d )%7

main()
    

        
