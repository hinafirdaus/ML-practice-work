## this program is for learning of pandas by some list of tracking app to count steps
import pandas as pd
import numpy as np


#reading a dataset using pandas
print ("reading and displaying iris dataset using the pandas library")
iris_data = pd.read_csv('F:\dissertation\python intel ML\Intel-ML101_Class1\data\Iris_Data.csv')
print (iris_data.head(n=5))  #head and tail can be use to dispaly some part of dataset
print("__________________________________________________________________________")
print (iris_data.iloc[:4])  #integer location can also help in viewing some part of the dataset

print("__________________________________________________________________________")

#data can be reassigned to a new column in the DataFrame

iris_data['sepal_area'] = iris_data.sepal_length * iris_data.sepal_width
print (iris_data.iloc[:5,-2:])

#finding mean, median, and mode of the DataFrame column
print("__________________________________________________________________________")
print ("mean of the iris dataset sepal width columns:\n ",iris_data.sepal_width.mean())
print("__________________________________________________________________________")
print ("median of the iris dataset sepal area columns:\n ", iris_data.sepal_area.median())
print("__________________________________________________________________________")
print ("mode of the iris dataset petal length columns:\n ",iris_data.petal_length.mode())
print("__________________________________________________________________________")
print ("standard deviation of the iris dataset petal length columns:\n ",iris_data.petal_length.std())
print("__________________________________________________________________________")
print ("variance of the iris dataset sepal length columns:\n ",iris_data.sepal_length.var())
print("__________________________________________________________________________")
print ("standard error of the mean of the iris dataset petal_width columns:\n ",iris_data.petal_width.sem())
#quantile of a dataset
print("__________________________________________________________________________")
print("quantile of dataset\n",iris_data.quantile(0))


print("__________________________________________________________________________")
#using function on the rows or column of a DataFrame or Series

iris_data['abbrevated'] = (iris_data.species.apply(lambda x: x.replace('Iris-','')))
print (iris_data.iloc[:5,-3:])

print("__________________________________________________________________________")
#concatinating rows in DataFrame along either dimensions

concatin = pd.concat([iris_data.iloc[:2],iris_data.iloc[-2:]])
print (concatin.iloc[:5,-5:])

print("__________________________________________________________________________")
#groupby method to calculate aggregated DataFrame

grp_sizes = (iris_data.groupby('abbrevated').size())
print(grp_sizes)

#description of the dataset whole calculation
print("__________________________________________________________________________")
print (iris_data.describe())










