import os
import unittest

import atmosphere.config
from atmosphere.mapping.endpoint import *

__author__ = 'paoolo'

pwd = os.path.dirname(os.path.abspath(__file__))
atmosphere.config.add_config_ini('%s/../config/main.ini' % pwd, '%s/../config/secure.ini' % pwd)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print get_all_endpoints()
        print '----'

        print get_endpoint(1)
        print '----'

        print get_endpoint_descriptor(1)
        print '----'


if __name__ == '__main__':
    unittest.main()