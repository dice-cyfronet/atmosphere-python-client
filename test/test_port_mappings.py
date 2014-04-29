import os
import unittest

import air.config
from air.mapping.port_mappings import *

__author__ = 'paoolo'

pwd = os.path.dirname(os.path.abspath(__file__))
air.config.add_config_ini('%s/../config/main.ini' % pwd, '%s/../config/secure.ini' % pwd)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print get_all_port_mappings()
        print '----'

        print get_port_mapping(0)
        print '----'


if __name__ == '__main__':
    unittest.main()