from air import tools

__author__ = 'paoolo'

PREFIX = '/appliance_configuration_templates'


def get_all_app_config_temp():
    """
    Get list of all available appliance configuration templates.

    :return: list of appliance configuration templates
    """
    return tools.create_req()
