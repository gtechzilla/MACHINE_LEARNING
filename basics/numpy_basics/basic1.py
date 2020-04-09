#NUMPY
import numpy as np

#crete a list
L=[1,2,3]

#convert the list to a numpy array
#use the numpy array function
#we ccan loop through both elements in a list and an array
A=np.array([1,2,3])
for e in L:
    print (e)

for e in A:
    print (e)

#lets use various list methods on arrays
#they wont work,so why do we need an array
'''A.append(4)
A=A+[4]

L.append(4)
L=L+[5]
'''
#lets do some vector addition
#in vector addition y components and x components are treated separately

#using lists
#adding the list to itself
print(L+L)
#to add wach components of a list separately,we use a loop
L2=[]
for e in L:
    L2.append(e+e)
print(L2)
#what about multiplying each element of a list
#it concatnates
print(2*L)

#lets try that with a numpy arrays
#arrays work element wise
#each element in the array is treated separately
print(A+A)

#multiplying an array with a scalar
print(2*A)

#lets try some mathematical functions
print(np.log(A))
print(np.exp(A))
print(np.sqrt(A))

'''Conclusion when working with vectors its more convinient to use arrays
   This is due to them working element wise.Lists can do element wise mathematical
   operations but you have to use a loop,loops make ur program slow as we shall see,
   avoid them when necessary,converting a list to an array allows us to do vector addition,
   solve matrices and othe matematical problems easily'''
