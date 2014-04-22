import tools

__author__ = 'paoolo'

PREFIX = '/virtual_machine_templates'


def _create_req(method=tools.HTTP_GET, url='', body=None, headers=None):
    return tools.create_req(method, PREFIX + url, body, headers)


def get_all_virtual_machines_templates():
    return _create_req()
