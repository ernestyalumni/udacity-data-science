##### Udacity 
####   Intro to Machine Learning
###     Lesson 3--Decision Trees
##       Decision Tree Accuracy Quiz 2 
# https://www.udacity.com/course/viewer#!/c-ud120/l-2258728540/e-2460738540/m-2935208538

import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()



########################## DECISION TREE #################################


### your code goes here--now create 2 decision tree classifiers,
### one with min_samples_split=2 and one with min_samples_split=50
### compute the accuracies on the testing data and store
### the accuracy numbers to acc_min_samples_split_2 and
### acc_min_samples_split_50, respectively

from sklearn import tree
from sklearn.metrics import accuracy_score

def DTclassify(x=features_train,y=labels_train,x_test=features_test,y_test=labels_test,min_split=2):
    clf = tree.DecisionTreeClassifier(min_samples_split=min_split)
    clf = clf.fit(x, y)
    pred = clf.predict(x_test)
    acc = accuracy_score(y_test,pred)  
    return acc

####################################################################################################
acc_min_samples_split_2  = DTclassify()
acc_min_samples_split_50 = DTclassify(min_split=50)
####################################################################################################

# Udacity:
# Good job! Your output matches our solution.
# Here's your output:
# {'acc_min_samples_split_50': 0.912, 'acc_min_samples_split_2': 0.908}


