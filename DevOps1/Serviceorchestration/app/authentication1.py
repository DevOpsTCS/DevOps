# import keystoneclient.v2_0.client as ksclient
from credentials1 import get_keystone_creds, get_heat_url
from credentials1 import get_stack_show_url
import httplib2
import json
import time
# from exception import
# from app.views import On-board-VNF-Package


def keystone_auth():
    creds = get_keystone_creds()
    keystone = creds
#    service = keystone.services.create(name="keystone",
#                                       service_type="identity",
#                                       description=
#                                       "OpenStack Identity Service")
    tokenID = keystone.auth_token
    return tokenID


def stack_create(stack_name1, heat_template, image):
    # Sending request to Heat service for creating the  heat stack
    path = get_heat_url()
    http = httplib2.Http()
    tokenID = keystone_auth()
    headers = {'Content-Type': 'application/json', 'X-Auth-Token': tokenID}
    data2 = {"stack_name": stack_name1,
             "template": heat_template,
             "parameters": {"image_id": image}}
    response, content = http.request(path, 'POST', headers=headers,
                                     body=json.dumps(data2))
    returned_content = json.loads(content)
    if response.status == 201:
        stack_id = returned_content["stack"]["id"]
        return stack_id
    else:
        #        raise exception
        print "ERROR"


def stack_show(stack_name, stack_id):
    tokenID = keystone_auth()
    headers = {'Content-Type': 'application/json', 'X-Auth-Token': tokenID}
    path1 = get_stack_show_url(stack_name, stack_id)
    http = httplib2.Http()
    response1, content1 = http.request(path1, headers=headers)
    while (json.loads(content1)['stack']['stack_status'] ==
           'CREATE_IN_PROGRESS'):
        time.sleep(2)
        response1, content1 = http.request(path1, headers=headers)
    stack_status = json.loads(content1)['stack']['stack_status']
    return stack_status


def stack_delete(stack_name, stack_id):
    try:
        tokenID = keystone_auth()
        headers = {'Content-Type': 'application/json', 'X-Auth-Token': tokenID}
        path = get_stack_show_url(stack_name, stack_id)
        http = httplib2.Http()
        response, content = http.request(path, 'DELETE', headers=headers)
        response1, content1 = http.request(path, 'GET', headers=headers)
    except ValueError:
        pass
    stack_status = json.loads(content1)['stack']['stack_status']
    return stack_status


def stack_delete_status(stack_name, stack_id):
    tokenID = keystone_auth()
    headers = {'Content-Type': 'application/json', 'X-Auth-Token': tokenID}
    http = httplib2.Http()
    path = get_stack_show_url(stack_name, stack_id)
    response1, content1 = http.request(path, 'GET', headers=headers)
    stack_status = json.loads(content1)['stack']['stack_status']
    return stack_status
