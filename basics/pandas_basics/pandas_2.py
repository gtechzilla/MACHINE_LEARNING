import pandas as pd
X=pd.read_csv("data.csv",header=None)
M=X.as_matrix()
#though we can have a mtrix data type,the above function returns a numpy array
print(type(M))
#to output a column of a file(file X) we use the column index,they start from zero
'''
*****************************NB********************************
********IN NUMPY,X[0] REFERS TO THE FIRST ROW******************
********IN PANDAS,X[0], REFERS TO THE 1ST COLUMN***************
'''
#this outputs a column
print(X[1])
#X[],will output a new data type called SERIES
#SERIES,is the data type used for 1 dimension objects in pandas
#DATA_FRAMES,this is the data type used for 2 dimension objects in pandas
print(type(X[0]))
'''**********HOW DO YOU WORK WITH ROWS IN PANDAS????***********'''
#to return a row,we can use two methods,iloc[] or ix[]
#the resultin data type is still a series(since its in 1D)
print(X.iloc[0])
print(X.ix[1])

#to select multiple columns
#this will output,the 0th and 2nd columns respectively of the file X
print(X[[0,2 ]])

#other section criterias are
#to select only values of ROWS in th 0th column,where all the data is less than 5
#in our case it will return false since we dont meet that criteria
print(X[0] <5)
