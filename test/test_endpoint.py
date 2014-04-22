import unittest

from air.mapping.endpoint import *

__author__ = 'paoolo'


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