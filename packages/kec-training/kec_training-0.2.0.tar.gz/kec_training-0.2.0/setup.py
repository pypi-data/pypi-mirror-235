from setuptools import setup, find_packages

setup(
    name='kec_training',
    version='0.2.0',
    author='Nishan Khanal',
    author_email='nishan.khanal98@gmail.com',
    description='A package to to assist in KEC Training',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)