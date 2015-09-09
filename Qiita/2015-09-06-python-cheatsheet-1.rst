====================================================
python-cheatsheet #0: builtin functions/組み込み関数
====================================================

**アルファベット順**


``abs``
=======

数値の絶対値::

    >>> abs(1)
    1
    >>> abs(-1)
    1


``all``
=======

リストの要素が全て真::

    >>> all([1, 2, 3])
    True
    >>> all([0, 2, 3])
    False


``any``
=======

リストの少なくとも一つが真::

    >>> any([1, 0, 0])
    True
    >>> any([0, 0, 0])
    False


``basestring``
==============

basestrinc <=> (unicode, str)::

    >>> isinstance('monty', basestring)
    True
    >>> isinstance('monty', str)
    True
    >>> isinstance('monty', unicode)
    False
    >>> isinstance(u'monty', basestring)
    True
    >>> isinstance(u'monty', str)
    False
    >>> isinstance(u'monty', unicode)
    True


``bin``
=======

10進数 -> 2進数::

    >>> bin(128)
    '0b10000000'


``bool``
========

Boolへの変換::

    >>> bool('a')
    True
    >>> bool(1)
    True
    >>> bool(-1)
    True
    >>> bool(0)
    False
    >>> bool('')
    False
    >>> bool([])
    False


``bytearray``
=============

バイト列への変換::

    >>> bytearray(1)
    bytearray(b'\x00')
    >>> bytearray('a', encoding='utf-8')
    bytearray(b'a')



``map``
=======

リスト要素への関数実行::

    >>> def square(x): return x * x
    >>> map(square, [1, 2, 3])
    [1, 4, 9]
    >>> map(lambda x:x**2, [1, 2, 3])
    [1, 4, 9]


``filter``
==========

リストからの選び出し::

    >>> filter(lambda x:x%2 == 0, [1, 2, 3])
    [2]


``ord/chr``
===========

文字列 <-> ascii code/アスキーコード::

    >>> ord('a')
    97
    >>> chr(97)
    'a'


``int``
=======

n進数 -> 10進数::

    >>> bin('11', 2)
    3


``isinstance``
==============

変数の型を調べる::

    >>> isinstance(1, int)
    True
    >>> isinstance(1., float)
    True


``__import__``
==============

importの関数::

    >>> __import__('os', {}, {}, [], -1)
    <module 'os' from '/usr/local/Cellar/python/2.7.10_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/os.pyc'>
