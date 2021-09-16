def factoral(x) : #n階層

    p = 1
    for i in range(2,x+1) :
        p *= i
    return p

def power( a = 10 , n = 1 ) : #a = 10 , n = 1 預設

    p = 1
    for i in range(n) :
        p*=a
    return p

def npower( a = 10 , n = 1 ) : #a = 10 , n = 1 預設

    p = a**n
    return p

def age( byear , cyear = 2019 ) : #年齡

    return cyear - byear

def psum( a , b , c = 0 ) :

    return a*b + c


def powers( foo , n = 1 ) :

    for i in range(len(foo)) :

        foo[i] = foo[i]**n

    return foo

def powers( foo , n = 1 ) :

    return [ c**n for c in foo ]
