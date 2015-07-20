#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division
import numpy as np
from sklearn.datasets import load_digits
from sklearn.preprocessing import binarize
from skimage.util import random_noise
from skimage.transform import resize

from hopfield import Hopfield


def transform_data(data, img_shape, resized_shape=None,
                   do_binarize=False, noise_amount=0.05):
    transformed = []
    for x in data:
        img = x.reshape(img_shape)
        # resize
        if resized_shape is not None:
            img = resize(image=img, output_shape=resized_shape)
        # binarize
        if do_binarize:
            img = binarize(img)
            img[img == 0] = -1
        # apply noise
        img_trans = random_noise(image=img.astype(float), mode='s&p',
                                 amount=noise_amount)
        transformed.append(img_trans.reshape(-1))
    return np.array(transformed)


def main():
    # load dataset
    dataset = load_digits()

    # parameters
    n_label = 2
    noise_amount = 0.0
    img_resized_shape = (5, 5)
    print('=parameters=')
    print('n_label:', n_label)
    print('noise_amount:', noise_amount)
    print('img_resized_shape:', img_resized_shape)

    # transform data
    dataset.data = transform_data(data=dataset.data,
                                  img_shape=(8, 8),
                                  resized_shape=img_resized_shape,
                                  do_binarize=True,
                                  noise_amount=noise_amount)

    # create train data
    target_names = dataset.target_names[:n_label]
    X, y = [], []
    for t in target_names:
        X.append(dataset.data[dataset.target == t])
        y.append(dataset.target[dataset.target == t])
    X = np.vstack(X)
    y = np.hstack(y)
    n_sample = len(X)
    p = np.random.randint(0, n_sample, n_sample)
    X, y = X[p], y[p]
    print('=data=')
    print('target_names:', target_names)
    print('X.shape:', X.shape)
    print('X:', X, sep='\n')
    print('y.shape:', y.shape)
    print('y:', y, sep='\n')

    # fit hopfield
    hf = Hopfield()
    hf.fit(X, y)

    # recall
    print('=input=')
    input_ = X[0].reshape(img_resized_shape)
    input_ = random_noise(X[0], mode='s&p', amount=0.05)
    print(input_.reshape(img_resized_shape))
    print('=output=')
    ret = hf.recall(x=input_.reshape(-1), n_times=10)
    print(ret.reshape(img_resized_shape))


if __name__ == '__main__':
    main()
