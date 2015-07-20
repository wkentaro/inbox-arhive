#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division
import numpy as np
from sklearn.datasets import load_digits
from sklearn.preprocessing import binarize
from skimage.util import random_noise
from skimage.transform import resize


def transform_data(data, img_shape, resized_shape=None,
                   do_binarize=False, noise_amount=0.05):
    # binarize
    if do_binarize:
        data = binarize(data)
        data[data == 0] = -1
    transformed = []
    for x in data:
        img = x.reshape(img_shape)
        # resize
        if resized_shape is not None:
            img = resize(image=img, output_shape=resized_shape)
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
    noise_amount = 0.05
    img_resized_shape = (5, 5)

    # transform data
    dataset.data = transform_data(data=dataset.data,
                                  img_shape=(8, 8),
                                  resized_shape=img_resized_shape,
                                  do_binarize=True,
                                  noise_amount=noise_amount)
    print(dataset.data)


if __name__ == '__main__':
    main()