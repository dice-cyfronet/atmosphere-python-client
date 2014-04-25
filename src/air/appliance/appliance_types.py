import air.tools

__author__ = 'paoolo'

PREFIX = '/appliance_types'


def get_all_appliance_types(name=None):
    """
    Get a list of appliance types.

    :param name: any string (optional)
    :return:
    """
    url = ''
    if name is not None:
        url += 'name=%s' % str(name)
    if len(url) > 0:
        url = '&' + url
    return air.tools.create_req(url=url)
