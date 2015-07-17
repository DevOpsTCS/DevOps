from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
flavor__types = Table('flavor__types', post_meta,
    Column('id', Integer),
    Column('name', String(length=64), primary_key=True, nullable=False),
    Column('vcpus', Integer),
    Column('memory_mb', Integer),
    Column('disk_gb', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['flavor__types'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['flavor__types'].drop()
