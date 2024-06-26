"""Initial migration

Revision ID: a8891dd7ea2e
Revises: 
Create Date: 2024-06-25 20:10:23.829166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8891dd7ea2e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wishlist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('light_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['light_id'], ['light.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('_alembic_tmp_light')
    with op.batch_alter_table('light', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_file', sa.String(length=20), nullable=False))
        batch_op.alter_column('color',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=20),
               existing_nullable=False)
        batch_op.alter_column('location_type',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=50),
               existing_nullable=False)
        batch_op.drop_column('image_files')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('user_type',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=10),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('user_type',
               existing_type=sa.String(length=10),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)

    with op.batch_alter_table('light', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_files', sa.TEXT(), nullable=False))
        batch_op.alter_column('location_type',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.alter_column('color',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.drop_column('image_file')

    op.create_table('_alembic_tmp_light',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('category', sa.VARCHAR(length=100), nullable=False),
    sa.Column('color', sa.VARCHAR(length=100), nullable=False),
    sa.Column('price', sa.FLOAT(), nullable=False),
    sa.Column('min_order_quantity', sa.INTEGER(), nullable=False),
    sa.Column('location_type', sa.VARCHAR(length=100), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('image_files', sa.TEXT(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('wishlist')
    # ### end Alembic commands ###