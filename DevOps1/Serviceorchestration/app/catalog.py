#!/usr/bin/python

# import sqlite3
import datetime
import json
# import os
import urllib2
import poster
from app import app
from app import db, models
from flask import request, jsonify  # , Flask, Request
from poster.streaminghttp import register_openers
from exception import NoVnfPackageException
from exception import VnfNotEnabledException
from exception import NoNsdException
from exception import NoVnfException
from exception import NsdNotEnabledException
from exception import NotOnBoardedException
from credentials import launch_vnf_url


def catalogue_on_board_nsd(nsd_filename, nsd_path):
    """Stores the details of NSD in Database
       :param nsd_filename: String representing name of NSD to be On-boarded
       :param nsd_path: String representing the path where NSD is stored
       :returns: A success or failure message
    """
    db_timestamp = datetime.datetime.now()
    # Updating NSD details in database
    nsd_details = models.NS_Catalogue(name=nsd_filename, status='Disable',
                                      filepath=nsd_path + '_1.0',
                                      timestamp=db_timestamp,
                                      version='1.0',
                                      name_version=nsd_filename + '_1.0')
    db.session.add(nsd_details)
    db.session.commit()
    return 'SUCCESS'


def catalogue_on_board_vnf_package(vnf_filename, vnf_filepath,
                                   image_name, image_path, glance_image_id):
    """Stores the details of VNF Package and image in Database
       :param vnf_filename: String representing name of
                            VNF Package to be On-boarded
       :param vnf_filepath: String representing path where
                            VNF Package is stored
       :param image_name: String representing name of image to be On-boarded
       :param image_path: String representing path where image file is stored
       :param glance_image_id: String representing the image-id
       :returns: The path where image file is stored
    """
    db_timestamp = datetime.datetime.now()
    # Updating NSD details in database
    vnf_details = models.VNF_Catalogue(name=vnf_filename, status='Disable',
                                       filepath=vnf_filepath + '_1.0',
                                       timestamp=db_timestamp,
                                       image_id=glance_image_id, version='1.0',
                                       name_version=vnf_filename + '_1.0',
                                       image_path=image_path,
                                       container_format='bare',
                                       disk_format='qcow2',
                                       is_public='true',
                                       image_name=image_name)
    db.session.add(vnf_details)
    db.session.commit()
    return image_path


def catalogue_query_nsd(nsd_name_version):
    """Retrieves the details of NSD from Database
       :param nsd_name_version: String representing the NSD
       :returns: The details of required NSD
    """
    # Getting NSD details from database
    nsd_details = models.NS_Catalogue.query.get(nsd_name_version)
    if nsd_details is None:
        status = "No NSD of given ID is found"
    else:
        nsd_details1 = {'name': nsd_details.name, 'status': nsd_details.status,
                        'filepath1': nsd_details.filepath,
                        'timestamp': nsd_details.timestamp,
                        'version': nsd_details.version}
        status = jsonify(nsd_details1)
    return status


def catalogue_query_all_nsd():
    """Retrieves the details of NSD from Database
       :param nsd_name_version: String representing the NSD
       :returns: The details of required NSD
    """
    # Getting NSD details from database
    nsd_details = models.NS_Catalogue.query.all()
    nsd_details1 = {}
    if nsd_details is None:
        status = "No NSD is found"
    else:
        for i in nsd_details:
            nsd_details1[i] = {'name': i.name, 'status': i.status,
                               'filepath1': i.filepath,
                               'timestamp': i.timestamp,
                               'version': i.version}
        status = nsd_details1
    return status


def catalogue_query_nfv_instances(nsd_name_version):
    """Retrieves the details of NFV Instances from Database, for given NSD
       :param nsd_name_version: String representing the NSD
       :returns: The details of NFV Instances of required NSD
    """
    nfv_instance_details = {}
    # Getting details of required NSD from database
    nsd_details = models.NS_Catalogue.query.get(nsd_name_version)
    # Getting details of all NFV instances in database
    nfv_instances = models.NFV_Instances.query.all()
    if nsd_details is None:
        status = "No NSD of given ID is found"
    else:
        for i in nfv_instances:
            if i.nsd_name_version == nsd_name_version:
                nfv_instance_details[str(i)] = {'count': i.count,
                                                'name': i.name,
                                                'stack_id': i.stack_id,
                                                'vnf_name_version':
                                                i.vnf_name_version,
                                                'status': i.status,
                                                'timestamp': i.timestamp}
            status = jsonify(nfv_instance_details)
    return status


def catalogue_remove_nfv_instances(nsd_count):
    """Retrieves the details of set of NFV Instances launched using a
       particular NSD
       :param nsd_count: Integer value given to set of NFV Instances
                         launched using a particular NSD
       :returns: The details of NFV Instances for given NSD Count
    """
    nfv_instance_details = {}
    # Getting details of all NFV instances having same count
    nfv_instances = models.NFV_Instances.query.filter_by(count=nsd_count[0])
    for i in nfv_instances:
        nfv_instance_details[i.stack_id] = i.name
    return nfv_instance_details


def catalogue_query_vnf_package(vnf_name_version):
    """Retrieves the details of required VNF Package
       :param vnf_name_version: String representing the VNF Package
       :returns: The details of given VNF Package
    """
    # Getting details of the required VNF from database
    vnf_details = models.VNF_Catalogue.query.get(vnf_name_version)
    if vnf_details is None:
        status = "No Package of given ID is found"
    else:
        vnf_details1 = {'name': vnf_details.name, 'status': vnf_details.status,
                        'filepath': vnf_details.filepath,
                        'timestamp': vnf_details.timestamp,
                        'version': vnf_details.version}
        status = jsonify(vnf_details1)
    return status


def catalogue_update_nsd(name, path):
    """Updates the details of NSD in database
       :param name: String representing the NSD
       :param path: String representing the path of NSD file
       :returns: Version of updated NSD
    """
    db_name = name
    version = []
    # Getting details of all the NSDs for a given filename
    nsd_details = models.NS_Catalogue.query.filter_by(name=str(db_name))
    for i in nsd_details:
        version.append(i.version)
    if version == []:
        raise NotOnBoardedException
    db_version = str(max(version) + 1.0)
    # Updating NSD details in database
    nsd_updated = models.NS_Catalogue(
        name=db_name, status='Disable', filepath=path,
        timestamp=datetime.datetime.now(),
        version=db_version, name_version=(db_name + '_' + db_version))
    db.session.add(nsd_updated)
    db.session.commit()
    return db_version


def catalogue_update_vnf_package(name, path):
    """Updates the details of VNF Package in database
       :param name: String representing the VNF Package
       :param path: String representing the path of VNF Package
       :returns: Version of updated VNF Package
    """
    db_name = name
    version = []
    # Getting details of all the NSDs for a given filename
    nsd_details = models.NS_Catalogue.query.filter_by(name=str(db_name))
    for i in nsd_details:
        version.append(i.version)
    if version == []:
        raise NotOnBoardedException
    db_version = str(max(version) + 1.0)
    # Updating NSD details in database
    nsd_updated = models.NS_Catalogue(
        name=db_name, status='Disable', filepath=path,
        timestamp=datetime.datetime.now(), count=0,
        version=db_version, name_version=(db_name + '_' + db_version))
    db.session.add(nsd_updated)
    db.session.commit()
    return db_version


def catalogue_get_image_id(vnf_name_version):
    """Retrieves the image-id for given VNF package
      :param vnf_name_version: String representing the VNF package
      :returns: Image-id for given VNF Package
    """
    # Getting details of the required VNf from database
    vnf_details = models.VNF_Catalogue.query.get(vnf_name_version)
    if vnf_details is None:
        raise NoVnfException
    else:
        status = vnf_details.image_id
    return status


def catalogue_delete_vnf_package(vnf_name_version):
    """Deletes the VNF Package in the database
       :param vnf_name_version: String representing the VNF Package
       :returns: The status of VNF Package
    """
    # Getting details of the required VNf from database
    vnf_details = models.VNF_Catalogue.query.get(vnf_name_version)
    if vnf_details is None:
        status = "No Package of given ID is found"
    else:
        if vnf_details.status == 'Disable':
            db.session.delete(vnf_details)
            db.session.commit()
            status = "VNF Package Deleted"
        elif vnf_details.status == 'Enable':
            # Getting details of all NFV instances to check if any instance
            #    launched using this VNF Package is in running state
            nfv_instance_details = models.NFV_Instances.query.all()
            for i in nfv_instance_details:
                if i.vnf_name_version == vnf_name_version and \
                        i.status == 'Running':
                    status = "Instance launched using this package is \
                    running. So VNF Package cannot be deleted"
                else:
                    status = "VNF Package cannot be Deleted as it is enabled"
    return status


def catalogue_delete_nsd(nsd_name_version):
    """Deletes the NSD in database
       :param nsd_name_version: String representing the NSD
       :returns: The status of NSD
    """
    # Getting details of the required NSD from database
    nsd_details = models.NS_Catalogue.query.get(nsd_name_version)
    if nsd_details is None:
        raise NoNsdException
        # status = "No NSD of given ID is found"
    else:
        if nsd_details.status == 'Disable':
            db.session.delete(nsd_details)
            db.session.commit()
            status = 'NSD Deleted'
        elif nsd_details.status == 'Enable':
            # Getting details of all NFV instances to check if any instance
            #     launched using this NSd is in running state
            nfv_instance_details = models.NFV_Instances.query.all()
            for i in nfv_instance_details:
                if i.nsd_name_version == nsd_name_version and \
                        i.status == 'Running':
                    status = "Instance launched with this Network Service is \
                    running. So NSD cannot be deleted"
                else:
                    status = "NSD cannot be Deleted as it is enabled"
    return status


def catalogue_enable_vnf_package(vnf_name_version):
    """Enables the VNF Package in database
       :param vnf_name_version: String representing the VNF Package
       :returns: The status of VNF Package
    """
    # Getting details of the required VNF pacakge from database
    vnf_details = models.VNF_Catalogue.query.get(vnf_name_version)
    if vnf_details is None:
        raise NoVnfException
    else:
        if vnf_details.status == 'Disable':
            vnf_details.status = 'Enable'
            db.session.commit()
            status = "VNF Package Enabled"
        elif vnf_details.status == 'Enable':
            status = "VNF Package is already Enabled"
    return status


def catalogue_enable_nsd(nsd_name_version):
    """Enables NSD in database
       :param nsd_name_version: String representing NSD
       :returns: The status of NSD
    """
    # Getting details of the required VNF pacakge from database
    nsd_details = models.NS_Catalogue.query.get(nsd_name_version)
    if nsd_details is None:
        status = "No NSD of given ID is found"
    else:
        if nsd_details.status == 'Disable':
            nsd_details.status = 'Enable'
            db.session.commit()
            status = "NSD Enabled"
        elif nsd_details.status == 'Enable':
            status = "NSD is already Enabled"
    return status


def catalogue_disable_vnf_package(vnf_name_version):
    """Disables the VNF Package in database
       :param vnf_name_version: String representing the VNF Package
       :returns: The status of VNF Package
    """
    # Getting details of the required VNF pacakge from database
    vnf_details = models.VNF_Catalogue.query.get(vnf_name_version)
    if vnf_details is None:
        status = "No Package of given ID is found"
    else:
        if vnf_details.status == 'Enable':
            # Getting details of all NFV instances to check if any instance
            #     launched using this VNF Package is in running state
            nfv_instance_details = models.NFV_Instances.query.all()
            for i in nfv_instance_details:
                if i.nsd_name_version == vnf_name_version and \
                        i.status == 'Running':
                    status = "Instance launched with this Network Service is \
                    running. So NSD cannot be disabled"
                    break
            else:
                vnf_details.status = 'Disable'
                db.session.commit()
                status = "VNF Package Disabled"
        elif vnf_details.status == 'Disable':
            status = "VNF Package is already Disabled"
    return status


def catalogue_disable_nsd(nsd_name_version):
    """Disables NSD in database
       :param nsd_name_version: String representing NSD
       :returns: The status of NSD
    """
    # Getting details of the required NSD from database
    nsd_details = models.NS_Catalogue.query.get(nsd_name_version)
    if nsd_details is None:
        status = "No NSD of given ID is found"
    else:
        if nsd_details.status == 'Enable':
            # Getting details of all NFV instances to check if any instance
            #     launched using this NSD is in running state
            nfv_instance_details = models.NFV_Instances.query.all()
            for i in nfv_instance_details:
                if i.nsd_name_version == nsd_name_version and \
                        i.status == 'Running':
                    status = "Cannot delete NSD as Instance launched with it \
                    is running"
                    break
            else:
                nsd_details.status = 'Disable'
                db.session.commit()
                status = "NSD Disabled"
        elif nsd_details.status == 'Disable':
            status = "NSD is already Disabled"
    return status


def catalogue_check_nsd(name_version):
    """Checks the status of NSD in database
       :param name_version: String representing NSD
       :raises: `flask.common.exception.ServiceOrchestration`
       :returns: The status of NSD
    """
    # Getting details of the required NSD from database
    nsd_details = models.NS_Catalogue.query.get(name_version)
    print name_version
    # A unique value is given to all nfv instances launched using a
    #     particular NSD
    if nsd_details is None:
        raise NoNsdException
        # status = "No NSD of given ID is found"
    else:
        if nsd_details.status == 'Enable':
            print nsd_details.filepath
            status = nsd_details.filepath
        else:
            raise NsdNotEnabledException
            # status = "Not Enabled"
    return status


def catalogue_count_nsd(name_version):
    """Retrieves the count of NSD from database
       :param name_version: String representing NSD
       :returns: The count of NSD
    """
    # Getting the details of NFV instances launched using the given NSD
    list1 = []
    nfv_instance_details = models.NFV_Instances.query.filter_by(
        nsd_name_version=eval(json.dumps(name_version[0])))
    for i in nfv_instance_details:
        # A unique value is given to all nfv instances launched using a
        #     particular NSD
        list1.append(i.count)
    if list1 == []:
        count = 1
    else:
        count = int(max(list1)) + 1
    return count


def catalogue_update_nfv_instances(name_version, nsd_count):
    """Updates the status of NFV Instances in database
       :param name_version: String representing NSD
       :param count: Integer value given to set of NFV Instances
                     launched with a particular NSD
    """
    nsd_status_update = models.NFV_Instances(
        nsd_name_version=eval(json.dumps(name_version))[0],
        status='Instantiating', count=nsd_count)
    db.session.add(nsd_status_update)
    db.session.commit()


def catalogue_check_vnf(vnf_name_version):
    """checks VNF status in the dattabase
       :param vnf_name_version: String representing VNF Package
       :returns: The status of VNF Package
    """
    # Getting the details of the required vnf from database
    vnf_details = models.VNF_Catalogue.query.get(vnf_name_version)
    if vnf_details is None:
        raise NoVnfPackageException
        # status = "No Package of given ID is found"
    else:
        if vnf_details.status == 'Enable':
            status = "Enabled"
        else:
            raise VnfNotEnabledException
            # status = "Not Enabled"
    return status


@app.route('/catalogue-check-vnf-instance', methods=['POST', 'PUT', 'GET'])
def catalogue_check_vnf_instances():
    """Sends VNFD to VNFM for launching NFV Instances
       :param vnf_name_version: String representing VNF Package
       :returns: Success or failure message
    """
    vnf_name_version = request.data
    # Getting the details of all the NFV instances from database
    nfv_instance_details = models.NFV_Instances.query.all()
    for i in nfv_instance_details:
        if i.status == 'Instantiating':
            count = i.count
    path = launch_vnf_url()
    register_openers()
    # Getting the details of  the required VNF package
    vnf_details = models.VNF_Catalogue.query.get(vnf_name_version)
    params = {'vnfd': open(vnf_details.filepath, "rb"),
              'image_id': vnf_details.image_id,
              'vnf_name_version': vnf_name_version,
              'count': count}
    datagen, headers = poster.encode.multipart_encode(params)
    request1 = urllib2.Request(path, datagen, headers)
    response = urllib2.urlopen(request1).read()
    return response


@app.route('/catalogue_db_insert', methods=['POST', 'PUT', 'GET'])
def stacks():
    """Inserts NFV Instance details in database
       :returns: Success or failure message
    """
    # Getting the details of all NFV instances
    nfv_instance_details = models.NFV_Instances.query.all()
    for i in nfv_instance_details:
        # Updating NFV instance details
        if i.status == 'Instantiating':
            i.name = request.form.get('stack_name')
            i.stack_id = request.form.get('stack_id')
            i.vnf_name_version = request.form.get('vnf_name_version')
            i.status = 'CREATE_IN_PROGRESS'
            i.timestamp = datetime.datetime.now()
            db.session.commit()
    return "SUCCESS"


@app.route('/catalogue_db_update', methods=['POST', 'PUT', 'GET'])
def catalogue_update():
    """Updates the status of NFV Instances in database
       :param _id: String representing
       :returns: The status of NFV Instances
    """
    stack_id1 = request.form.get('stack_id')
    # Getting the details of NFV instance for given stack id
    NFV_instance = models.NFV_Instances.query.filter_by(stack_id=stack_id1)
    if NFV_instance is None:
        status = "No NFV Instance of given ID is found"
    else:
        # Updating the status of NFV instance
        for i in NFV_instance:
            i.status = request.form.get('status')
            db.session.commit()
        status = request.form.get('status')
    resp = {"stack_id": stack_id1,
            "status": status}
    status = jsonify(resp)
    return status
