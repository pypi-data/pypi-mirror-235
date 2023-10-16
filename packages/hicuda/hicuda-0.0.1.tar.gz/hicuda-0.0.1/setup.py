from setuptools import setup, find_packages

setup(
    name='hicuda',
    version='0.0.1',
    packages=find_packages(),
    package_data={
        '': ['*.so'],  # Include .so files from any package
    },
)
