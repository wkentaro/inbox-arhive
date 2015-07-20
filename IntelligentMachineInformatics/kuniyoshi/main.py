#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from sklearn.datasets import fetch_mldata
from skimage.util import random_noise


def apply_noise(data, img_shape, noise_amount=0.05):
    applied = []
    for x in data:
        img = x.reshape(img_shape).astype(float)
        img_noise_applied = random_noise(image=img, mode='s&p',
                                         amount=noise_amount)
        applied.append(img_noise_applied.reshape(-1))
    return np.array(applied)


def main():
    dataset = fetch_mldata('MNIST original')
    dataset.data = apply_noise(data=dataset.data, img_shape=(28, 28))


if __name__ == '__main__':
    main()