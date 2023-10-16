#!/usr/bin/env python

"""setup.py script for py_ballisticcalc library"""

from Cython.Build import cythonize
from setuptools import setup

setup(
    ext_modules=cythonize(
        [
            'py_ballisticcalc/trajectory_calc.pyx',
            'py_ballisticcalc/drag_model.pyx'
        ],
        compiler_directives={"language_level": 3, "embedsignature": True}
    )
)
