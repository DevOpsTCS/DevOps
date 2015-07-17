#!/usr/bin/python
from app import app
from flask import request
import urllib2
import os
from poster.streaminghttp import register_openers
import poster.encode
from app.exception import InvalidFileException, InvalidInputException
from catalog import catalogue_on_board_nsd, catalogue_on_board_vnf_package
from catalog import catalogue_query_nsd, catalogue_query_nfv_instances
from catalog import catalogue_remove_nfv_instances, catalogue_query_vnf_package
from catalog import catalogue_update_nsd, catalogue_update_vnf_package
from catalog import catalogue_get_image_id, catalogue_delete_vnf_package
from catalog import catalogue_delete_nsd, catalogue_enable_vnf_package
from catalog import catalogue_enable_nsd, catalogue_disable_vnf_package
from catalog import catalogue_disable_nsd, catalogue_check_nsd
from catalog import catalogue_count_nsd, catalogue_update_nfv_instances
from catalog import catalogue_check_vnf, catalogue_query_all_nsd
from credentials import instantiate_vnfm, remove_vnfm
from credentials import NSD_FOLDER, NSD_DELETED, VNFPACKAGE_FOLDER
from credentials import VNFPACKAGE_DELETED, IMAGE_FOLDER
from credentials import ALLOWED_EXTENSIONS, ALLOWED_EXTENSIONS1, ver
from authentication import image_create, image_delete
nsd_instantiation_ongoing = False


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def allowed_image(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS1


@app.route('/on-board-nsd', methods=['PUT', 'POST'])
def onboard_nsd():
    """On-boards the given NSD
       :param nsd_file: File representing NSD to be On-boarded
       :raises: flask.common.exception.ServiceOrchestrator
       :returns: A success or failure message
    """
    nsd_file = request.files.get('nsd_file')  # gives you a FileStorage
    try:
        if not nsd_file:
            raise InvalidInputException
        elif not allowed_file(nsd_file.filename):
            raise InvalidFileException(what=nsd_file.filename, required='yaml')
        else:
            status = catalogue_on_board_nsd(
                nsd_file.filename, NSD_FOLDER + nsd_file.filename)
            # saves file in NSD_FOLDER
            nsd_file.save(os.path.join(NSD_FOLDER,
                                       '_'.join([nsd_file.filename, ver])))
    except Exception as err:
        return err.__str__()
    return status


@app.route('/on-board-vnf-package', methods=['PUT', 'POST'])
def onboard_vnf():
    """On-boards the given VNF Package
       :param vnf_file: File representing VNF Package to be On-boarded
       :param image_file: File representing the image to be on-boarded
       :raises: flask.common.exception.ServiceOrchestrator
       :returns: A success or failure message
    """
    vnf_file = request.files.get('vnf_file')   # gives you a FileStorage
    image_file = request.files.get('image_file')
    try:
        if not vnf_file or not image_file:
            raise InvalidInputException
        elif not allowed_file(vnf_file.filename):
            raise InvalidFileException(what=vnf_file.filename, required='yaml')
        elif not allowed_image(image_file.filename):
            raise InvalidFileException(what=image_file.filename,
                                       required='img')
        else:
            vnf_file.save(os.path.join(VNFPACKAGE_FOLDER,
                                       '_'.join([vnf_file.filename, ver])))
            image_file.save(os.path.join(IMAGE_FOLDER,
                                         image_file.filename))
            path = (IMAGE_FOLDER + image_file.filename)
            image_id = image_create(path)
            catalogue_on_board_vnf_package(vnf_file.filename,
                                           VNFPACKAGE_FOLDER
                                           + vnf_file.filename,
                                           image_file.filename,
                                           IMAGE_FOLDER
                                           + image_file.filename,
                                           image_id)
    except Exception as err:
        return err.__str__()
    return 'SUCCESS'


@app.route('/disable-nsd', methods=['PUT', 'POST'])
def disable_nsd():
    """Disables the given NSD
       :param nsd_name_version: String representing NSD to be disabled
       :raises: flask.common.exception.ServiceOrchestrator
       :returns: A success or failure message
    """
    try:
        # nsd_name_version sent from curl command retrieved
        nsd_name_version = request.form.get('nsd_name_version')
        if not nsd_name_version:
            raise InvalidInputException
        status = catalogue_disable_nsd(nsd_name_version)
    except Exception as err:
        return err.__str__()
    return status


@app.route('/disable-vnf-package', methods=['PUT', 'POST'])
def disable_vnf_package():
    """Disables the given VNF Package
       :param vnf_name_version: String representing VNF Package to be disabled
       :raises: flask.common.exception.ServiceOrchestrator
       :returns: A success or failure message
    """
    try:
        # vnf_name_version sent from curl command retrieved
        vnf_name_version = request.form.getlist('vnf_name_version')
        if not vnf_name_version:
            raise InvalidInputException
        status = catalogue_disable_vnf_package(vnf_name_version)
    except Exception as err:
        return err.__str__()
    return status


@app.route('/enable-nsd', methods=['PUT', 'POST'])
def enable_nsd():
    """Enables the given NSD
       :param nsd_name_version: String representing NSD to be enabled
       :raises: flask.common.exception.ServiceOrchestrator
       :returns: A success or failure message
    """
    try:
        # nsd_name_version sent from curl command retrieved
        nsd_name_version = request.form.getlist('nsd_name_version')
        if not nsd_name_version:
            raise InvalidInputException
        status = catalogue_enable_nsd(nsd_name_version)
    except Exception as err:
        return err.__str__()
    return status


@app.route('/enable-vnf-package', methods=['PUT', 'POST'])
def enable_vnf_package():
    """Enables the given VNF Package
       :param vnf_name_version: String representing VNF Package to be enabled
       :raises: flask.common.exception.ServiceOrchestrator
       :returns: A success or failure message
    """
    try:
        # vnf_name_version sent from curl command retrieved
        vnf_name_version = request.form.getlist('vnf_name_version')
        if not vnf_name_version:
            raise InvalidInputException
        status = catalogue_enable_vnf_package(vnf_name_version)
    except Exception as err:
        return err.__str__()
    return status


@app.route('/delete-vnf-package', methods=['PUT', 'POST'])
def delete_vnf_package():
    """Deletes the given VNF Package
       :param vnf_name_version: String representing VNF Package to be deleted
       :raises: flask.common.exception.ServiceOrchestrator
       :returns: A success or failure message
    """
    try:
        # vnf_name_version sent from curl command retrieved
        vnf_name_version = request.form.getlist('vnf_name_version')
        if not vnf_name_version:
            raise InvalidInputException
        image_id = catalogue_get_image_id(vnf_name_version)
        # if returned_status == 'No Package of given ID is found':
        #    return returned_status
        image_delete(image_id)
        status = catalogue_delete_vnf_package(vnf_name_version)
        # move the deleted vnf to another folder
        if status == 'VNF Deleted':
            os.rename(VNFPACKAGE_FOLDER +
                      request.form.getlist('vnf_name_version')[0],
                      VNFPACKAGE_DELETED +
                      request.form.getlist('vnf_name_version')[0])
    except Exception as err:
        return err.__str__()
    return status


@app.route('/delete-nsd', methods=['PUT', 'POST'])
def delete_nsd():
    """Deletes the given NSD
       :param nsd_name_version: String representing NSD to be deleted
       :raises: flask.common.exception.ServiceOrchestrator
       :returns: A success or failure message
    """
    try:
        # nsd_name_version sent from curl command retrieved
        nsd_name_version = request.form.getlist('nsd_name_version')
        if not nsd_name_version:
            raise InvalidInputException
        status = catalogue_delete_nsd(nsd_name_version)
        # move the deleted nsd to another folder
        if status == 'NSD Deleted':
            os.rename(NSD_FOLDER +
                      request.form.getlist('nsd_name_version')[0],
                      NSD_DELETED +
                      request.form.getlist('nsd_name_version')[0])
    except Exception as err:
        return err.__str__()
    return status


@app.route('/update-nsd', methods=['PUT', 'POST'])
def update_nsd():
    """Updates the given NSD
       :param nsd_file: File representing NSD to be updated
       :raises: flask.common.exception.ServiceOrchestrator
       :returns: A success or failure message
    """
    try:
        nsd_file = request.files.get('nsd_file')   # gives you a FileStorage
        if not nsd_file:
            raise InvalidInputException
        elif not allowed_file(nsd_file.filename):
            raise InvalidFileException(what=nsd_file.filename, required='yaml')
        else:
            status = catalogue_update_nsd(
                nsd_file.filename, NSD_FOLDER + nsd_file.filename)
            # if status == 'NSD not OnBoarded':
            #    return status
            nsd_file.save(os.path.join(NSD_FOLDER,
                                       '_'.join([nsd_file.filename, status])))
    except Exception as err:
        return err.__str__()
    return 'NSD Updated'


@app.route('/update-vnf-package', methods=['PUT', 'POST'])
def update_vnf_package():
    try:
        vnf_file = request.files.get('vnf_file')   # gives you a FileStorage
        if not vnf_file:
            raise InvalidInputException
        elif not allowed_file(vnf_file.filename):
            raise InvalidFileException(what=vnf_file.filename, required='yaml')
        else:
            status = catalogue_update_vnf_package(
                vnf_file.filename, VNFPACKAGE_FOLDER + vnf_file.filename)
            # if status == 'VNF not OnBoarded':
            #    return status
            vnf_file.save(os.path.join(VNFPACKAGE_FOLDER,
                                       '_'.join([vnf_file.filename, status])))
    except Exception as err:
        return err.__str__()
    return 'NSD Updated'


@app.route('/query-nsd', methods=['PUT', 'POST'])
def query_nsd():
    """Retrives the details of the given NSD
       :param nsd_name_version: String representing NSD to be queried
       :raises: flask.common.exception.ServiceOrchestrator
       :returns: The details of NSD
    """
    try:
        # nsd_name_version sent from curl command retrieved
        nsd_name_version = request.form.getlist('nsd_name_version')
        if not nsd_name_version:
            raise InvalidInputException
        status = catalogue_query_nsd(nsd_name_version)
    except Exception as err:
        return err.__str__()
    return status


@app.route('/query-all-nsd', methods=['PUT', 'POST'])
def query_all_nsd():
    """Retrives the details of the given NSD
       :param nsd_name_version: String representing NSD to be queried
       :raises: flask.common.exception.ServiceOrchestrator
       :returns: The details of NSD
    """
    try:
        # nsd_name_version sent from curl command retrieved
        # nsd_name_version = request.form.getlist('nsd_name_version')
        # if not nsd_name_version:
        #     raise InvalidInputException
        status = catalogue_query_all_nsd()
    except Exception as err:
        return err.__str__()
    return status


@app.route('/query-vnf-package', methods=['PUT', 'POST'])
def query_vnf_package():
    """Retrives the details of the given VNF Package
       :param vnf_name_version: String representing VNF Package to be queried
       :raises: flask.common.exception.ServiceOrchestrator
       :returns: The details of VNF package
    """
    try:
        # vnf_name_version sent from curl command retrieved
        vnf_name_version = request.form.getlist('vnf_name_version')
        if not vnf_name_version:
            raise InvalidInputException
        status = catalogue_query_vnf_package(vnf_name_version)
    except Exception as err:
        return err.__str__()
    return status


@app.route('/instantiate_nsd', methods=['PUT', 'POST'])
def instantiate_nsd():
    """Instantiates the given NSD
       :param nsd_name_version: String representing NSD to be instantiated
       :raises: flask.common.exception.ServiceOrchestrator
       :returns: Success or failure message
    """
    global nsd_instantiation_ongoing
    if nsd_instantiation_ongoing:
        return "NSD instantiation is ongoing.. Pls try later"
    nsd_instantiation_ongoing = True
    try:
        nsd_name_version = request.form.getlist('nsd_name_version')
        if not nsd_name_version:
            raise InvalidInputException
        # check the status of nsd
        status = catalogue_check_nsd(nsd_name_version)
        nsd_filepath = status
        # open nsd file
        with open(nsd_filepath, 'rb') as input_file:
            nsd_read_data = input_file.read()
        # convert string to list
        nsd_data = eval(nsd_read_data)
        number_of_vnfs_enabled = 0
        # check the status of vnfs
        for i in range(len(nsd_data)):
            status1 = catalogue_check_vnf(nsd_data[i])
            if status1 == 'Enabled':
                number_of_vnfs_enabled = number_of_vnfs_enabled + 1
        # send request to vnf manager to launch vnf
        # instances if all the required vnfs are enabled
        if number_of_vnfs_enabled == len(nsd_data):
            count = catalogue_count_nsd(nsd_name_version)
            for i in range(len(nsd_data)):
                catalogue_update_nfv_instances(nsd_name_version, count)
                url = instantiate_vnfm()
                register_openers()
                params = {'nsd_data': nsd_data[i]}
                datagen, headers = poster.encode.multipart_encode(params)
                request1 = urllib2.Request(url, datagen, headers)
                response = urllib2.urlopen(request1).read()
    except Exception as err:
        return err.__str__()
    finally:
        nsd_instantiation_ongoing = False
    return response


@app.route('/query_nfv_instances', methods=['PUT', 'POST'])
def query_nfv_instances():
    """Retrives the details of NFV Instances launched using the given NSD
       :param nsd_name_version: String representing NSD
       :raises: flask.common.exception.ServiceOrchestrator
       :returns: The details of VNF Instances launched using the given NSD
    """
    try:
        nsd_name_version = request.form.getlist('nsd_name_version')
        if not nsd_name_version:
            raise InvalidInputException
        status = catalogue_query_nfv_instances(nsd_name_version)
    except Exception as err:
        return err.__str__()
    return status


@app.route('/remove_nfv_instances', methods=['PUT', 'POST'])
def remove_nfv_instance():
    """Removes the NFV Instances launched using the given NSD
       :param nsd_count: Integer value given to set of NFV Instances
           launched using the given NSD
       :raises: flask.common.exception.ServiceOrchestrator
       :returns: A Success or failure message
    """
    try:
        nsd_count = request.form.getlist('count')
        if not nsd_count:
            raise InvalidInputException
        status = catalogue_remove_nfv_instances(nsd_count)
        for key, value in status.items():
            path1 = remove_vnfm()
            register_openers()
            params = {'stack_name': value,
                      'stack_id': key}
            datagen, headers = poster.encode.multipart_encode(params)
            request1 = urllib2.Request(path1, datagen, headers)
            response2 = urllib2.urlopen(request1).read()
    except Exception as err:
        return err.__str__()
    return response2
