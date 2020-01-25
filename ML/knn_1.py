# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 15:53:38 2019

@author: ojhas
"""

import sklearn
import numpy as np
from sklearn.datasets import load_breast_cancer
cancer= load_breast_cancer()
print ("{}".format(cancer.keys()))

help(sklearn.datasets)

{n : v for n,v in zip(cancer.target_names, np.bincount(cancer.target))}




from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

from sklearn.neighbors import  KNeighborsClassifier
cancer= load_breast_cancer()
print (cancer.data)
neighbors_settings = range(1, 11)
X_train, X_test,y_train, y_test = train_test_split(cancer.data, 
                                                   cancer.target, 
                                       stratify=cancer.target,
                                       random_state=66)


training_accuracy = []
test_accuracy = []
for neigh in neighbors_settings:
    clf = KNeighborsClassifier(n_neighbors=neigh)
    clf.fit(X_train, y_train)
    training_accuracy.append(clf.score(X_train, y_train))
    test_accuracy.append(clf.score(X_test,y_test))

import matplotlib.pyplot as plt
plt.plot(neighbors_settings, training_accuracy, label="training accuracy")
plt.plot(neighbors_settings, test_accuracy, label="test accuracy")
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()





fig, axes = plt.subplots(1, 3, figsize=(10, 3))
for n_neighbors, ax in zip([1, 3, 9], axes):
    # the fit method returns the object self, so we can instantiate
    # and fit in one line
    clf = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X, y)
    plt.plots.plot_2d_separator(clf, X, fill=True, eps=0.5, ax=ax, alpha=.4)
    plt.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)
    ax.set_title("{} neighbor(s)".format(n_neighbors))
    ax.set_xlabel("feature 0")
    ax.set_ylabel("feature 1")
axes[0].legend(loc=3)



"""
KNN Regressor
"""
from sklearn.neighbors import KNeighborsRegressor
X_train,X_test, y_train,y_test = train_test_split(sklearn.datasets.load_diabetes().data, sklearn.datasets.load_diabetes().target , random_state=0)

for i in range(1,40):
    reg= KNeighborsRegressor(n_neighbors=i)
    reg.fit(X_train, y_train)
    print (reg.score(X_test,y_test))
    
    
    
"""

Liniear Models

"""

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

bds =load_boston()
X_train,X_test,y_train,y_test = train_test_split(bds.data, bds.target, random_state=0)
lr = LinearRegression().fit(X_train, y_train)
lr.predict(X_test)
lr.score(X_test, y_test)
lr.coef_

len(bds.feature_names)


import pandas as pd
df=pd.DataFrame(data=bds.data, columns=bds.feature_names)
df["target"]=pd.Series(bds.target)
df


"""
Ridge Regression: A linear model regression
"""

from sklearn.linear_model import Ridge
ridge = Ridge()
ridge.fit(X_train, y_train)
ridge.score(X_test, y_test)





import seaborn as sn
df.corr()
sn.heatmap(df.corr(), annot=True)









