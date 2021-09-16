'''
def fsum( fn , a , b ) :
    s = 0
    for x in range(a,b+1) :
        s += fn(x)
    return s 

sqr = lambda x : x**2
cubic = lambda z : z**3

print( fsum( sqr , 1 , 10 ) ) # 1 到 10 的 平方和
print( fsum( cubic , 1 , 10 ) )# 1 到 10 的 立方和
'''
#畫圖
import pylab
pylab.figure( facecolor = "w" )

def plot_fn( f , a , b , n ) :
    xs = pylab.linspace( a , b , n )
    ys = f(xs)
    pylab.plot(xs,ys)

#h = 2sin(x) + 4 cos(x)
def h(x) :
    return 2*pylab.sin(x) + 4*pylab.cos(x)

plot_fn( h , -1 , 2 , 100 )
plot_fn( lambda x : x**3 - x**2 + 1 , -1 , 2 , 50 )
pylab.axis()
pylab.grid()
pylab.show()
