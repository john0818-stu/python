
from pylab import *

ts = [0+12*pi*i/1000 for i in range (1001)]

x=[sin(t)*(e**cos(t) - 2*cos(4*t)-sin(t/12)**5) for t in ts]

y=[cos(t)*(e**cos(t) - 2*cos(4*t)-sin(t/12)**5) for t in ts]

axis("off")#顯示區域(前面加"off"關掉做標軸)

fill(x,y,color="m")

plot(x,y,"b")

show()


