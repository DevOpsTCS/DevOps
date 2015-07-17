from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
VNF__catalogue = Table('VNF__catalogue', pre_meta,
    Column('name', VARCHAR(length=64)),
    Column('status', VARCHAR(length=64)),
    Column('file1', BLOB),
    Column('timestamp', DATETIME),
    Column('count', VARCHAR),
    Column('version', INTEGER),
    Column('name_version', VARCHAR(length=64), primary_key=True, nullable=False),
    Column('file2', BLOB),
    Column('container_format', VARCHAR(length=64)),
    Column('disk_format', VARCHAR(length=64)),
    Column('is_public', VARCHAR(length=6)),
    Column('image_name', VARCHAR(length=64)),
)

VNF__catalogue = Table('VNF__catalogue', post_meta,
    Column('name', String(length=64)),
    Column('status', String(length=64)),
    Column('filepath1', BLOB),
    Column('timestamp', DateTime),
    Column('count', String),
    Column('version', Integer),
    Column('name_version', String(length=64), primary_key=True, nullable=False),
    Column('filepath2', BLOB),
    Column('container_format', String(length=64)),
    Column('disk_format', String(length=64)),
    Column('is_public', String(length=6)),
    Column('image_name', String(length=64)),
)

NS__catalogue = Table('NS__catalogue', pre_meta,
    Column('name', VARCHAR(length=64)),
    Column('status', VARCHAR(length=64)),
    Column('file1', BLOB),
    Column('timestamp', DATETIME),
    Column('count', INTEGER),
    Column('version', INTEGER),
    Column('name_version', VARCHAR(length=64), primary_key=True, nullable=False),
)

NS__catalogue = Table('NS__catalogue', post_meta,
    Column('name', String(length=64)),
    Column('status', String(length=64)),
    Column('filepath1', BLOB),
    Column('timestamp', DateTime),
    Column('count', Integer),
    Column('version', Integer),
    Column('name_version', String(length=64), primary_key=True, nullable=False),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['VNF__catalogue'].columns['file1'].drop()
    pre_meta.tables['VNF__catalogue'].columns['file2'].drop()
    post_meta.tables['VNF__catalogue'].columns['filepath1'].create()
    post_meta.tables['VNF__catalogue'].columns['filepath2'].create()
    pre_meta.tables['NS__catalogue'].columns['file1'].drop()
    post_meta.tables['NS__catalogue'].columns['filepath1'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['VNF__catalogue'].columns['file1'].create()
    pre_meta.tables['VNF__catalogue'].columns['file2'].create()
    post_meta.tables['VNF__catalogue'].columns['filepath1'].drop()
    post_meta.tables['VNF__catalogue'].columns['filepath2'].drop()
    pre_meta.tables['NS__catalogue'].columns['file1'].create()
    post_meta.tables['NS__catalogue'].columns['filepath1'].drop()
