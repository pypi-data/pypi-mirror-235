#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File   : setup.py
@Author : XinWang
"""

import numpy as np
# from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
ext_modules = [Extension("fast_dist",
                         ["fast_dist.pyx"]
                         ),
               Extension('fast_score',
                         ["fast_score.pyx"]
                         )
               ]
setuptools.setup(
    name="fitPhylo",
    version="1.0",
    author="XinWang",
    author_email="wangx768@mail2.sysu.edu.cn",
    description="A package for inferring CNA fitness evolutionary trees and CNAs' evolutionary efficiency",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FangWang-SYSU/fitPhylo.git",
    packages=setuptools.find_packages(),
    # install_requires=['requests', 'selenium', 'baidu-aip', 'pillow', 'pywin32'],
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules,
    include_dirs=[np.get_include()],
    python_requires='>=3.9',
    keywords=['Single cell', 'phylogenetic tree', 'CNA', 'evolutionary efficiency'],
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

)
# python setup.py build_ext --inplace
# setup(
#     name='fitPhylo',
#     cmdclass={'build_ext': build_ext},
#     ext_modules=ext_modules,
#     include_dirs=[np.get_include()]
# )

