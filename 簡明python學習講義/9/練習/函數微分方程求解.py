import pylab

def fn(x) :

    return x**(1/3)*pylab.sin(x) + 0.2

pylab.figure(facecolor="w")
a , b , n = 0 , 20*pylab.pi , 501
dx = (b-a)/(n-1)

xs = [ a + i*dx for i in range(n) ]
ys = [None]*n

for c in range(0,11,5) :

    ys[0] = c
    for i in range( 1 , n ) :
        ys[i] = ys[i-1] + dx*fn(xs[i-1])

    sym = 'y(0) = ' + str( ys[0] )
    pylab.plot(xs,ys,label = sym )

pylab.title( r"$y' = \sqrt[3]{x}\ , \sin(x) + 0.2$" , fontsize = 20 )

pylab.xlabel('x')
pylab.ylabel('y')

pylab.legend(loc=2)
pylab.show()
