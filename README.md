# atmosphere-python-client

[![Build Status](https://travis-ci.org/dice-cyfronet/atmosphere-python-client.svg?branch=master)](https://travis-ci.org/dice-cyfronet/atmosphere-python-client)
[![Code Health](https://landscape.io/github/dice-cyfronet/atmosphere-python-client/master/landscape.svg?style=flat)](https://landscape.io/github/dice-cyfronet/atmosphere-python-client/master)
[![Codacy Badge](https://www.codacy.com/project/badge/d90b929be42e4593a4ec6bfcc811cd44?style=flat)](https://www.codacy.com/public/pawel/atmosphere-python-client)
[![Coverage Status](https://coveralls.io/repos/dice-cyfronet/atmosphere-python-client/badge.svg)](https://coveralls.io/r/dice-cyfronet/atmosphere-python-client)

[![PyPI](https://img.shields.io/pypi/l/atmosphere-python-client.svg)](https://pypi.python.org/pypi/atmosphere-python-client)
[![PyPI](https://img.shields.io/pypi/pyversions/atmosphere-python-client.svg)](https://pypi.python.org/pypi/atmosphere-python-client)
[![PyPI](https://img.shields.io/pypi/implementation/atmosphere-python-client.svg)](https://pypi.python.org/pypi/atmosphere-python-client)
[![PyPI](https://img.shields.io/pypi/status/atmosphere-python-client.svg)](https://pypi.python.org/pypi/atmosphere-python-client)

This library provides a wrapper of REST operation performed by [Atmosphere](https://github.com/dice-cyfronet/atmosphere).

## Installation

Download stable version and run command `python setup.py install`.

If you have installed `atmosphere-client-python`, if any problem occurs, run
`python setup.py clean` and/or `pip uninstall atmosphere-client-python`.

## Examples

Copy file `config/main-example.ini` to `config/main.ini` and
`config/secure-example.ini` to `config/secure.ini`. Edit these files.
You will find it in [`examples/`](examples/).

## Usage

### Config

To use *atmosphere* API you need to have `API_PRIVATE_TOKEN` or `API_MI_TICKET`.
Copy file `config/main-example.ini` to `config/main.ini` and
`config/secure-example.ini` to `config/secure.ini`. Edit these files.
You need to set it via config files, which are loaded via `config.add_config_ini()`.

Example of config files are in [`config/`](config/).

### Use in code

    import atmosphere.config
    atmosphere.config.add_config_ini('path/to/main.ini', 'path/to/secure.ini', 'path/to/other.ini', ...)
    from atmosphere.appliance.appliance_configuration_templates import get_all_app_config_temp
    get_all_app_config_temp()

That's all!
