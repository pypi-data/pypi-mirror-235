from setuptools import setup, find_packages

setup(
    name='iitg_energy_analyzer',
    version='1.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
    ],
)