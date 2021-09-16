import os

s = os.listdir()

print(s)

cwd = os.getcwd()
print(cwd)

#f = os.popen('ls ..')

#print( list( os.popen('ls')) )
#print( [ x.strip() for x in f ] )

x = "john/text.py"
print( os.path.split(x) )
print( os.path.join( "john" , "text" ) )
print( os.path.splitext(x))

#import os
print( os.listdir() )
print(os.chdir("../"))
print( os.listdir() )
