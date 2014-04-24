import unittest

import air.config
from air.mapping.port_mappings import *

__author__ = 'paoolo'


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print get_all_port_mappings()
        print '----'

        print get_port_mapping(0)
        print '----'


if __name__ == '__main__':
    air.config.add_config_ini('../config/main.ini', '../config/secure.ini')
    unittest.main()