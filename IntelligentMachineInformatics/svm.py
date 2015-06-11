#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from sklearn.datasets import load_digits
from matplotlib.pyplot import *

learning_rate = 0.05

def f(x1, w, b):
    return - (w[0] / w[1]) * x1 - (b / w[1])

def kernel(x, y):
    return np.dot(x, y)

def dL(i, X, y, L, N):
    ans = 0
    for j in range(0, N):
        ans += L[j] * y[i] * y[j] * kernel(X[i], X[j])
    return 1 - ans

data = np.loadtxt('data/svm_data.txt')
N = len(data)
X = np.c_[data[:, :2], np.ones(N)]
y = data[:, 2]
L = np.zeros((N, 1))

for i in range(1000):
    for i in range(N):
        L[i] = L[i] + learning_rate * dL(i, X, y, L, N)
        if L[i] < 0:
            L[i] = 0
        elif L[i] > np.inf:
            L[i] = np.inf

    S = []
    for i in range(N):
        if L[i] < 0.00001:
            continue
        S.append(i)

    w = np.zeros(3)
    for n in S:
        w += L[n] * y[n] * X[n]

   # wの3次元目は拡張次元のbとなる。
    b = w[2]
    np.delete(w, 2, 0)

    # 訓練データを描画
    for i in range(0,N):
        if y[i] > 0:
            plot(X[i][0],X[i][1], 'rx')
        else:
            plot(X[i][0],X[i][1], 'bx')

    # サポートベクトルを描画
    for n in S:
        scatter(X[n,0], X[n,1], s=80, c='y', marker='o')

    # 識別境界を描画
    x1 = np.linspace(-6, 6, 1000)
    x2 = [f(x, w, b) for x in x1]
    plot(x1, x2, 'g-')

    xlim(-6, 6)
    ylim(-6, 6)
    show()

    b = w[2]
    np.delete(w, 2, 0)