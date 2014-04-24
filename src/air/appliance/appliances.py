import simplejson

from air import tools

__author__ = 'paoolo'

PREFIX = '/appliances'


def get_all_app(_all=False):
    url = '?all=true' if _all else ''
    return tools.create_req(url=url)


def get_app(_id):
    url = '/%s' % str(_id)
    return tools.create_req(url=url)


def get_app_endpoints(_id):
    url = '/%s/endpoints' % str(_id)
    return tools.create_req(url=url)


def create_app(appliance_set_id, configuration_template_id,
               name=None, user_key_id=None, params=None):
    _data = {'appliance_set_id': appliance_set_id,
             'configuration_template_id': configuration_template_id}
    if name is not None:
        _data['name'] = name
    if user_key_id is not None:
        _data['user_key_id'] = user_key_id
    if params is not None:
        _data['params'] = params
    body = {'appliance': _data}
    body = simplejson.dumps(body)
    return tools.create_req(method=tools.HTTP_POST, body=body, headers={'Content-Length': len(body),
                                                                        'Content-Type': 'application/json'})


def update_app(_id, name=None):
    _data = {}
    if name is not None:
        _data['name'] = name
    body = {'appliance': _data}
    body = simplejson.dumps(body)
    url = '/%s' % str(_id)
    return tools.create_req(method=tools.HTTP_PUT, url=url, body=body, headers={'Content-Length': len(body),
                                                                                'Content-Type': 'application/json'})


def delete_app(_id):
    url = '/%s' % int(_id)
    return tools.create_req(method=tools.HTTP_DELETE, url=url)
