def ssum( a , b ) :
    s = 0
    for i in range( a , b+1 ) :
        s += i
    return s

no = ( 2 , 4 )
'''
print( ssum(2,4) )
print( ssum( no[0] , no[1] ) )
print( ssum( *no ) )
print( ssum(*(2,4))  )
'''

def avg(math,phy,eng=0) :
    if eng == 0 :
        return ( 3*math+2*phy ) // 5
    else :
        return 0
ans = { 'a':1 , "b":2 }
#print( avg(**ans) )
'''算半徑1到9
def main() :

    global pi
    pi = 3.14
    for r in range(1,10):
        print( circle_area(r) )

def circle_area( rad ) :

    #global pi
    return rad*rad*pi

main()
'''
'''global
def main() :

    global x
    x = 1
    fn()
    print(x) #x == 6
def fn() :
    global x
    x += 5
main()
'''
def main() :
    x = 1
    x += fn(x) #x == 7
    print(x)
def fn(a) :
    a += 5
    return a

main()
