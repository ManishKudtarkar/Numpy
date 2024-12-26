import numpy as np
lst =[0,1,2,3,4]
lst2=[4,5,6]
print(lst*2)
print(lst+lst2)

array =np.array(lst)
print(type(array))


np.zeros(5)

np.zeros([9,3])

my_data = np.array ([[0,3],[10,7],[20,9],[30,9]])
print(my_data)

for i in range(10):
  #print(i)
  print(i,end=".")


arr =np.arange(10)
print(arr)
type(arr)

arr = np.arange(1,10,2)
print(arr)

np.random.rand(5)

arr =np.arange(1,11,1)
print(arr)

arr[0]

arr[2:4]

arr[-1]

arr[arr<5]

arr[arr*2<5]

arr[[1,3,5]]

a  = [12,2,14,1,15]
set(a)

 b = "12213"
 set(b)

c = "1,1,21,3"
set(c)

tup = (1,21,2,1,42,3)
print(set(tup))

lst = [1,21,2,1,42,3]
print(set(lst))

  arr2d = np.arange(10).reshape((2,5))
print(arr2d)
