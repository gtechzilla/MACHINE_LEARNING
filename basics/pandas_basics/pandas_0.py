import numpy as np
import pandas

x=[]
for line in open('data.csv',"r"):
    row=line.split(',')
    '''for python3 wrap the map function into a list
     function to output an actual list instead of a
      list object'''
    sample= list(map(float,row))
    x.append(sample)
x=np.array(x)
#here shape is an attribute thus u dont need the brackets
#make sure u cover functions in the book or google to understand the differences
print(x.shape)
