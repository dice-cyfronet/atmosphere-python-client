import os
import unittest

import air.config
from air.appliance.appliance_configuration_templates import *


__author__ = 'paoolo'

pwd = os.path.dirname(os.path.abspath(__file__))
air.config.add_config_ini('%s/../config/main.ini' % pwd, '%s/../config/secure.ini' % pwd)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print get_all_app_config_temp()
        print '----'

        app_conf_temp = create_app_conf_temp(1, '_empty', 'null')
        print app_conf_temp
        print '----'

        print get_all_app_config_temp()
        print '----'

        print update_app_conf_temp(app_conf_temp['appliance_configuration_template']['id'],
                                   '_full', 'payload')
        print '----'

        print get_all_app_config_temp()
        print '----'

        print delete_app_conf_temp(app_conf_temp['appliance_configuration_template']['id'])


if __name__ == '__main__':
    unittest.main()