import os
import unittest

import atmosphere.config
from atmosphere.machine.virtual_machines import *

__author__ = 'paoolo'

pwd = os.path.dirname(os.path.abspath(__file__))
atmosphere.config.add_config_ini('%s/../config/main.ini' % pwd, '%s/../config/secure.ini' % pwd)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print get_all_virtual_machines()
        print '----'

        print get_virtual_machines(0)
        print '----'


if __name__ == '__main__':
    unittest.main()