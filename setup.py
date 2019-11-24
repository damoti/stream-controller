import os
from setuptools import setup

HERE = os.path.dirname(__file__)
with open(os.path.join(HERE, 'README.md')) as fh:
    long_description = fh.read()
with open(os.path.join(HERE, 'streamcontroller.py')) as fh:
    version = fh.readline().split('"')[1]

setup(
    name='streamcontroller',
    version=version,
    url='https://github.com/damoti/stream-controller',
    license='BSD',
    description='Asynchronous event stream classes inspired by Dart streams API.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Lex Berezhny',
    author_email='lex@damoti.com',
    keywords='asyncio,stream,event,dart,api',
    python_requires='>=3.8',
    py_modules=['streamcontroller'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: AsyncIO',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
)
