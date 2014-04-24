from air import tools

__author__ = 'paoolo'

PREFIX = '/appliance_types'


def get_all_appliance_types(name=None):
    url = ''
    if name is not None:
        url += 'name=%s' % str(name)
    if len(url) > 0:
        url = '&' + url
    return tools.create_req(url=url)
