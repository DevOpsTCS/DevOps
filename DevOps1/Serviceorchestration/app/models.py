from app import db


class NS_Catalogue(db.Model):
    name = db.Column(db.String(64), index=True)
    status = db.Column(db.String(64), index=True)
    filepath = db.Column(db.BLOB, index=True)
    timestamp = db.Column(db.DateTime)
    version = db.Column(db.Integer)
    name_version = db.Column(db.String(64), primary_key=True)

    def __repr__(self):
        return '<User %r>' % (self.name)


class VNF_Catalogue(db.Model):
    name = db.Column(db.String(64), index=True)
    status = db.Column(db.String(64), index=True)
    filepath = db.Column(db.BLOB, index=True)
    timestamp = db.Column(db.DateTime)
    image_id = db.Column(db.String)
    version = db.Column(db.Integer)
    name_version = db.Column(db.String(64), primary_key=True)
    image_path = db.Column(db.BLOB, index=True)
    container_format = db.Column(db.String(64), index=True)
    disk_format = db.Column(db.String(64), index=True)
    is_public = db.Column(db.String(6), index=True)
    image_name = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<User %r>' % (self.name)


class NFV_Instances(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    count = db.Column(db.Integer)
    stack_id = db.Column(db.String(64), index=True)
    nsd_name_version = db.Column(db.String(64))
    vnf_name_version = db.Column(db.String(64))
    status = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return '<User %r>' % (self.name)


class Resources_Information(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    vcpus = db.Column(db.Integer)
    local_gb_used = db.Column(db.Integer, index=True)
    memory_mb_used = db.Column(db.Integer, index=True)
    memory_mb = db.Column(db.Integer, index=True)
    free_disk_gb = db.Column(db.Integer, index=True)
    local_gb = db.Column(db.Integer, index=True)
    free_ram_mb = db.Column(db.Integer, index=True)
    updated_at = db.Column(db.DateTime)

    def __repr__(self):
        return '<User %r>' % (self.name)


class Flavor_Types(db.Model):
    id = db.Column(db.Integer)
    name = db.Column(db.String(64), index=True, primary_key=True)
    vcpus = db.Column(db.Integer)
    memory_mb = db.Column(db.Integer, index=True)
    disk_gb = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<User %r>' % (self.name)
