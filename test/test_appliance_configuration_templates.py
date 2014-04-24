import unittest

import air.config
from air.appliance.appliance_configuration_templates import *

__author__ = 'paoolo'


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print get_all_app_config_temp()


if __name__ == '__main__':
    air.config.add_config_ini('../config/main.ini', '../config/secure.ini')
    unittest.main()