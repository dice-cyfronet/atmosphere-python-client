import unittest

import air.config
from air.appliance.appliance_types import *

__author__ = 'paoolo'

air.config.add_config_ini('../config/main.ini', '../config/secure.ini')


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print get_all_appliance_types()
        print '----'


if __name__ == '__main__':
    unittest.main()