import unittest

import air.config
from air.mapping.http_mappings import *

__author__ = 'paoolo'


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print get_all_http_map()
        print '----'

        print get_http_map(0)
        print '----'


if __name__ == '__main__':
    air.config.add_config_ini('../config/main.ini', '../config/secure.ini')
    unittest.main()