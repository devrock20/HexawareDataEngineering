#!/usr/bin/env python
# coding: utf-8

# ### 1. How to import pandas and check the version?

# ##### solution:

# In[ ]:





# ### 2. How to create a series from a list, numpy array and dict?

# ##### Input:
import numpy as np
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
# ##### solution:

# In[ ]:





# ### 3. How to convert the index of a series into a column of a dataframe?

# ##### Input:
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)
# ##### solution:

# In[ ]:





# ### 4. How to combine many series to form a dataframe?

# ##### Input:
import numpy as np
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
# ##### solution:

# In[ ]:





# ### 5. How to assign name to the series’ index?

# ##### Input:
Give a name to the series ser calling it ‘alphabets’.

ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
# ##### solution:

# In[ ]:





# ### 6. How to get the items of series A not present in series B?

# ##### Input:
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
# ##### solution:

# In[ ]:





# ### 7. How to get the items not common to both series A and series B?

# ##### Input:
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
# ##### solution:

# In[ ]:





# ### 8. How to get the minimum, 25th percentile, median, 75th, and max of a numeric series?

# ##### Input:
ser = pd.Series(np.random.normal(10, 5, 25))
# ##### solution:

# In[ ]:





# ### 9. How to get frequency counts of unique items of a series?

# ##### Input:
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
# ##### solution:

# In[ ]:





# ### 10. How to keep only top 2 most frequent values as it is and replace everything else as ‘Other’?

# ##### Input:
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))
# ##### solution:

# In[ ]:





# ### 11. How to bin a numeric series to 10 groups of equal size?

# ##### Input:
ser = pd.Series(np.random.random(20))
# ##### solution:

# In[ ]:





# ### 12. How to convert a numpy array to a dataframe of given shape? (L1)

# ##### Input:
Reshape the series ser into a dataframe with 7 rows and 5 columns

ser = pd.Series(np.random.randint(1, 10, 35))
# ##### solution:

# In[ ]:





# ### 13. How to find the positions of numbers that are multiples of 3 from a series?

# ##### Input:
ser = pd.Series(np.random.randint(1, 10, 7))
# ##### solution:

# In[ ]:





# ### 14. How to extract items at given positions from a series

# ##### Input:
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
# ##### solution:

# In[ ]:





# ### 15. How to stack two series vertically and horizontally ?

# ##### Input:
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))
# ##### solution:

# In[ ]:





# ### 16. How to get the positions of items of series A in another series B?

# ##### Input:
ser1 = pd.Series([10, 9, 6, 5, 3, 1, 12, 8, 13])
ser2 = pd.Series([1, 3, 10, 13])
# ##### solution:

# In[ ]:





# ### 17. How to compute the mean squared error on a truth and predicted series?

# ##### Input:
truth = pd.Series(range(10))
pred = pd.Series(range(10)) + np.random.random(10)
# ##### solution:

# In[ ]:





# ### 18. How to convert the first character of each element in a series to uppercase?

# ##### Input:
ser = pd.Series(['how', 'to', 'kick', 'ass?'])
# ##### solution:

# In[ ]:





# ### 19. How to calculate the number of characters in each word in a series?

# ##### Input:
ser = pd.Series(['how', 'to', 'kick', 'ass?'])
# ##### solution:

# In[ ]:





# ### 20. How to compute difference of differences between consequtive numbers of a series?

# ##### Input:
ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])
# ##### solution:

# In[ ]:





# ### 21. How to convert a series of date-strings to a timeseries?

# ##### Input:
ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])
# ##### solution:

# In[ ]:





# ### 22. How to get the day of month, week number, day of year and day of week from a series of date strings?

# ##### Input:
ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])
# ##### solution:

# In[ ]:





# ### 23. How to convert year-month string to dates corresponding to the 4th day of the month?

# ##### Input:
ser = pd.Series(['Jan 2010', 'Feb 2011', 'Mar 2012'])
# ##### solution:

# In[ ]:





# ### 24. How to filter words that contain atleast 2 vowels from a series?

# ##### Input:
ser = pd.Series(['Apple', 'Orange', 'Plan', 'Python', 'Money'])
# ##### solution:

# In[ ]:





# ### 25. How to filter valid emails from a series?

# ##### Input:
emails = pd.Series(['buying books at amazom.com', 'raeses@egypt.com', 'matt@xyt.co', 'xyz@abc.com'])
pattern ='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'
# ##### solution:

# In[ ]:





# ### 26. How to get the mean of a series grouped by another series?

# ##### Input:
fruit = pd.Series(np.random.choice(['apple', 'banana', 'carrot'], 10))
weights = pd.Series(np.linspace(1, 10, 10))
print(weight.tolist())
print(fruit.tolist())
#> [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
#> ['banana', 'carrot', 'apple', 'carrot', 'carrot', 'apple', 'banana', 'carrot', 'apple', 'carrot']
# ##### solution:

# In[ ]:





# ### 27. How to compute the euclidean distance between two series?

# ##### Input:
p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
# ##### solution:

# In[ ]:





# ### 28. How to find all the local maxima (or peaks) in a numeric series?

# ##### Input:
ser = pd.Series([2, 10, 3, 4, 9, 10, 2, 7, 3])
# ##### solution:

# In[ ]:





# ### 29. How to replace missing spaces in a string with the least frequent character?

# ##### Input:
my_str = 'dbc deb abed gade'
# ##### solution:

# In[ ]:





# ### 30. How to create a TimeSeries starting ‘2000-01-01’ and 10 weekends (saturdays) after that having random numbers as values?

# ##### solution:

# In[ ]:





# ### 31. How to fill an intermittent time series so all missing dates show up with values of previous non-missing date?

# ##### Input:
ser = pd.Series([1,10,3,np.nan], index=pd.to_datetime(['2000-01-01', '2000-01-03', '2000-01-06', '2000-01-08']))
print(ser)
#> 2000-01-01     1.0
#> 2000-01-03    10.0
#> 2000-01-06     3.0
#> 2000-01-08     NaN
#> dtype: float64
# ##### solution:

# In[ ]:





# ### 32. How to compute the autocorrelations of a numeric series?

# ##### Input:
ser = pd.Series(np.arange(20) + np.random.normal(1, 10, 20))
# ##### solution:

# In[ ]:





# ### 33. How to import only every nth row from a csv file to create a dataframe?

# ##### Input:
Import every 50th row of BostonHousing dataset as a dataframe.
csv file: "BostonHousing.csv"
# ##### solution:

# In[ ]:





# ### 34. How to change column values when importing csv to a dataframe?

# ##### Input:
Import the boston housing dataset, but while importing change the 'medv' (median house value) column so that values < 25 becomes ‘Low’ and > 25 becomes ‘High’.
csv file: "BostonHousing.csv"
# ##### solution:

# In[ ]:





# ### 35. How to create a dataframe with rows as strides from a given series?

# ##### Input:
L = pd.Series(range(15))
# ##### solution:

# In[ ]:





# ### 36. How to import only specified columns from a csv file?

# ##### Input:
Import ‘crim’ and ‘medv’ columns of the BostonHousing dataset as a dataframe.
csv file: "BostonHousing.csv"
# ##### solution:

# In[ ]:





# ### 37. How to get the nrows, ncolumns, datatype, summary stats of each column of a dataframe? Also get the array and list equivalent.

# ##### Input:
Get the number of rows, columns, datatype and summary statistics of each column of the Cars93 dataset. 
Also get the numpy array and list equivalent of the dataframe.
csv file: 'Cars93_miss.csv'
# ##### solution:

# In[ ]:





# ### 38. How to extract the row and column number of a particular cell with given criterion?

# ##### Input:
csv file: df = 'Cars93_miss.csv'

Which manufacturer, model and type has the highest Price? What is the row and column number of the cell with the highest Price value?
# ##### solution:

# In[ ]:





# ### 39. How to rename a specific columns in a dataframe?

# ##### Input:
Rename the column Type as CarType in df and replace the ‘.’ in column names with ‘_’.
csv file: df = 'Cars93_miss.csv'
# ##### solution:

# In[ ]:





# ### 40. How to check if a dataframe has any missing values?

# ##### Input:
csv file: 'Cars93_miss.csv'
# ##### solution:

# In[ ]:





# ### 41. How to count the number of missing values in each column?

# ##### Input:
Count the number of missing values in each column of df. Which column has the maximum number of missing values?
csv file: 'Cars93_miss.csv'
# ##### solution:

# In[ ]:





# ### 42. How to replace missing values of multiple numeric columns with the mean?

# ##### Input:
Replace missing values in Min.Price and Max.Price columns with their respective mean.
csv file: 'Cars93_miss.csv'
# ##### solution:

# In[ ]:





# ### 43. How to use apply function on existing columns with global variables as additional arguments?

# ##### Input:
use apply method to replace the missing values in Min.Price with the column’s mean and those in Max.Price with the column’s median.
csv file: 'Cars93_miss.csv'
# ##### solution:

# In[ ]:





# ### 44. How to select a specific column from a dataframe as a dataframe instead of a series?

# ##### Input:
Get the first column (a) in df as a dataframe (rather than as a Series).

df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
# ##### solution:

# In[ ]:





# ### 45. How to change the order of columns of a dataframe?

# ##### Input:
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))

1. In df, interchange columns 'a' and 'c'.
2. Create a generic function to interchange two columns, without hardcoding column names.
3. Sort the columns in reverse alphabetical order, that is colume 'e' first through column 'a' last.
# ##### solution:

# In[ ]:





# ### 46. How to set the number of rows and columns displayed in the output?

# ##### Input:
Change the pamdas display settings on printing the dataframe df it shows a maximum of 10 rows and 10 columns.
csv file: df = 'Cars93_miss.csv'
# ##### solution:

# In[ ]:





# ### 47. How to format or suppress scientific notations in a pandas dataframe?

# ##### Input:
Suppress scientific notations like ‘e-03’ in df and print upto 4 numbers after decimal.
df = pd.DataFrame(np.random.random(4)**10, columns=['random'])
# ##### solution:

# In[ ]:





# ### 48. How to format all the values in a dataframe as percentages?

# ##### Input:
Format the values in column 'random' of df as percentages.
df = pd.DataFrame(np.random.random(4), columns=['random'])
# ##### solution:

# In[ ]:





# ### 49. How to filter every nth row in a dataframe?

# ##### Input:
From df, filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).
csv file: 'Cars93_miss.csv'
# ##### solution:

# In[ ]:





# ### 50. How to create a primary key index by combining relevant columns?

# ##### Input:
Replace NaNs with ‘missing’ in columns 'Manufacturer', 'Model' and 'Type' and create a index as a combination of these three columns and check if the index is a primary key.
csv file: 'Cars93_miss.csv'
# ##### solution:

# In[ ]:





# ### 51. How to get the row number of the nth largest value in a column?

# ##### Input:
Find the row position of the 5th largest value of column 'a' in df.
df = pd.DataFrame(np.random.randint(1, 30, 30).reshape(10,-1), columns=list('abc'))
# ##### solution:

# In[ ]:





# ### 52. How to find the position of the nth largest value greater than a given value?

# ##### Input:
find the position of the 2nd largest value greater than the mean.
ser = pd.Series(np.random.randint(1, 100, 15))
# ##### solution:

# In[ ]:





# ### 53. How to get the last n rows of a dataframe with row sum > 100?

# ##### Input:
Get the last two rows of df whose row sum is greater than 100.
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
# ##### solution:

# In[ ]:





# ### 54. How to find and cap outliers from a series or dataframe column?

# ##### Input:
Replace all values of ser in the lower 5%ile and greater than 95%ile with respective 5th and 95th %ile value.
ser = pd.Series(np.logspace(-2, 2, 30))
# ##### solution:

# In[ ]:





# ### 55. How to reshape a dataframe to the largest possible square after removing the negative values?

# ##### Input:
Reshape df to the largest possible square with negative values removed. Drop the smallest values if need be. The order of the positive numbers in the result should remain the same as the original.
df = pd.DataFrame(np.random.randint(-20, 50, 100).reshape(10,-1))
# ##### solution:

# In[ ]:





# ### 56. How to swap two rows of a dataframe?

# ##### Input:
Swap rows 1 and 2 in df.
df = pd.DataFrame(np.arange(25).reshape(5, -1))
# ##### solution:

# In[ ]:





# ### 57. How to reverse the rows of a dataframe?

# ##### Input:
Reverse all the rows of dataframe df.
df = pd.DataFrame(np.arange(25).reshape(5, -1))
# ##### solution:

# In[ ]:





# ### 58. How to create one-hot encodings of a categorical variable (dummy variables)?

# ##### Input:
Get one-hot encodings for column 'a' in the dataframe df and append it as columns.
df = pd.DataFrame(np.arange(25).reshape(5,-1), columns=list('abcde'))
# ##### solution:

# In[ ]:





# ### 59. Which column contains the highest number of row-wise maximum values?

# ##### Input:
Obtain the column name with the highest number of row-wise maximum’s in df.
df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1))
# ##### solution:

# In[ ]:





# ### 60. How to create a new column that contains the row number of nearest column by euclidean distance?

# ##### Input:
Create a new column such that, each row contains the row number of nearest row-record by euclidean distance.
df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1), columns=list('pqrs'), index=list('abcdefghij'))
# ##### solution:

# In[ ]:





# ### 61. How to know the maximum possible correlation value of each column against other columns?

# ##### Input:
Compute maximum possible absolute correlation value of each column against other columns in df.
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1), columns=list('pqrstuvwxy'), index=list('abcdefgh'))
# ##### solution:

# In[ ]:





# ### 62. How to create a column containing the minimum by maximum of each row?

# ##### Input:
Compute the minimum-by-maximum for every row of df.
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))
# ##### solution:

# In[ ]:





# ### 63. How to create a column that contains the penultimate value in each row?

# ##### Input:
Create a new column 'penultimate' which has the second largest value of each row of df.
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))
# ##### solution:

# In[ ]:





# ### 64. How to normalize all columns in a dataframe?

# ##### Input:
1. Normalize all columns of df by subtracting the column mean and divide by standard deviation.
2. Range all columns of df such that the minimum value in each column is 0 and max is 1.
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))
# ##### solution:

# In[ ]:





# ### 65. How to compute the correlation of each row with the suceeding row?

# ##### Input:
Compute the correlation of each row of df with its succeeding row.
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))
# ##### solution:

# In[ ]:





# ### 66. How to replace both the diagonals of dataframe with 0?

# ##### Input:
df = pd.DataFrame(np.random.randint(1,100, 100).reshape(10, -1))
# ##### solution:

# In[ ]:





# ### 67. How to get the particular group of a groupby dataframe by key?

# ##### Input:
This is a question related to understanding of grouped dataframe. From df_grouped, get the group belonging to 'apple' as a dataframe.

df = pd.DataFrame({'col1': ['apple', 'banana', 'orange'] * 3,
                   'col2': np.random.rand(9),
                   'col3': np.random.randint(0, 15, 9)})

df_grouped = df.groupby(['col1'])
# ##### solution:

# In[ ]:





# ### 68. How to get the n’th largest value of a column when grouped by another column?

# ##### Input:
In df, find the second largest value of 'taste' for 'banana'

df = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                   'rating': np.random.rand(9),
                   'price': np.random.randint(0, 15, 9)})
# ##### solution:

# In[ ]:





# ### 69. How to compute grouped mean on pandas dataframe and keep the grouped column as another column (not index)?

# ##### Input:
In df, Compute the mean price of every fruit, while keeping the fruit as another column instead of an index.

df = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                   'taste': np.random.rand(9),
                   'price': np.random.randint(0, 15, 9)})
# ##### solution:

# In[ ]:





# ### 70. How to join two dataframes by 2 columns so they have only the common rows?

# ##### Input:
Join dataframes df1 and df2 by ‘fruit-pazham’ and ‘weight-kilo’.

df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['high', 'medium', 'low'] * 3,
                    'price': np.random.randint(0, 15, 9)})

df2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
                    'kilo': ['high', 'low'] * 3,
                    'price': np.random.randint(0, 15, 6)})
# ##### solution:

# In[ ]:





# ### 71. How to remove rows from a dataframe that are present in another dataframe?

# ##### Input:
From df1, remove the rows that are present in df2. All three columns must be the same.

df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['high', 'medium', 'low'] * 3,
                    'price': np.random.randint(0, 15, 9)})

df2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
                    'kilo': ['high', 'low'] * 3,
                    'price': np.random.randint(0, 15, 6)})
# ##### solution:

# In[ ]:





# ### 72. How to get the positions where values of two columns match?

# ##### Input:
df = pd.DataFrame({'fruit1': np.random.choice(['apple', 'orange', 'banana'], 10),
                    'fruit2': np.random.choice(['apple', 'orange', 'banana'], 10)})
# ##### solution:

# In[ ]:





# ### 73. How to create lags and leads of a column in a dataframe?

# ##### Input:
Create two new columns in df, one of which is a lag1 (shift column a down by 1 row) of column ‘a’ and the other is a lead1 (shift column b up by 1 row).

df = pd.DataFrame(np.random.randint(1, 100, 20).reshape(-1, 4), columns = list('abcd'))
# ##### solution:

# In[ ]:





# ### 74. How to get the frequency of unique values in the entire dataframe?

# ##### Input:
df = pd.DataFrame(np.random.randint(1, 10, 20).reshape(-1, 4), columns = list('abcd'))
# ##### solution:

# In[ ]:





# ### 75. How to split a text column into two separate columns?

# ##### Input:
Split the string column in df to form a dataframe with 3 columns as shown.

df = pd.DataFrame(["STD, City    State",
"33, Kolkata    West Bengal",
"44, Chennai    Tamil Nadu",
"40, Hyderabad    Telengana",
"80, Bangalore    Karnataka"], columns=['row'])
# ##### solution:

# In[ ]:




