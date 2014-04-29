import os
import unittest

import air.config
from air.appliance.appliance_sets import *

__author__ = 'paoolo'

pwd = os.path.dirname(os.path.abspath(__file__))
air.config.add_config_ini('%s/../config/main.ini' % pwd, '%s/../config/secure.ini' % pwd)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print get_all_app_set()
        print '----'

        app_set = create_app_set(appliance_set_type=APP_SET_TYPE_DEV)

        if 'message' in app_set:
            app_set = get_all_app_set()
            delete_app_set(app_set['appliance_sets'][0]['id'])
            app_set = create_app_set(appliance_set_type=APP_SET_TYPE_DEV)

        print app_set
        try:
            app_id = app_set['appliance_set']['id']
        except:
            app_id = 0

        print '----'

        print get_all_app_set()
        print '----'

        print get_app_set(app_id)
        print '----'

        print update_app_set(app_id, name='name', priority=2)
        print '----'

        print delete_app_set(app_id)


if __name__ == '__main__':
    unittest.main()