#!/usr/bin/env python
# -*- coding: utf-8 -*-
# print_wave_info.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import sys

import wave
import pyaudio


def print_wave_info(wf):
    """Get wave file information"""
    print("channel num: {}".format(wf.getnchannels()))
    print("sample width: {}".format(wf.getsampwidth()))
    print("frame rate: {}".format(wf.getframerate()))
    print("frame num: {}".format(wf.getnframes()))
    print("params: {}".format(wf.getparams()))
    print("length [s]: {}".format(wf.getnframes() / wf.getframerate()))


def output_wave_file(wf):
    # open the stream
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    # output sound with chunk unit to stream
    chunk = 1024
    data = wf.readframes(chunk)
    while data != '':
        stream.write(data)
        data = wf.readframes(chunk)
    stream.close()
    p.terminate()


def main(filename):
    # load
    wf = wave.open(filename, 'r')
    # get info
    print_wave_info(wf=wf)
    # output wave file
    output_wave_file(wf=wf)
    # close
    wf.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "[usage]: python " + sys.argv[0] + " <wave filename>"
        sys.exit()
    main(sys.argv[1])