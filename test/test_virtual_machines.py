import unittest

from air.machine.virtual_machines import *

__author__ = 'paoolo'


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print get_all_virtual_machines()
        print '----'

        print get_virtual_machines(0)
        print '----'


if __name__ == '__main__':
    unittest.main()