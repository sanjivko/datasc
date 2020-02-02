# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 22:52:04 2020

@author: ojhas
"""
def print_full(x):
    pd.set_option('display.max_rows', len(x))
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.float_format', '{:20,.2f}'.format)
    pd.set_option('display.max_colwidth', -1)
    print(x)
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')
    pd.reset_option('display.width')
    pd.reset_option('display.float_format')
    pd.reset_option('display.max_colwidth')
    
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import os
os.chdir("C:\\Users\\ojhas\\Documents\\PythonTrishna\\ML\\titanic")
print (os.listdir())

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")



train.head()


test.head()

train.shape

 

train.describe()

train.dtypes


list(train.columns)
'''
['PassengerId',
 'Survived',
 'Pclass',
 'Name',
 'Sex',
 'Age',
 'SibSp',
 'Parch',
 'Ticket',
 'Fare',
 'Cabin',
 'Embarked']
'''
sns.countplot(y="Survived", data=train)

train.Survived.value_counts()
sns.distplot(train.Pclass)


train.Sex.value_counts()

train.Sex.isna().value_counts()

sns.factorplot("Sex", "Survived", data=train, kind="bar")








