import os
import unittest

import air.config
from air.appliance.appliance_configuration_templates import *

__author__ = 'paoolo'

pwd = os.path.dirname(os.path.abspath(__file__))
air.config.add_config_ini('%s/../config/main.ini' % pwd, '%s/../config/secure.ini' % pwd)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print get_all_app_config_temp()


if __name__ == '__main__':
    unittest.main()