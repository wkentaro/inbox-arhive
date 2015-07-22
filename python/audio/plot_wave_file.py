#!/usr/bin/env python
# -*- coding: utf-8 -*-
# plot_wave_file.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import sys

import wave
import numpy as np
import matplotlib.pyplot as plt

from output_wave_file import (
    print_wave_info,
    output_wave_file,
    )


def plot_wave_file(wf):
    buf = wf.readframes(wf.getnframes())
    print(len(buf))
    # buf is binary & get together to make int with 2 bytes
    data = np.frombuffer(buf, dtype='int16')
    # plot
    ax1 = plt.subplot(2, 1, 1)
    ax1.plot(data)
    ax2 = plt.subplot(2, 1, 2)
    ax2.plot(data[8000:9000])
    plt.show()


def main(filename):
    # load
    wf = wave.open(filename, 'r')
    # plot wave
    plot_wave_file(wf=wf)
    # close
    wf.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "[usage]: python " + sys.argv[0] + " <wave filename>"
        sys.exit()
    main(sys.argv[1])
