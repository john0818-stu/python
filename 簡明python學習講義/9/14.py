def main() :

        while 1 :
        
                y , m , d = map( int , input( "1> "  ).split() )

                y0 , m0 , d0 = map( int , input( "2> "  ).split() )

                my , mm , md = ( y , m , d ) if int( str(y) + str(m) + str(d) ) >  int( str(y0) + str(m0) + str(d0) ) else ( y0 , m0 , d0 )

                sy , sm , sd = ( y , m , d ) if int( str(y) + str(m) + str(d) ) <  int( str(y0) + str(m0) + str(d0) ) else ( y0 , m0 , d0 )

                if int( str(y) + str(m) + str(d) ) >  int( str(y0) + str(m0) + str(d0) ) :
                
                        print( "相差 {} 天".format( ym(  my , sy , mm , sm ) + md - sd ) )

                else :

                        print( "相隔 {} 天".format( ym(  my , sy , mm , sm ) + md - sd ) )
               
def q(y) :#閏年
	
	if ((y % 4 == 0 and y % 100 != 0) or (y % 400 == 0 and y % 3200 != 0)):

		return True
	else :

		return False

def day( y , m  ) : #判斷月友幾天

	days = [ 31 , 28 , 31 , 30 ,31 , 30 ,31 ,31 ,30 ,31 ,30 ,31 ]

	if q(y) == True : days[1] = 29

	return days[m-1]

def ym(  my , sy , mm , sm ) :

        ans = 0
        
        while 1 :

                ans = ans + day( sy , sm )

                sm += 1

                if sm == 13 :

                        sm = 1

                        sy += 1
                        
                if my == sy and mm == sm :
                        
                        break
        return ans
main()

