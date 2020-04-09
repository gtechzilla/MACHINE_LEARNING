# shows how linear regression analysis can be applied to 1-dimensional data
#
# notes for this course can be found at:
# https://deeplearningcourses.com/c/data-science-linear-regression-in-python
# https://www.udemy.com/data-science-linear-regression-in-python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#read the data from csv file
df=pd.read_csv('sac.csv')

#function to convert our data into matrix/array
def my_data(df):
    #get the indicated columns from the data
	a=df[['sq__ft','price']]
    #slice data from the sq__ft that has a size 0
	b=a.loc[a['sq__ft']==0]
	c=b.index

	c=np.array(c)
	a=a.drop(c)
	'''d=a.loc[a['sq__ft']>5000]
	d=d.index
	d=np.array(d)
	a=a.drop(d)'''
	x=a['sq__ft']
	y=a['price']


	x=x.as_matrix()
	y=y.as_matrix()
	
	return (x,y)

# load the data
X,Y=my_data(df)

# let's turn X and Y into numpy arrays since that will be useful later
X = np.array(X)
Y = np.array(Y)


# let's plot the data to see what it looks like
plt.scatter(X, Y)
plt.show()


# apply the equations we learned to calculate a and b

# denominator is common
# note: this could be more efficient if
#       we only computed the sums and means once
denominator = X.dot(X) - X.mean() * X.sum()
a = ( X.dot(Y) - Y.mean()*X.sum() ) / denominator
b = ( Y.mean() * X.dot(X) - X.mean() * X.dot(Y) ) / denominator

# let's calculate the predicted Y
Yhat = a*X + b

# let's plot everything together to make sure it worked
plt.scatter(X, Y)
plt.plot(X, Yhat)
plt.show()

# determine how good the model is by computing the r-squared
d1 = Y - Yhat
d2 = Y - Y.mean()
r2 = 1 - d1.dot(d1) / d2.dot(d2)
print("the r-squared is:", r2)
