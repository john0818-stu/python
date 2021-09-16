import pylab 
import matplotlib.animation as animation 
from numpy import *
from random import *

fig = pylab.figure()
infile = open('grades.txt','r',encoding="utf8")
nums , names , grades = list( zip( *[ x.split() for x in infile ] ) )

def animate(i) :

    pylab.xlabel("x")
    pylab.ylabel("y")
    pylab.title("everyone grades")
    pylab.xlim(-2,43)
    pylab.ylim(0,108)
    
    xs = [x for x in range(i)]
    ys = list( map( eval , grades[:i] ) )

    for i in range(i) :
        pylab.bar( xs[i] , ys[i] , color = [ random() for i in range(4) ] )
    
    #print(i)
    
ani = animation.FuncAnimation(fig, animate, interval=1) 
pylab.show()
