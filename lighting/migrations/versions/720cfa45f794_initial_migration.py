"""Initial migration

Revision ID: 720cfa45f794
Revises: a8891dd7ea2e
Create Date: 2024-06-25 20:45:59.971198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '720cfa45f794'
down_revision = 'a8891dd7ea2e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('light_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('light_id', sa.Integer(), nullable=False),
    sa.Column('image_file', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['light_id'], ['light.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('light', schema=None) as batch_op:
        batch_op.drop_column('image_file')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('light', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_file', sa.VARCHAR(length=20), nullable=False))

    op.drop_table('light_image')
    # ### end Alembic commands ###
