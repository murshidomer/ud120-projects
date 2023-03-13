#!/usr/bin/python3

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time

sys.path.append("../tools/")
from tools.email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

clf = SVC(kernel="linear")
clf.fit(features_train, labels_train)
predictions = clf.predict(features_test)
accuracy = accuracy_score(labels_test, predictions)
print(accuracy)
#########################################################

#########################################################
'''
You'll be Provided similar code in the Quiz
But the Code provided in Quiz has an Indexing issue
The Code Below solves that issue, So use this one
'''
# features_train = features_train[:int(len(features_train)/100)]
# labels_train = labels_train[:int(len(labels_train)/100)]


# clf = SVC(kernel="linear")
# clf = SVC(kernel="rbf", C=10)
clf = SVC(kernel="rbf", C=10000)
t0 = time()
clf.fit(features_train, labels_train)
print("training time", round(time() - t0, 3), "s")

t0 = time()
prediction = clf.predict(features_test)
print("prediction time", round(time() - t0, 3), "s")
acc = accuracy_score(labels_test, prediction)
print(acc)

element10 = prediction[10]
element26 = prediction[26]
element50 = prediction[50]

print("element 10:{},element 26:{},element 50:{}".format(element10, element26, element50))

chrisEmailCount = [value for value in prediction if value == 1]

print(len(chrisEmailCount))
#########################################################
