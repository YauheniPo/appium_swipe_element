import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='appium_swipe_element',
    version='1.0.1',
    description='YauheniPo package for swiping by element',
    url='https://github.com/YauheniPo/Appium_Swipe_Element.git',
    author='Yauheni Papovich',
    author_email='ip.popovich.1990@gmail.com',
    license='MIT',
    packages=setuptools.find_packages(),
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
