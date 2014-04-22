import unittest

from air.dev_mode_property_sets import *

__author__ = 'paoolo'


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