atmosphere-python
=================

Installation
------------

Download stable version and run command `python setup.py install`.

If you have installed `atmosphere-client-python`, if any problem occurs, run
`python setup.py clean` and/or `pip uninstall atmosphere-client-python`.

Test
----

Copy file `config/main-example.ini` to `config/main.ini` and
`config/secure-example.ini` to `config/secure.ini`. Edit these files.
Execute `test/run-test.sh`. You do not need to install `atmosphere-client-python`.

Usage
-----

**Config**

To use *atmosphere* API you need to have `API_PRIVATE_TOKEN` or `API_MI_TICKET`.
You need to set it via config files, which are loaded via `config.add_config_ini()`.

Example of config files are in `config/.

**Use in code**

    import atmosphere.config
    atmosphere.config.add_config_ini('path/to/main.ini', 'path/to/secure.ini', 'path/to/other.ini', ...)
    from atmosphere.appliance.appliance_configuration_templates import get_all_app_config_temp
    get_all_app_config_temp()

That's all!