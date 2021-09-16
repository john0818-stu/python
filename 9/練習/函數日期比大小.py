def by_small_date(x) :
    s = x.split('/')
    return ( int(s[1]) , int(s[0]) )
    
def by_big_date(x) :
    s =  x.split('/')
    return (-int(s[1]) , -int(s[0]) )

dates = [ '2/2010' , '9/2010' , '7/2009' , '7/2008' ]

for date in sorted( dates , key = by_small_date )  :
    print(date,end=" ")
print()

for date in sorted( dates , key = by_big_date )  :
    print(date,end=" ")
print()
