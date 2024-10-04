from numpy import *
import sys
import matplotlib.pyplot as plt

def powers(listPowers,n1,n2):
    if len(listPowers) == 0:
        return listPowers
    powerMatrix = []
    for i in listPowers:
        temp = []
        for j in range(n1,n2+1):
            temp.append(i**j)
        
        powerMatrix.append(temp)
    
    return array(powerMatrix)

def poly(a,x):
    result = 0
    degree = len(a)
    for i in range(degree):
        result += a[i] * (x ** i)
    return result

textfile = sys.argv[1]
n = sys.argv[2]


xyPairs = loadtxt(textfile)

resList = transpose(xyPairs)
x = resList[0]
y = resList[1]

Xp  = powers(x,0,n)
Yp  = powers(y,1,1)
Xpt = Xp.transpose()

a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
a = a[:,0]

x2 = linspace(x[0],x[len(x)-1],int((x[len(x)-1]-x[0])/0.2)).tolist()
y2 = [poly(a,x) for x in x2]




plt.plot(x,y,'ro')
plt.plot(x2,y2)
plt.show()