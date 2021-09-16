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

def dd( x ) :

    return ( "0" + str(x) ) if x < 10 else x

def f( x ) :

    y , m , d = x.__dict__.values()
    
    return y*1000 + m*100 + d

#a-b
def sub( a , b ) :

    y0 , m0 , d0 = a.__dict__.values()

    y1 , m1 , d1 = b.__dict__.values()

    ans = 0
        
    while 1 :

        if y0 == y1 and m0 == m1 :
                        
                break

        ans = ans + mondays( y1 , m1 )

        m1 += 1

        if m1 == 13 :

                m1 = 1

                y1 += 1
                
    return str( ans + d0 - d1 )
    
#a+b
def add( a , b ) :

    y , m , d = a.__dict__.values()
        
    while 1 :

        if b + d < mondays( y , m ) :

                break

        b = b - mondays( y , m )

        m += 1

        if m == 13 :

                m = 1

                y += 1
                             
    return "{}-{}-{}".format( y , dd(m) , dd(b + d) )

class Date :

    def __init__( self , y , m , d ) :

        self.y , self.m , self.d = y , m , d

    def __str__( self ) :

        s = [ self.y , dd( self.m ) , dd( self.d ) ]

        return "-".join( list( map( str , s ) ) )

    @classmethod
    def from_str( cls , ss ) :

        y , m , d = list( map( int , ss.split("-") ) )

        return cls( y , m , d  )

    def nth_day_of_year( self ) :

        ans = 0

        for i in range( 1 , self.m ) :

            ans += mondays( self.y , i )

        return ans + self.d
    #<
    def __lt__( self , foo ) :

        return True if f( self ) < f( foo ) else False
    #=
    def __eq__( self , foo ) :

        return True if f( self ) == f( foo ) else False

    def __sub__( self , foo ) :

        if f( self ) < f( foo ) :

            return "-" + sub( foo , self )

        else :

            return sub( self , foo )
    
    def __add__( self , foo ) :

        return add( self , foo )

foo = Date( 2018 , 3 , 2 )

date = input( "年-月-日> " )

bar = Date.from_str( date )

print( "foo :" , foo )

print( "bar :" , bar )

print( "nth day of year :" , bar.nth_day_of_year() , end="\n\n" )

print( "foo < bar :" , foo < bar )

print( "foo == bar :" , foo == bar )

print( "foo - bar :" , foo - bar , end="\n\n" )

print( "bar + 10 :" , bar + 10 )

print( "bar + 200 :" , bar + 200 )

print( "bar + 365 :" , bar + 365 )

print( "bar + 731 :" , bar + 731 )
