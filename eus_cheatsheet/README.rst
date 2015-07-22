=============
eus-cheatrepo
=============
Cheat Repository when using euslisp and roseus.

Euslisp
=======

[SITUATION1] Creating class
---------------------------

Basic class format
^^^^^^^^^^^^^^^^^^
.. code-block:: lisp

  #!/usr/bin/env eus
  (defclass square
    :super propertied-object
    :slots (area-length area-size))
  (defmethod square
    (:init
      (_area-length)
      (setq area-length _area-length)
      (setq area-size (* area-length area-length)))
    (:area-length () area-length)
    (:area-size () area-size))

  (setq s (instance square :init 10))
  (print (send s :slots))
  (format t "area-length: ~A~%" (send s :area-length))
  (format t "area-size:  ~A~%" (send s :area-size))

the output will be::

  ((plist) (area-length . 10) (area-size . 100))
  area-length: 10
  area-size:  100


Get ``:a`` from ``"a"``
^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: lisp

  (intern (string-upcase "a") "KEYWORD")