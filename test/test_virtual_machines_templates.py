import unittest

from air.machine.virtual_machines_templates import *

__author__ = 'paoolo'


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print get_all_virtual_machines_templates()
        print '----'


if __name__ == '__main__':
    unittest.main()