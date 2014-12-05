import os
import unittest

import atmosphere.config
from atmosphere.appliance.appliance_types import *
from atmosphere.appliance.appliances import *


__author__ = 'paoolo'

pwd = os.path.dirname(os.path.abspath(__file__))
atmosphere.config.add_config_ini('%s/../config/main.ini' % pwd, '%s/../config/secure.ini' % pwd)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print get_all_appliance_types()
        print '----'

        print get_all_app_type()
        print '----'

        print get_app_type(1)
        print '----'

        print update_app_type(1, name='Testing-update')
        print '----'


if __name__ == '__main__':
    unittest.main()