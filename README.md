air-python
==========

Installation
------------

Download stable version and run command `python setup.py install`.

If you have installed `air-python`, if any problem occurs, run
`python setup.py clean` and/or `pip uninstall air-python`.

Test
----

Execute `test/run-test.sh`. You do not need to install `air-python`.

Usage
-----

**Config**

To use *air* API you need to have `API_PRIVATE_TOKEN` or `API_MI_TICKET`.
You need to set it via config files, which are loaded via `config.add_config_ini()`.

Example of config files are in `config/.

**Use in code**

    import air.config
    air.config.add_config_ini('path/to/main.ini', 'path/to/secure.ini', 'path/to/other.ini', ...)
    from air.appliance.appliance_configuration_templates import get_all_app_config_temp
    get_all_app_config_temp()

That's all!