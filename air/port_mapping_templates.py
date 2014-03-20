import simplejson

from air import tools, appliance_sets, appliances, dev_mode_property_sets


__author__ = 'paoolo'

PREFIX = '/port_mapping_templates'


def _create_req(method=tools.HTTP_GET, url='', body=None, headers=None):
    return tools.create_req(method, PREFIX + url, body, headers)


def get_all_port_map_temp_by_at(appliance_type_id):
    url = '?appliance_type_id=%s' % str(appliance_type_id)
    return _create_req(url=url)


def get_all_port_map_temp_by_dev(dev_mode_property_set_id, target_port=None):
    url = '?dev_mode_property_set_id=%s' % str(dev_mode_property_set_id)
    if target_port is not None:
        url += '&target_port=%s' % str(target_port)
    return _create_req(url=url)


def get_port_map_temp(_id):
    url = '/%s' % str(_id)
    return _create_req(url=url)


def create_port_map_temp_for_at(appliance_type_id,
                                transport_protocol, application_protocol, service_name, target_port):
    body = {'port_mapping_template': {'appliance_type_id': appliance_type_id,
                                      'transport_protocol': transport_protocol,
                                      'application_protocol': application_protocol,
                                      'service_name': service_name,
                                      'target_port': target_port}}
    body = simplejson.dumps(body)
    return _create_req(method=tools.HTTP_POST, body=body, headers={'Content-Length': len(body),
                                                                   'Content-Type': 'application/json'})


def create_port_map_temp_for_dev(dev_mode_property_set_id,
                                 transport_protocol, application_protocol, service_name, target_port):
    body = {'port_mapping_template': {'dev_mode_property_set_id': dev_mode_property_set_id,
                                      'transport_protocol': transport_protocol,
                                      'application_protocol': application_protocol,
                                      'service_name': service_name,
                                      'target_port': target_port}}
    body = simplejson.dumps(body)
    return _create_req(method=tools.HTTP_POST, body=body, headers={'Content-Length': len(body),
                                                                   'Content-Type': 'application/json'})


def update_port_map_temp(_id, appliance_type_id=None, dev_mode_property_set_id=None,
                         transport_protocol=None, application_protocol=None, service_name=None, target_port=None):
    url = '/%s' % str(_id)
    _data = {}
    if appliance_type_id is not None:
        _data['appliance_type_id'] = appliance_type_id
    if dev_mode_property_set_id is not None:
        _data['dev_mode_property_set_id'] = dev_mode_property_set_id
    if transport_protocol is not None:
        _data['transport_protocol'] = transport_protocol
    if application_protocol is not None:
        _data['application_protocol'] = application_protocol
    if service_name is not None:
        _data['service_name'] = service_name
    if target_port is not None:
        _data['target_port'] = target_port
    body = {'port_mapping_template': _data}
    body = simplejson.dumps(body)
    return _create_req(method=tools.HTTP_PUT, url=url, body=body, headers={'Content-Length': len(body),
                                                                           'Content-Type': 'application/json'})


def delete_port_map_temp(_id):
    url = '/%s' % str(_id)
    return _create_req(method=tools.HTTP_DELETE, url=url)


def get_dev_id_for_app(app_id, dev_sets):
    if 'dev_mode_property_sets' in dev_sets:
        for dev_set in dev_sets['dev_mode_property_sets']:
            if 'appliance_id' in dev_set and dev_set['appliance_id'] == app_id:
                return dev_set
    return None
