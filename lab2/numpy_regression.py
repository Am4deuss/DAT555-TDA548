from numpy import *
import sys
import matplotlib.pyplot as plt

def powers(listPowers,n1,n2):
    if listPowers == []:
        return []
    powerMatrix = []
    for i in listPowers:
        temp = []
        for j in range(n1,n2+1):
            temp.append(i**j)
        
        powerMatrix.append(temp)
    
    return powerMatrix

#textfile = sys.argv[1]
textfile = 'chirps.txt'

xyPairs = loadtxt(textfile)



resList = transpose(xyPairs)
x = resList[0]
y = resList[1]

Xp  = powers(x,0,1)
Yp  = powers(y,1,1)
Xpt = transpose(Xp)

[[b],[m]] = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))



plt.plot(x,y,'ro')
plt.plot(x,y2)
plt.show()