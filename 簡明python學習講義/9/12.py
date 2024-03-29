def main() :

    wstrs = ( "Sun" , "Mon" , "Tue" , "Wed" , "Thu" , "Fri" , "Sat" )
    w = 4 
    fmt = "{:>" + str(w) + "}"

    global allday

    while True :

        y = int( input("輸入西元年> ") ) 

        for m in range(1,13,2) :

            #if m == 5 : break

            for i in range(2) :

		# 列印月名與一周的星期字串
                print(  "{:>12}".format(m+i), "月" , end=" "*15 )

            print()

            xx = "".join( fmt.format(x) for x in wstrs )

            print( xx + "  " + xx )
            
            nw = []

            for i in range(2) :

		# 計算每月一日是星期幾與當月的天數
                wday , mdays = weekday( y , m + i , 1 ) , mondays( y , m + i )

                td = wday + mdays

                #print(wday)

                #計算一個月有幾周
                nw += [int( td/7 + ( 1 if td//7 != td/7 else 0 ) )]
                
            allday = [ [[" "]*7 for i in range( max(nw) ) ] for ss in range(2) ]

            for i in range( 2 ) :

                r = 1

                wday , mdays = weekday( y , m + i , 1 ) , mondays( y , m + i )
                
                for w , ch in enumerate( allday[i] ) :

                    for c in range( len(ch) ) :

                        if r > mdays :

                            break

                        if w == 0 and c < wday :

                            continue

                        else :

                            ch[c] = r 

                            r += 1                    
                            
            for ii in range( max(nw) ) :

                for ss in allday :

                    for ff in ss[ii] :

                        print( fmt.format(ff) ,end="")

                    print(end="  ")
                
                print()
            

                


# 某年是否為閏年
def isleap( y ) :
    return True if y%400 == 0 or ( y%100 and y%4 == 0 ) else False 

# 某年某月的日數
def mondays( y , m ) :
    days = [ 31 , 28 , 31 , 30 , 31 , 30 , 
             31 , 31 , 30 , 31 , 30 , 31 ]
    if m == 2 :
        return 29 if isleap(y) else 28 
    else :
        return days[m-1] 
        
# 計算某年月日星期幾
def weekday( y , m , d ) :
    ( y , m ) = ( y-1 , m+10 ) if m < 3 else ( y , m - 2 )
    return ( y + y//4 - y//100 + y//400 + int(2.6*m-0.2) + d )%7 


# 執行主函式
main() 
