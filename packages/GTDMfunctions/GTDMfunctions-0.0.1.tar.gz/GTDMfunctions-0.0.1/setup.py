# En setup.py

from setuptools import setup, find_packages

setup(
    name='GTDMfunctions',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'sympy'
        # Otras dependencias de tu biblioteca
    ],
)
