from setuptools import setup

setup(
    name='Keymatrix',
    version='0.3',
    packages=['keypad'],
    license='MIT',
    author='Ruslan Walch',
    long_description=open('README.md').read(),
    install_requires=['rpi.gpio'],
)
