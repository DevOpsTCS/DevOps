#!/usr/bin/python


def get_keystone_creds():
    d = {}
    d['username'] = 'admin'
    d['password'] = 'test'
    d['auth_url'] = 'http://10.138.97.156:5000/v2.0/'
    d['tenant_name'] = 'admin'
    return d


def get_glance_url():
    auth_url = 'http://10.138.97.156:9292/v1/images'
    return auth_url


def instantiate_vnfm():
    auth_url = 'http://10.138.97.172:5070/check-vnf'
    return auth_url


def remove_vnfm():
    auth_url = 'http://10.138.97.172:5070/delete-vnf-instance'
    return auth_url


def launch_vnf_url():
    auth_url = 'http://10.138.97.172:5070/launch-vnf-instance'
    return auth_url


NSD_FOLDER = 'app/../NSD/'
NSD_DELETED = 'app/../NSD_Deleted/'
VNFPACKAGE_FOLDER = 'app/../VNFPackage/'
VNFPACKAGE_DELETED = 'app/../VNF_Deleted/'
IMAGE_FOLDER = 'app/../IMAGES/'
ALLOWED_EXTENSIONS = 'yaml'
ALLOWED_EXTENSIONS1 = 'img'
ver = '1.0'
