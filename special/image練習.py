from PIL import Image
import numpy as np 
import pylab


im = Image.open( "123.png" )

arr = np.array( im )

print( arr.shape )

pylab.imshow( arr )
pylab.axis("off")
pylab.show()
"""
print("x")
a = 2
"""
