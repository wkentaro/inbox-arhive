#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split
from sklearn.datasets import fetch_mldata, load_digits, load_iris
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score

dataset = fetch_mldata('MNIST original')
# dataset = load_digits()
# dataset = load_iris()
X, y = dataset.data, dataset.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

print('just SVC ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
clf = SVC(kernel='linear', probability=True)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
score = accuracy_score(y_test, y_pred)
print('score: ', score)

print('AdaBoost ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
ada = AdaBoostClassifier(base_estimator=SVC(kernel='linear', probability=True))
ada.fit(X_train, y_train)
y_pred = ada.predict(X_test)
score = accuracy_score(y_test, y_pred)
print('score: ', score)
