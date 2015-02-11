import unittest
import os

import atmosphere.config
from atmosphere.property.dev_mode_property_sets import *


__author__ = 'paoolo'

pwd = os.path.dirname(os.path.abspath(__file__))
atmosphere.config.add_config_ini('%s/../config/main.ini' % pwd, '%s/../config/secure.ini' % pwd)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print get_all_dev_mode_property_set()
        print '----'

        print get_dev_mode_property_set(0)
        print '----'

        print update_dev_mode_property_set(0)
        print '----'


if __name__ == '__main__':
    unittest.main()