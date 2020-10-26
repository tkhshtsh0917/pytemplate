# -*- coding: utf-8 -*-
"""
setup
"""
from distutils.core import Extension, setup

from Cython.Build import cythonize

if __name__ == "__main__":
    extension = Extension("cythonic", sources=["cythonic.pyx"])
    setup(name="cythonic", ext_modules=cythonize([extension]))
