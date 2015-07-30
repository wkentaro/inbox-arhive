#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import platform


def get_completion_install_location(shell):
    uname = platform.uname()[0]
    is_root = (os.get_uid() == 0)

    prefix = ''
    if shell == 'bash':
        if is_root and uname == 'Linux':
            prefix = '/'
        location = os.path.join(prefix, 'etc/bash_completion.d')
    elif shell == 'zsh':
        location = os.path.join(prefix, 'share/zsh/site-functions')
    else:
        raise ValueError('unsupported shell: {0}'.format(shell))

    return location