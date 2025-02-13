'''
q1: Which type of data can be used while creating a series object in pandas?
ans: A series object in pandas can be created using various types of data such as 
lists, dictionaries, scalar values.
'''

'''
q2: Create a series having the month's number as data and assign name as their index values? 
'''
import pandas as samar
def q2():
    data = [1,2,3,4,5,6,7,8,9,10,11,12]
    index = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    series = samar.Series(data, index=index)
    return print(series)



'''
q3: Write a program to create a series object using the dictionary which store the number of students 
in fresh batch groups ( MatMIE, Mat DAIS, COMIE, COMEC)?'''

def q3():
    d = {'MatMIE': 45, 
         'Mat DAIS': 550, 
         'COMIE': 60, 
         'COMEC': 40
         }
    series_object=samar.Series(d)
    return print(series_object)

'''q4: Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']'''
import numpy as np

def q4():
    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
                 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
                 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    df = samar.DataFrame(exam_data, index=labels)
    return print(df)

'''
q5: Write a Pandas program to select the rows where the number of attempts in the examination is greater than 2.

Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

'''

def q5():
    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
                 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
                 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    d = samar.DataFrame(exam_data, labels)
    sorted = d[d['attempts'] > 2]
    return print(sorted)


for i, j in zip([2, 3, 4, 5], [q2, q3, q4, q5]):
    print(f"Question {i}")
    j()
    print(' ')