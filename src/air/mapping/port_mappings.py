from air import tools

__author__ = 'paoolo'

PREFIX = '/port_mappings'


def get_all_port_mappings(port_mapping_template_id=None, virtual_machine_id=None):
    url = ''
    if port_mapping_template_id is not None:
        url += 'port_mapping_template_id=%s' % str(port_mapping_template_id)
    if virtual_machine_id is not None:
        if len(url) > 0: url += '&'
        url += 'virtual_machine_id=%s' % str(virtual_machine_id)
    if len(url) > 0:
        url = '?' + url
    return tools.create_req(url=url)


def get_port_mapping(_id):
    url = '/%s' % str(_id)
    return tools.create_req(url=url)
