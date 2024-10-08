def transpose(matrix):
    if matrix == []:
        return matrix

    newMatrix = []
    for i in range(0,len(matrix[0])):
        newRows = []
        for j in range(0,len(matrix)):
            newRows.append(matrix[j][i])

        newMatrix.append(newRows)
    
    return newMatrix

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

def matmul(matrixA, matrixB):
    if len(matrixA) < 1:
        return []
    
    n = len(matrixA)
    m = len(matrixB[0])
    k = len(matrixA[0])

    matrixC = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for p in range(k):
                matrixC[i][j] += matrixA[i][p] * matrixB[p][j]
            
    return matrixC

def invert(matrixA):
    a = matrixA[0][0]
    b = matrixA[0][1]
    c = matrixA[1][0]
    d = matrixA[1][1]
    det = a * d - b * c
    matrixB = [[d/det, -b/det],[-c/det, a/det]]
    return matrixB



def loadtxt(file):
    fileRead = open(file, "r", encoding = "utf-8")
    data = fileRead.read()
    lines = data.split("\n")
    matrix = []
    for i in lines:
        pair = i.split("\t")

        if len(pair) < 2:
            pass
        elif len(pair) > 2:
            pair.pop(2)
            matrix.append(pair)
        else:
            matrix.append(pair)

    outerIndex = 0
    for m in matrix: # Makes every string into float values
        innerIndex = 0
        for n in m:
            matrix[outerIndex][innerIndex] = float(n)
            innerIndex += 1
        outerIndex += 1

    fileRead.close()
    
    return matrix