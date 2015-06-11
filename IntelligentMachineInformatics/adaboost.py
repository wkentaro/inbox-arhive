#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.datasets import load_digits, load_iris, fetch_mldata
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score


h = []
h.append(KNeighborsClassifier(n_neighbors=3))
h.append(KNeighborsClassifier(n_neighbors=4))
h.append(KNeighborsClassifier(n_neighbors=5))
h.append(KNeighborsClassifier(n_neighbors=6))
h.append(LogisticRegression())
M = len(h)
print 'M:', M

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
N = len(X_train)
print 'N:', N

print('fitting')
for m in range(M):
    h[m].fit(X_train, y_train)
    print 'score:', h[m].score(X_test, y_test)

w = np.ones(N) / N
alpha = np.zeros(M)
for m in range(1, M):
    Js = []
    for m in range(M):
        # print(m, '---------------------------------------------')
        I = (h[m].predict(X_train) != y_train).astype(int)
        print 'train score:', h[m].score(X_train, y_train)
        # print 'I.sum():', I.sum()
        # print 'I.shape:', I.shape
        Ji = (w * I).sum()
        Js.append(Ji)
        # print 'J:', J
    print 'Js:', Js
    m = np.argmin(Js)
    J = Js[m]

    epsilon = J / w.sum()
    # print 'w.shape:', w.shape
    print 'w.sum(): ', w.sum()
    print 'epsilon: ', epsilon
    alpha[m] = np.log((1. - epsilon) / epsilon)

    # w_prev = w
    w = w * np.exp(alpha[m] * I)
    # dw = w - w_prev
    # print 'dw.sum():', dw.sum()

    print 'alpha:', alpha

y_pred = np.zeros(len(X_test))
for m in range(M):
    y_pred += alpha[m] * h[m].predict(X_test)
y_pred = np.sign(y_pred)
print 'alpha:', alpha
print 'score:', accuracy_score(y_test, y_pred)
