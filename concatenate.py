import numpy

n, m, _ = map(int, input().split())
a1 = numpy.vstack([list(map(int, input().split())) for _ in range(n)])
a2 = numpy.vstack([list(map(int, input().split())) for _ in range(m)])
print(numpy.concatenate((a1, a2), axis=0))
