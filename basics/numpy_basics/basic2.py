#Dot product
import numpy as np
a=np.array([1,2])
b=np.array([2,1])

#using the zip method,we separate the vector components and add them individually
#we the multiply simillar components of the zip elements
dot =0
for e,f in zip(a,b):
    dot +=e*f
print(dot)

#in numpy arrays we can multiply two vectors together,they must be of the same order
#in the previous example we multiplied a scalar with a vector
print(a*b)

#we can find the dot product by also
dot1=a*b
print(np.sum(dot1))

#sum can also be used as an instance of the array object/class
print((a*b).sum())

#easiset way to find the dot product,we use the dot function of numpy lib
print(np.dot(a,b))
