from setuptools import setup, find_packages

setup(
    name='iitg_pv_energy_generation',
    version='2.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib'
    ],
)