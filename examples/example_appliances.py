import os
import unittest

import atmosphere.config
from atmosphere.appliance import appliance_sets
from atmosphere.appliance.appliances import *


__author__ = 'paoolo'

pwd = os.path.dirname(os.path.abspath(__file__))
atmosphere.config.add_config_ini('%s/../config/main.ini' % pwd, '%s/../config/secure.ini' % pwd)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        _app_set = appliance_sets.create_app_set(
            appliance_set_type=appliance_sets.APP_SET_TYPE_DEV)
        print _app_set
        print '----'

        try:
            print get_all_app()
            print '----'

            app = create_app(_app_set['appliance_set']['id'], atmosphere.config.CONF_AT_ID)

            print app
            try:
                __id = app['appliance']['id']
            except:
                __id = 0

            print '----'

            print get_all_app()
            print '----'

            print get_app(__id)
            print '----'

            print get_app_endpoints(__id)
            print '----'

            print update_app(__id, 'name')
            print '----'

            print delete_app(__id)

        finally:
            print appliance_sets.delete_app_set(_app_set['appliance_set']['id'])


if __name__ == '__main__':
    unittest.main()