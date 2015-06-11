#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import numpy as np
from sklearn.datasets import load_digits
from matplotlib.pyplot import *
import matplotlib.pyplot as plt


# generate datasets
def dataset_fixed_cov():
    '''Generate 2 Gaussians samples with the same covariance matrix'''
    n, dim = 300, 2
    np.random.seed(0)
    C = np.array([[0., -0.23], [0.83, .23]])
    X = np.r_[np.dot(np.random.randn(n, dim), C),
              np.dot(np.random.randn(n, dim), C) + np.array([1, 1])]
    y = np.hstack((-np.ones(n), np.ones(n)))
    return X, y


def f(x, w, b):
    return - (w[0] / w[1]) * x - (b / w[1])


def linear_kernel(x, y):
    return np.dot(x, y)


learning_rate = 0.05
kernel = linear_kernel

X, y = dataset_fixed_cov()
N = len(X)
X = np.c_[X, np.ones(N)]
L = np.zeros((N, 1))
print('N:', N)

for k in range(1000):
    for i in range(N):
        dL_i = 1. - np.dot(np.atleast_2d(y[i] * L.reshape(-1) * y),
                           kernel(np.atleast_2d(X[i]), X.T).T)[0][0]
        # for j in range(N):
        #     dL_i -= L[j] * y[i] * y[j] * kernel(X[i], X[j])
        L[i] += learning_rate * dL_i
        if L[i] < 0:
            L[i] = 0
        elif L[i] > np.inf:
            L[i] = np.inf

support_vectors = []
for i in range(N):
    if L[i] < 1e-5:
        continue
    support_vectors.append(i)

w = np.zeros(3)
for i_sv in support_vectors:
    w += L[i_sv] * y[i_sv] * X[i_sv]

# w's 3rd index is b
b = w[2]
w = np.delete(w, 2, 0)

# visalize train data
for i in range(0,N):
    if y[i] > 0:
        plt.plot(X[i][0],X[i][1], 'ro')
    else:
        plt.plot(X[i][0],X[i][1], 'bo')

# visualize support vectors
for n in support_vectors:
    plt.scatter(X[n,0], X[n,1], s=80, marker='x')

# visualize discriminative plane
x1 = np.linspace(-6, 6, 1000)
x2 = [f(x, w, b) for x in x1]
plt.plot(x1, x2, 'g-')

plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.show()
