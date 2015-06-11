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


class SVM(object):
    def __init__(self, kernel='linear', learning_rate=0.05):
        self.kernel = kernel
        self.learning_rate = learning_rate

    def fit(self, X, y):
        kernel = self.kernel
        learning_rate = self.learning_rate
        N = len(X)
        X = np.c_[X, np.ones(N)]
        L = np.zeros((N, 1))

        if kernel == 'linear':
            kernel = lambda x, y: np.dot(x, y)

        for k in range(1000):
            for i in range(N):
                dL_i = 1. - np.dot(np.atleast_2d(y[i] * L.reshape(-1) * y),
                                kernel(np.atleast_2d(X[i]), X.T).T)[0][0]
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

        self.support_vectors = support_vectors
        self.X_train = X
        self.y_train = y
        self.w = w

    def visualize(self):
        support_vectors = self.support_vectors
        X = self.X_train
        y = self.y_train
        w = self.w
        N = len(X)
        f = lambda x, w, b: - (w[0] / w[1]) * x - (b / w[1])

        # w's 3rd index is b
        b = w[2]
        w = np.delete(w, 2, 0)

        # visalize train data
        for i in range(0, N):
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


def test_svm():
    X, y = dataset_fixed_cov()
    clf = SVM()
    clf.fit(X, y)
    clf.visualize()


if __name__ == '__main__':
    test_svm()
