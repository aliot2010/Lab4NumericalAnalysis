import math
import gauss
import numpy

xi = [0.0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
yi = [3, 87, 156, 210, 238, 252, 239, 211, 158, 90, -5]

N = 11  # число измерений
m = 2  # степень аппроксимрующего полинома m

def sum (data, p):
    s = 0.0
    for i in range(11):
        s += math.pow(data[i][0], p)
    return s

def sumY(data, p):
    s = 0.0
    for i in range(11):
        s += data[i][1] * math.pow(data[i][0], p)

    return s



data = numpy.zeros((11, 2))
for i in range(len(xi)):
    data[i][0] = xi[i]
    data[i][1] = yi[i]

A = numpy.zeros((m+1, m+2))

for i in range(m+1):#формируем левые части системы
    for j in range(m+1):
        A[i][j] = sum(data, i+j)

A[0][0] = N
for i in range(m + 1):#формируем правые части системы
    A[i][m+1] = sumY(data, i)

a = numpy.zeros(m+1)
a = gauss.gaussFunc(A)#определяем коэфф искомого полинома

for i in a:
    print(i)


#вычисление остаточной дисперсии
b = 0.0

for i in range(N):
    bi = data[i][1]
    for y in range(m+1):
        bi -= a[y] * math.pow(data[i][0], y)
    b += bi * bi

b /= (N-m-1)

print("sigma= " + str(math.sqrt(b)))






