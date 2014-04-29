import os
import unittest

import air.config
from air.mapping.http_mappings import *

__author__ = 'paoolo'

pwd = os.path.dirname(os.path.abspath(__file__))
air.config.add_config_ini('%s/../config/main.ini' % pwd, '%s/../config/secure.ini' % pwd)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print get_all_http_map()
        print '----'

        print get_http_map(0)
        print '----'


if __name__ == '__main__':
    unittest.main()