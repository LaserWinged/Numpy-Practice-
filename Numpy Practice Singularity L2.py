import numpy as np

a = np.zeros(((3,3)),dtype=np.int64)
a[:] = 2
a.fill(8)
a+=3
a -=2 

print(a)

b= np.arange(1, 10).reshape((3,3))
'''print(b)
b_sum=b.sum(0)
print(b_sum)
b_rowsum=b.sum(1)
print(b_rowsum)'''
#print(b)'''

#Arithmetic Operator
'''c=np.zeros((3,3))
c.fill(2)
array_sum=c.sum()
print(array_sum)
array_product=c.prod()
array_average=c.mean()
array_min=c.min()
array_max=c.max()
print(array_max,array_min)
print(array_average)
f,g= c.argmax(), c.argmin()
#arg max will give the index of the value'''

peak_to_peak = np.ptp(b)
#peak to peak means max - min 
#print(peak_to_peak)

 #flatten arrays 
'''array_flat= b.reshape(b.size)
print(array_flat)'''

#2nd method to flatten array
'''array_flat=b.flatten()
print(array_flat)

array_flat= b.ravel()
print(array_flat)'''

#The flatten will make a copy, the ravel will make a view of the array
#view affects orignal array, copy dosent 
#repeat values/arrays
'''array_repeat =np.repeat(255, 3)
print(array_repeat)
array_repeat =np.repeat(b,3) #can add axis also after 3. 0,1 
print(array_repeat)
array_unique= np.unique(array_repeat , axis=0)
print(array_unique)
array_diagonal = np.diagonal(b) #format is (b,offset)
print(array_diagonal)'''

#conversion and storage
'''my_list =b.tolist()
print("b is",type(b))
print("mylist is", type(my_list))

b.tofile("my_array.txt", sep=",")'''

#transposition 
'''array_swapped=np.swapaxes(b, 0, 1)
print(array_swapped)
array_swapped = b.transpose(1,0)
print(array_swapped)
array_swapped=b.T
print(array_swapped)'''

#operations on 2 matrices.
simple_ops= a+b
'''print(simple_ops)

modulo=b%a
print(modulo)

floor_division=b//a #integers
floor_division= np.floor(b/a) #float
print(floor_division)'''

# matrix multiplication 
matrix_multiply = np.matmul(a,b)
# print(matrix_multiply) 
matrix_multiply = a.dot(b)
matrix_multiply= a @ b
print(a*b)
