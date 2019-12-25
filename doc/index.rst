.. code-block::

                  __  __      _         ____ _
      _ __  _   _|  \/  | ___| |_ __ _ / ___| | __ _ ___ ___  ___  ___
     | '_ \| | | | |\/| |/ _ \ __/ _` | |   | |/ _` / __/ __|/ _ \/ __|
     | |_) | |_| | |  | |  __/ || (_| | |___| | (_| \__ \__ \  __/\__ \
     | .__/ \__, |_|  |_|\___|\__\__,_|\____|_|\__,_|___/___/\___||___/
     |_|    |___/

pyMetaClasses Documentation
###########################

A collection of MetaClasses for Python.

Introduction
************

A Python meta class is a class used to construct instances of other classes.
Python has one default meta class called :py:class:`type`. It's possible to
write new meta classes from scratch or to derive subclasses from :py:class:`type`.

Meta classes are used by passing a named parameter to a class definition in
addition to a list of classes for inheritance.

.. code-block:: Python

   class Foo(Bar, metaclass=type):
     pass


List of meta classes
********************

* :py:class:`pyMetaClasses.Singleton`


Contributors
************

* `Patrick Lehmann <https://github.com/Paebbels>`_ (Maintainer)


License
*******

This library is licensed under **Apache License 2.0**.


------------------------------------

.. |docdate| date:: %b %d, %Y - %H:%M

.. only:: html

   This document was generated on |docdate|.

.. toctree::
   :caption: Overview
   :hidden:

   Installation
   Dependencies

.. toctree::
   :caption: Meta Classes
   :hidden:

   Singleton


.. toctree::
   :caption: Appendix
   :hidden:

   License
   genindex

.. #
   py-modindex
