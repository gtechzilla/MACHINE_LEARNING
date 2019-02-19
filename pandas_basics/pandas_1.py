import pandas as pd
#reading data from csv files using pandas
#this returns a data type called dataframes
X=pd.read_csv("data.csv",header=None)
#to check the returned data type
print(type(X))
#gives us info about our data
print(X.info())
#gives us a sneak peek of the data contained by printing the first few rows
print(X.head())
