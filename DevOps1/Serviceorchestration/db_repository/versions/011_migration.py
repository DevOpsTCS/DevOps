from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
resources__information = Table('resources__information', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('vcpus', Integer),
    Column('local_gb_used', Integer),
    Column('memory_mb_used', Integer),
    Column('memory_mb', Integer),
    Column('free_disk_gb', Integer),
    Column('local_gb', Integer),
    Column('free_ram_mb', Integer),
    Column('updated_at', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['resources__information'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['resources__information'].drop()
