import unittest

import air.config
from air.machine.compute_sites import *

__author__ = 'paoolo'

air.config.add_config_ini('../config/main.ini', '../config/secure.ini')


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print get_all_compute_sites()
        print '----'

        print get_compute_sites(1)
        print '----'


if __name__ == '__main__':
    unittest.main()