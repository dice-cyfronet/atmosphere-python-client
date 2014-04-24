# coding=utf-8

__author__ = 'paoolo'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='air-python',
    packages=['air', 'air.appliance', 'air.machine', 'air.mapping', 'air.property'],
    package_dir={'air': 'src/air',
                 'air.appliance': 'src/air/appliance',
                 'air.machine': 'src/air/machine',
                 'air.mapping': 'src/air/mapping',
                 'air.property': 'src/air/property'},
    install_requires=required,
    version='1.0',
    description='AIR REST API wrapper in python',
    author=u'Paweł Suder',
    author_email='pawel@suder.info',
    url='https://gitlab.dev.cyfronet.pl/paoolo/air-python',
    download_url='https://gitlab.dev.cyfronet.pl/paoolo/air-python/repository/archive.zip',
    keywords=['air', 'atmosphere'],
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
    ],
    long_description='''\
'''
)