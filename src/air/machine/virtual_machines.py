from air import tools

__author__ = 'paoolo'

PREFIX = '/virtual_machines'


def get_all_virtual_machines(app_id=None):
    url = ''
    if app_id is not None:
        url += 'appliance_id=%s' % str(app_id)
    if len(url) > 0:
        url = '?' + url
    return tools.create_req(url=url)


def get_virtual_machines(_id):
    url = '/%s' % str(_id)
    return tools.create_req(url=url)
