"""empty message

Revision ID: ab4344121689
Revises: ae9bdeb3e292
Create Date: 2019-09-30 05:29:47.782710

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ab4344121689'
down_revision = 'ae9bdeb3e292'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_apicache_characterinfo_corporation_id', table_name='apicache_characterinfo')
    op.get_bind().execute(sa.sql.table('apicache_characterinfo').delete())
    op.add_column('apicache_characterinfo', sa.Column('alliance_id', sa.Integer(), nullable=True))
    op.alter_column('apicache_characterinfo', 'character_name',
               existing_type=sa.String(length=100),
               nullable=False)
    op.alter_column('apicache_characterinfo', 'corporation_id',
               existing_type=sa.Integer(),
               nullable=False)
    op.alter_column('apicache_characterinfo', 'expire',
               existing_type=sa.DateTime(),
               nullable=False)
    op.alter_column('apicache_characterinfo', 'race_id',
               existing_type=sa.Integer(),
               nullable=False)
    op.create_index(op.f('ix_apicache_characterinfo_character_name'), 'apicache_characterinfo', ['character_name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_apicache_characterinfo_character_name'), table_name='apicache_characterinfo')
    op.alter_column('apicache_characterinfo', 'race_id',
               existing_type=sa.Integer(),
               nullable=True)
    op.alter_column('apicache_characterinfo', 'expire',
               existing_type=sa.DateTime(),
               nullable=True)
    op.alter_column('apicache_characterinfo', 'corporation_id',
               existing_type=sa.Integer(),
               nullable=True)
    op.alter_column('apicache_characterinfo', 'character_name',
               existing_type=sa.String(length=100),
               nullable=True)
    op.drop_column('apicache_characterinfo', 'alliance_id')
    op.create_index('ix_apicache_characterinfo_corporation_id', 'apicache_characterinfo', ['corporation_id'], unique=False)
    # ### end Alembic commands ###
