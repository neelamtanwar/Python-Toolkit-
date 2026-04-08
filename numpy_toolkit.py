import numpy as np
#arr1 = np.array([1,2,3,4,5]) #creating a 1D array
#print(arr1)  #printing the array
#print(type(arr1)) #printing the type of the array
#print(arr1.shape) #printing the shape of the array
#print(arr1.ndim) #printing the dimemsion of the array
#print(arr1.dtype) #printing the data type of the array
#arr2 = np.array([[1,2,3],[4,5,6]]) #creating a 2D array 
#print(arr2) #printing the array
#print((type(arr1)),(arr2.shape),(arr2.ndim),(arr2.dtype)) #printing the type, shape, dimension and data type of the array)
#arr3 = np.zeros((3,3)) #creating a 2d array of zeros
#print(arr3) #printing the array
#arr4 = np.ones((4,3)) #creating a 3d array of ones
#print(arr4) #printing the array
#print(np.__version__) #version of numpy
#print(np.show_config()) #configuration of numpy
#arrzero = np.zeros(10)
#print(arrzero) #printing the array of zeros
#arrzero[4] = 5 #changing the value of the 5th element to 5 
#print(arrzero) #printing the modified array
#arrsizebw = np.arange(30,50) #creating a 1D array of integer from 30 to 49
#print(arrsizebw) #printing the array
#arrsizebwstep = np.arange(30,60,5) #createing a 1d array of int from 30 to 59 with step of 5
#print(arrsizebwstep) #printing the array 
#arrverse = np.arange(20)  #creating a 1D array of integers from 0 to 19
#print(arrverse)
#arrverse = arrverse[::-1] #reversing the array 
#print(arrverse) #printing the reversed array
areverse1 =  np.arange(40) #creating a 1D array of integers from 0 to 39
#areverse1 =areverse1[0:0:-2] #reversing the array with step of 2 where start and stop at index 0 creates empty output 
#print(areverse1) 
areverse11 = areverse1[::-2]
print(areverse11) 