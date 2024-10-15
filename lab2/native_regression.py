from matrix import *
import sys
import matplotlib.pyplot as plt

#textfile = sys.argv[1]
textfile = 'chirps.txt'

xyPairs = loadtxt(textfile)

resList = transpose(xyPairs)
x = resList[0]
y = resList[1]

Xp  = powers(x,0,1)
Yp  = powers(y,1,1)
Xpt = transpose(Xp)

[[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))



plt.plot(x,y,'ro')
plt.plot(x,y2)
plt.show()