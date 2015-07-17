#!/usr/bin/python


def get_keystone_creds():
    d = {}
    d['username'] = 'admin'
    d['password'] = 'test'
    d['auth_url'] = 'http://10.138.97.156:5000/v2.0/'
    d['tenant_name'] = 'admin'
    return d


def get_vnf_check_url():
    vnf_check_url = 'http://10.138.97.172:5070/catalogue-check-vnf-instance'
    return vnf_check_url


def get_heat_url():
    # auth_url = 'http://10.138.97.156:8004/v1//stacks'
    return 'auth_url'


def get_catalogue_insert_url():
    db_insert_url = 'http://10.138.97.172:5070/catalogue_db_insert'
    return db_insert_url


def get_stack_show_url(stack_name, stack_id):
    # stack_show_url = 'http://10.138.97.156:8004/v1/ % (stack_name, stack_id)
    return 'stack_show_url'


def get_catalogue_update_url():
    db_update_url = 'http://10.138.97.172:5070/catalogue_db_update'
    return db_update_url
