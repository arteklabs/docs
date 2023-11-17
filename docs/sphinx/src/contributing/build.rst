Build
=====

About
-----

The section shows how to build the package from source.

Getting Started
---------------

Build a distribution package do ``dist`` (notice the ``.whl`` distribution file):

.. code:: shell

   (dmacli-py3.8) poetry build
   Building dmacli (1.0.0-beta)
   - Building sdist
   - Built dmacli-1.0.0b0.tar.gz
   - Building wheel
   - Built dmacli-1.0.0b0-py3-none-any.whl

   (dmacli-py3.8) tree dist
   dist
   ├── dmacli-1.0.0b0-py3-none-any.whl
   └── dmacli-1.0.0b0.tar.gz
