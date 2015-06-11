#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import numpy as np
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.datasets import load_digits, load_iris, fetch_mldata
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score


class AdaBoost(object):
    def __init__(self, classifiers):
        self.clfs = classifiers

    def fit(self, X, y):
        clfs = self.clfs
        M = len(clfs)
        N = len(X)

        for m in range(M):
            print('fitting:', m)
            clfs[m].fit(X, y)

        w = np.ones(N) / N
        alpha = np.zeros(M)
        for m in range(1, M):
            print('updating weight:', m)
            Js = []
            for m in range(M):
                I = (clfs[m].predict(X) != y).astype(int)
                Ji = (w * I).sum()
                Js.append(Ji)
            m = np.argmin(Js)
            J = Js[m]

            epsilon = J / w.sum()
            alpha[m] = np.log((1. - epsilon) / epsilon)

            w = w * np.exp(alpha[m] * I)

        self.alpha = alpha

    def predict(self, X):
        clfs = self.clfs
        alpha = self.alpha
        M = len(clfs)

        y_pred = np.zeros(len(X))
        for m in range(M):
            y_pred += alpha[m] * clfs[m].predict(X)
        y_pred = np.sign(y_pred)

        return y_pred

    def score(self, X, y):
        y_pred = self.predict(X)
        score = accuracy_score(y, y_pred)
        return score

dataset = fetch_mldata('MNIST original')
X, y_tmp = dataset.data, dataset.target
p = np.random.randint(0, len(X), 10000)
X, y_tmp = X[p], y_tmp[p]
y = []
for yi in y_tmp:
    if yi <= 4:
        y.append(1)
    else:
        y.append(-1)
X_train, X_test, y_train, y_test = train_test_split(X, y)

clfs = []
clfs.append(KNeighborsClassifier(n_neighbors=3))
clfs.append(KNeighborsClassifier(n_neighbors=4))
clfs.append(KNeighborsClassifier(n_neighbors=5))
clfs.append(KNeighborsClassifier(n_neighbors=6))
clfs.append(LogisticRegression())

ada = AdaBoost(classifiers=clfs)
ada.fit(X, y)
for clf in clfs:
    print('score:', m, clf.score(X_test, y_test))
score = ada.score(X_test, y_test)
print('score:', score)
