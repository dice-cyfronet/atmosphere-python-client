import unittest

import air.config
from air.machine.virtual_machines import *

__author__ = 'paoolo'

air.config.add_config_ini('../config/main.ini', '../config/secure.ini')


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print get_all_virtual_machines()
        print '----'

        print get_virtual_machines(0)
        print '----'


if __name__ == '__main__':
    unittest.main()