import os
import unittest

import atmosphere.config
from atmosphere.appliance import appliances
from atmosphere.appliance import appliance_sets
from atmosphere.mapping.port_mapping_templates import *
from atmosphere.property import dev_mode_property_sets

__author__ = 'paoolo'

pwd = os.path.dirname(os.path.abspath(__file__))
atmosphere.config.add_config_ini('%s/../config/main.ini' % pwd, '%s/../config/secure.ini' % pwd)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        _app_set = appliance_sets.create_app_set(
            appliance_set_type=appliance_sets.APP_SET_TYPE_DEV)
        print _app_set
        print '----'

        _app = appliances.create_app(_app_set['appliance_set']['id'], atmosphere.config.CONF_AT_ID)
        print _app
        print '----'

        _dev_sets = dev_mode_property_sets.get_all_dev_mode_property_set(_app['appliance']['id'])
        print _dev_sets
        print '----'

        try:
            print get_all_port_map_temp_by_dev(_dev_sets['dev_mode_property_sets'][0]['id'])
            print '----'

            _port_mapping = create_port_map_temp_for_dev(_dev_sets['dev_mode_property_sets'][0]['id'], 'tcp', 'none',
                                                         'telnet', 25)
            print _port_mapping
            print '----'

            print get_all_port_map_temp_by_dev(_dev_sets['dev_mode_property_sets'][0]['id'])
            print '----'

            print update_port_map_temp(_port_mapping['port_mapping_template']['id'], service_name='http',
                                       target_port=80)
            print '----'

            print get_all_port_map_temp_by_dev(_dev_sets['dev_mode_property_sets'][0]['id'])
            print '----'

            print delete_port_map_temp(_port_mapping['port_mapping_template']['id'])
            print '----'

        finally:
            print appliances.delete_app(_app['appliance']['id'])
            print appliance_sets.delete_app_set(_app_set['appliance_set']['id'])


if __name__ == '__main__':
    unittest.main()