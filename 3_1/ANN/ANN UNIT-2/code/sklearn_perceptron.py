# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 21:54:45 2023

@author: kgnan
"""

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
#
# Load the data set
#
bc = datasets.load_breast_cancer()
X = bc.data
y = bc.target

#
# Create training and test split
#
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)

#sklearn perceptron
prcptrn = Perceptron()
#
# Fit the model
#
prcptrn.fit(X_train, y_train)
#
# Score the model
#
y_pred=prcptrn.predict(X_test)

print(y_pred)
print(accuracy_score(y_test,y_pred))
#print(prcptrn.score(X_train, y_train))
print("accuracy=",prcptrn.score(X_test, y_test))










