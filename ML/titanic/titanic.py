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


import os
os.chdir("C:\\Users\\ojhas\\Documents\\PythonTrishna\\ML\\titanic")
os.listdir()

pd.set_option('display.max_columns', None)  
train = pd.read_csv("train.csv")
train.describe()


#Fillup 
train['Age'].fillna(train['Age'].median(), inplace=True)
train['Sex'] = train['Sex'].map({'female':0, 'male':1})
fig , ax= plt.subplots(1,1,figsize=(18,6))
train['Age'].unique()
sns.factorplot(x='Sex', y='Survived', data=train, kind='bar')

sns.heatmap(train.corr(), annot=True)

x_features = list(train.columns)
x_features.remove('Survived')

train[x_features]

from sklearn.naive_bayes import GaussianNB




