##### Udacity 
####   Intro to Machine Learning
###     Lesson 3--Decision Trees
##       Decision Tree Accuracy Quiz
# https://www.udacity.com/course/viewer#!/c-ud120/l-2258728540/e-2441028547/m-2962588651

import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()



#################################################################################


########################## DECISION TREE #################################


#### your code goes here

from sklearn import tree
from sklearn.metrics import accuracy_score

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)



acc = accuracy_score(labels_test,pred)  ### you fill this in!
### be sure to compute the accuracy on the test set


    
def submitAccuracies():
  return {"acc":round(acc,3)}

# From Udacity: Good job! Your output matches our solution.
# Here's your output:
# {'acc': 0.908}




