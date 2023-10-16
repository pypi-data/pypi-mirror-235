from codecs import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name='elenchos',

        version='1.0.0',

        description='Élenchos: A Nagios plugin framework',
        long_description=long_description,

        url='https://github.com/NagiosElenchos/elenchos',

        author='Set Based IT Consultancy',
        author_email='info@setbased.nl',

        license='MIT',

        classifiers=[
            'Development Status :: 5 - Production/Stable',

            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'Topic :: Software Development :: Build Tools',
            'Topic :: Software Development :: Code Generators',
            'Topic :: System :: Systems Administration',

            'License :: OSI Approved :: MIT License',

            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
        ],

        keywords='Élenchos, Elenchos',

        packages=find_packages(exclude=['build', 'test']),

        install_requires=['cleo~=2.0.0',
                          'lxml~=4.9.3'],

        entry_points={
            'console_scripts': [
                'elenchos = elenchos:main',
            ],
        }
)
