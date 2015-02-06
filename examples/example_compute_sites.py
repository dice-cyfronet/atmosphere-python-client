import os
import unittest

import atmosphere.config
from atmosphere.machine.compute_sites import *

__author__ = 'paoolo'

pwd = os.path.dirname(os.path.abspath(__file__))
atmosphere.config.add_config_ini('%s/../config/main.ini' % pwd, '%s/../config/secure.ini' % pwd)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print get_all_compute_sites()
        print '----'

        print get_compute_sites(1)
        print '----'


if __name__ == '__main__':
    unittest.main()