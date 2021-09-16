def main() :
        
        y , m ,d = map( int , input( "輸入年 月 日> "  ).split() )

        for s in [100,1000,10000] :

                print( "第 {} 天 :".format(s),"-".join( f( y , m , d , s ) ) )

def q(y) :#閏年
	
	if ((y % 4 == 0 and y % 100 != 0) or (y % 400 == 0 and y % 3200 != 0)):

		return True
	else :

		return False

def day( y , m  ) : #判斷月友幾天

	days = [ 31 , 28 , 31 , 30 ,31 , 30 ,31 ,31 ,30 ,31 ,30 ,31 ]

	if q(y) == True : days[1] = 29

	return days[m-1]

def f( y , m , d , s ) : #2018 1 1 加 100
        
        s = s - d - day( y , m ) + 1

        m = m + 1

        while 1 :

                s = s - day( y , m )

                m += 1

                if m == 13 :

                        m = 1

                        y += 1
                        
                if s < day( y , m ) :

                        break
                
        return [ str( y ) , str( m ) , str( s ) ]

main()

