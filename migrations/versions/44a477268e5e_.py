"""empty message

Revision ID: 44a477268e5e
Revises: 1877262ba3de
Create Date: 2016-03-07 14:53:14.725000

"""

# revision identifiers, used by Alembic.
revision = '44a477268e5e'
down_revision = '1877262ba3de'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('apicache_characteraffiliation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('corporationID', sa.Integer(), nullable=True),
    sa.Column('corporationName', sa.String(length=100), nullable=True),
    sa.Column('allianceID', sa.Integer(), nullable=True),
    sa.Column('allianceName', sa.String(length=100), nullable=True),
    sa.Column('expire', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_apicache_characteraffiliation_allianceID'), 'apicache_characteraffiliation', ['allianceID'], unique=False)
    op.create_index(op.f('ix_apicache_characteraffiliation_allianceName'), 'apicache_characteraffiliation', ['allianceName'], unique=False)
    op.create_index(op.f('ix_apicache_characteraffiliation_corporationID'), 'apicache_characteraffiliation', ['corporationID'], unique=False)
    op.create_index(op.f('ix_apicache_characteraffiliation_corporationName'), 'apicache_characteraffiliation', ['corporationName'], unique=False)
    op.create_index(op.f('ix_apicache_characteraffiliation_name'), 'apicache_characteraffiliation', ['name'], unique=True)
    op.create_table('ban',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('reason', mysql.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ban_name'), 'ban', ['name'], unique=True)
    op.drop_table('alliance_bans')
    op.drop_table('corporation_bans')
    op.drop_column('characters', 'reason')
    op.drop_column('characters', 'banned')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('characters', sa.Column('banned', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.add_column('characters', sa.Column('reason', mysql.TEXT(), nullable=True))
    op.create_table('corporation_bans',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('reason', mysql.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('alliance_bans',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('reason', mysql.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.drop_index(op.f('ix_ban_name'), table_name='ban')
    op.drop_table('ban')
    op.drop_index(op.f('ix_apicache_characteraffiliation_name'), table_name='apicache_characteraffiliation')
    op.drop_index(op.f('ix_apicache_characteraffiliation_corporationName'), table_name='apicache_characteraffiliation')
    op.drop_index(op.f('ix_apicache_characteraffiliation_corporationID'), table_name='apicache_characteraffiliation')
    op.drop_index(op.f('ix_apicache_characteraffiliation_allianceName'), table_name='apicache_characteraffiliation')
    op.drop_index(op.f('ix_apicache_characteraffiliation_allianceID'), table_name='apicache_characteraffiliation')
    op.drop_table('apicache_characteraffiliation')
    ### end Alembic commands ###