from setuptools import setup, find_namespace_packages

setup(
    name='clean_modul',
    version='1.0.0',
    author='Oleksandr Zhytnikov',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean=clean_modul.clean:start']}
)