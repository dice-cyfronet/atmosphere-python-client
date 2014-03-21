import httplib
import simplejson

import config
import secure_config


__author__ = 'paoolo'

HTTP_GET = 'GET'
HTTP_POST = 'POST'
HTTP_PUT = 'PUT'
HTTP_DELETE = 'DELETE'


def func_create_req(api_url, api_prefix, api_private_token=None, api_mi_ticket=None):
    def __create_req(method, url, body=None, headers=None):
        if not headers:
            headers = {}
        if not 'PRIVATE-TOKEN' in headers and api_private_token is not None:
            headers['PRIVATE-TOKEN'] = api_private_token
        if not 'MI-TICKET' in headers and api_mi_ticket is not None:
            headers['MI-TICKET'] = api_mi_ticket

        connection = httplib.HTTPConnection(api_url)
        connection.request(method, api_prefix + url, body, headers=headers)
        response = connection.getresponse()
        content = response.read()

        try:
            data = simplejson.loads(content)
        except simplejson.JSONDecodeError as e:
            data = {}

        response.close()
        connection.close()

        return data

    return __create_req


create_req = func_create_req(config.API_URL, config.API_PREFIX, secure_config.API_TOKEN)
