Singleton
#########

.. autoclass:: pyMetaClasses.Singleton
   :members:
   :private-members:
   :special-members:

Example Usage
*************

.. code-block:: Python

   class Terminal(metaclass=Singleton):
     def __init__(self):
       pass

     def WriteLine(self, message):
       print(message)
