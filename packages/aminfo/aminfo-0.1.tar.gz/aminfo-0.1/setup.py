from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension

ext_modules = [
    Pybind11Extension(
        'aminfo',
        ['src/aminfo.cpp'],
    ),
]

setup(
    name='aminfo',
    version='0.1',
    ext_modules=ext_modules,
    setup_requires=["pybind11>=2.11.0"],
    license='MIT'
)