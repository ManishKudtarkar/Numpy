import numpy
n, m = input().split()
a = numpy.array([input().split() for _ in range(int(n))], int)
b = numpy.array([input().split() for _ in range(int(n))], int)
[print(i) for i in [a+b, a-b, a*b, a//b, a % b, a**b]]
