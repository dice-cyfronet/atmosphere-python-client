import simplejson

from air import tools


__author__ = 'paoolo'

PREFIX = '/appliance_sets'


def _create_req(method=tools.HTTP_GET, url='', body=None, headers=None):
    return tools.create_req(method, PREFIX + url, body, headers)


def get_all_app_set():
    return _create_req()


def get_app_set(_id):
    url = '/%s' % str(_id)
    return _create_req(url=url)


APP_SET_TYPE_DEV = 'development'
APP_SET_TYPE_PORTAL = 'portal'
APP_SET_TYPE_WORKFLOW = 'workflow'


def create_app_set(name=None, priority=None, appliance_set_type=None):
    _data = {}
    if name is not None:
        _data['name'] = name
    if priority is not None:
        _data['priority'] = priority
    if appliance_set_type is not None:
        _data['appliance_set_type'] = appliance_set_type
    body = {'appliance_set': _data}
    body = simplejson.dumps(body)
    return _create_req(method=tools.HTTP_POST, body=body, headers={'Content-Length': len(body),
                                                                   'Content-Type': 'application/json'})


def update_app_set(_id, name=None, priority=None):
    url = '/%s' % str(_id)
    _data = {'id': _id}
    if name is not None:
        _data['name'] = name
    if priority is not None:
        _data['priority'] = priority
    body = {'appliance_set': _data}
    body = simplejson.dumps(body)
    return _create_req(method=tools.HTTP_PUT, url=url, body=body, headers={'Content-Length': len(body),
                                                                           'Content-Type': 'application/json'})


def delete_app_set(_id):
    url = '/%s' % str(_id)
    return _create_req(method=tools.HTTP_DELETE, url=url)

if __name__ == '__main__':
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
