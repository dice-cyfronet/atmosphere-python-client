import air.tools

__author__ = 'paoolo'

PREFIX = '/virtual_machine_templates'


def get_all_virtual_machines_templates():
    """
    Get a list of virtual machines used by appliances added to user appliance sets.

    :return:
    """
    return air.tools.create_req()
