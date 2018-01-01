## this program is for learning of pandas by some list of tracking app to count steps
import pandas as pd
import numpy as np


step_data = [5000, 3650, 4789, 6745, 7890, 8743, 9919, 10000]
step_data.sort() #sort the unsorted list of step count
step_count = pd.Series(step_data, name ='steps') # series helps to labels the axis in 1d ndarray
print (step_count)
print (type(step_data)) # type if for analyzing the type of data we are using 
print("__________________________________________________________________________")
# generating data_range to the series of step data

step_count.index = pd.date_range('20171128', periods = 8)
print (step_count)
print ("steps on 2017 nov 29:   ", step_count['2017-11-29'])  #list can also work as dictionary
print ("steps count on index 7: ",step_count[7])  #list can work as index
print("__________________________________________________________________________")
print (step_count['2017-12'])  #selects all the step data of december from the list 
print("__________________________________________________________________________")
#we can convert the datatype by importing the numpy library

print ("step count before conversion of datatype is: ",step_count.dtype)

#conversion of int64 step_count into float type
step_count = step_count.astype(np.float64)
print ("step count after conversion of datatype is : ", step_count.dtype)
print("__________________________________________________________________________")
#creating invalid data and filling it with some values

#creating invalid data
step_count[5:7] = np.NaN

#filling the invalid data with zeroes
step_count = step_count.fillna(0.)
print ("Filling the created invalid steps count with zero: ", step_count[5:7])
print("__________________________________________________________________________")

## DataFrame can be created from lists , dictionories, and pandas series
#create a list of cycling distance data
cycledist_data = [10.7, 10.0, None, 2.0, 5.6, 10.5, 3.2, None]

#create a tuple of data
join_data = list(zip(step_data, cycledist_data))

#create the DataFrame
#in ndarray DataFrame the column name can be even changed
activity = pd.DataFrame(join_data, index=pd.date_range('20171128', periods=8),columns=['walking_step_count','cycling_dist'])
print(activity)
print("__________________________________________________________________________")
#location in dataframe of string using loc
print (activity.loc['2017-12-01'])
#location of integer using loc
print (activity.iloc[7])
#calling only column name
print ("column name using normal column calling")
print (activity['walking_step_count'])
print("__________________________________________________________________________")
#printing caolumn using object oriented approach
print ("column name printing using object oriented concepts")
print (activity.walking_step_count)
print("__________________________________________________________________________")


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

print("__________________________________________________________________________")
print ("mean of the iris dataset columns:\n ",iris_data.mean())
print("__________________________________________________________________________")
print ("median of the iris dataset columns:\n ", iris_data.median())
