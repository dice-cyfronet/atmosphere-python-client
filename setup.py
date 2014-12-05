# coding=utf-8

import os

__author__ = 'paoolo'

pwd = os.path.dirname(os.path.abspath(__file__))

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('%s/requirements.txt' % pwd) as f:
    required = f.read().splitlines()

setup(
    name='atmosphere-python-client',
    packages=['atmosphere', 'atmosphere.appliance', 'atmosphere.machine', 'atmosphere.mapping', 'atmosphere.property'],
    package_dir={'atmosphere': '%s/src/atmosphere' % pwd,
                 'atmosphere.appliance': '%s/src/atmosphere/appliance' % pwd,
                 'atmosphere.machine': '%s/src/atmosphere/machine' % pwd,
                 'atmosphere.mapping': '%s/src/atmosphere/mapping' % pwd,
                 'atmosphere.property': '%s/src/atmosphere/property' % pwd},
    install_requires=required,
    version='1.0',
    description='Atmosphere REST API client written in python',
    author=u'Paweł Suder',
    author_email='pawel@suder.info',
    url='https://github.com/dice-cyfronet/atmosphere-python-client',
    download_url='https://github.com/dice-cyfronet/atmosphere-python-client/archive/master.zip',
    keywords=['atmosphere', 'atmosphere'],
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