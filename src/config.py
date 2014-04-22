import ConfigParser
import sys

__author__ = 'paoolo'


class Config(object):
    def __init__(self, *args):
        self.__config = ConfigParser.ConfigParser()
        map(lambda config_file_path: self.__config.read(config_file_path), args)

    def __getattr__(self, name):
        # noinspection PyBroadException
        try:
            return self.__config.get('default', name)
        except Exception as n_exp:
            # TODO: notify about this
            return None


sys.modules[__name__] = Config('../config/main.ini', '../config/secure.ini')