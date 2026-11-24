import numpy as np

my_array= np.arange(8)

#print(my_array)
#print(type(my_array))

'''my_array= np.arange(1,8,2)
print(my_array)

my_array= np.arange(1,8,0.5)
print(my_array)'''

#arrays from lists
#from_list=np.array([1,2,3])
#print(from_list)
#print(type(from_list[0]))

#from_list=np.array([1,2,3], dtype=np.int8)
#print(type(from_list[0]))

#2D Array 
'''from_list=np.array([[1,2,3],[4,5,6]], dtype=np.int8)
array_2d=np.array((np.arange(0,8,2), np.arange(1,8,2)))
print(my_array.shape)
print(array_2d.shape)
array_2d= array_2d.reshape(2,1,4)
print(array_2d)'''


#empty arrays
'''empty_array= np.zeros((2,2))
empty_array= np.ones((2,2))
empty_array= np.empty((2,2)) #returns random values for 3d array
print(empty_array)

eye_array=np.eye(3)
eye_array[eye_array ==0] = 2
eye_array[eye_array <2] = 9
eye_array[1:] = 3
eye_array[1:, :2] = 4
print(eye_array)'''

#Sorting arrays
eye_array=np.eye(3)

sorted_array= np.sort(eye_array, axis=0)
print(sorted_array)

#Copy arrays (View changes the orignal array. Copy dosent)
my_view=sorted_array.view()
my_copy=sorted_array.copy()

# my_view[:] = 4
#print(my_view, "\n") 

my_copy[:] = 4
print(my_copy, "\n")
print(sorted_array)

#View only changes values changing shape of view will have no effect on orignal array
my_view= my_view.reshape((3,3,1))
print(my_view,"\n")
print(sorted_array)

