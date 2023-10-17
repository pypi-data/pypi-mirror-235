from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='kandinsky.py',
version='2.4',
description='Reverse Engineered Kandinsky 2.2 API',
long_description=long_description,
long_description_content_type='text/markdown',
author='zenafey',
author_email='zenafey@eugw.ru',
packages=['kandinsky'],
license='MIT',
install_requires=['requests', 'aiohttp', 'Pillow', 'colorama'])
