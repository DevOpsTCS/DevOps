#!/usr/bin/python

import time
import urllib2
from app import app
from flask import request
import httplib2
import poster
import poster.encode
from poster.streaminghttp import register_openers
from credentials1 import get_catalogue_update_url
from credentials1 import get_catalogue_insert_url
from credentials1 import get_vnf_check_url
from authentication1 import stack_show, stack_create


@app.route('/check-vnf', methods=['POST', 'PUT'])
def launch():
    """Sends request to catalogue to check the status of VNF Package in database
       :param vnf_data: String representing VNF details
       :returns: The status of VNF Package
    """
    vnf_data = request.form.get('nsd_data')
    # Send a request to catalogue to check the status of VNF instance
    url1 = get_vnf_check_url()
    http = httplib2.Http()
    response, content = http.request(url1, 'POST', body=vnf_data)
    return content


@app.route('/launch-vnf-instance', methods=['GET', 'POST', 'PUT'])
def launch_vnf():
    """Launches the NFV Instances
       :param vnfd: file representing VNF Package
       :param image: String representing the Glance image-id
       :param count: Integer value given to set of NFV Instances launched with
                     a particular NSD
       :returns: The status of NSD
    """
    vnfd = request.files["vnfd"]
    image = request.form.get('image_id')
    count = request.form.get('count')
    vnf_name_version = request.form.get('vnf_name_version')
    heat_template = vnfd.read()
    stack_name1 = vnf_name_version + '_' + count
    # Sending request to Heat service for creating the  heat stack
    stack_id1 = stack_create(stack_name1, heat_template, image)
    # Sending request to catalogue to update the NFV instance
    # details in database
    url = get_catalogue_insert_url()
    register_openers()
    params = {'stack_id': stack_id1,
              'vnf_name_version': vnf_name_version,
              'stack_name': stack_name1}
    datagen, headers1 = poster.encode.multipart_encode(params)
    request2 = urllib2.Request(url, datagen, headers1)
    urllib2.urlopen(request2).read()
    # sending request to heat service to show heat stack details for
    #     given stack id
    stack_status = stack_show(stack_name1, stack_id1)
    # Sending request to catalogue to Update NFV instance status
    # stack_update = catalogue_db_update(stack_id1, stack_status)
    url3 = get_catalogue_update_url()
    params = {'stack_id': stack_id1,
              'status': stack_status}
    datagen, headers = poster.encode.multipart_encode(params)
    request3 = urllib2.Request(url3, datagen, headers)
    response3 = urllib2.urlopen(request3).read()
    return response3


@app.route('/delete-vnf-instance', methods=['GET', 'POST', 'PUT', 'DELETE'])
def delete_vnf():
    """Deletes the NFV Instances
       :param stack_name: String representing the name of VNF Package
       :param stack_id: String representing the id of heat-stack
           created with VNF Package
       :returns: The status of
    """
    stack_name = request.form.get('stack_name')
    stack_id = request.form.get('stack_id')
    # sending request to heat service to show heat stack details
    #     for given stack id
    stack_status = stack_name, stack_id
    url1 = get_catalogue_update_url()
    params = {'stack_id': stack_id,
              'status': stack_status}
    datagen, headers1 = poster.encode.multipart_encode(params)
    request1 = urllib2.Request(url1, datagen, headers1)
    urllib2.urlopen(request1).read()
    stack_status1 = stack_status
    while (stack_status1 == 'DELETE_IN_PROGRESS'):
        time.sleep(2)
        stack_status1 = stack_name, stack_id
    # Sending request to catatlogue to Update NFV instance status
    url2 = get_catalogue_update_url()
    params = {'stack_id': stack_id,
              'status': stack_status1}
    datagen, headers3 = poster.encode.multipart_encode(params)
    request3 = urllib2.Request(url2, datagen, headers3)
    response3 = urllib2.urlopen(request3).read()
    return response3
