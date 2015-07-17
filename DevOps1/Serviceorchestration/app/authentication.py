# import keystoneclient.v2_0.client as ksclient
from credentials import get_keystone_creds
# from app.views import On-board-VNF-Package


def keystone_auth():
    creds = get_keystone_creds()
    keystone = creds
    tokenID = keystone.auth_token
    return tokenID


def image_create(path):
    glance = keystone_auth()
    with open(path) as fimage:
        glance.images.create(name="success",
                             is_public=True,
                             disk_format="qcow2",
                             container_format="bare",
                             data=fimage)
    image_id = glance.images.list().next().id
    return image_id


def image_delete(image_id):
    glance = keystone_auth()
    glance.images.delete(image_id)
