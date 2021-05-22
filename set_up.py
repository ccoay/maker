# coding:utf-8
import os
import stat
from setuptools import setup, find_packages
from setuptools.command.install import install


setup(
        name='marker',
        version='1.0',
        description='This is a watermarker tool',
        author='iiotxiaoyao',
        packages=find_packages(),
        install_requires=[
            'pillow',
        ],

)