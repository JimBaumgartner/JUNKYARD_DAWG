"""empty message

Revision ID: c4472e978f1e
Revises: 
Create Date: 2019-12-11 12:55:24.663716

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4472e978f1e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('parts_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('part', sa.String(length=100), nullable=False),
    sa.Column('make', sa.String(length=100), nullable=False),
    sa.Column('model', sa.String(length=100), nullable=False),
    sa.Column('trim_package', sa.String(length=100), nullable=True),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('target_make', sa.String(length=100), nullable=False),
    sa.Column('target_model', sa.String(length=100), nullable=False),
    sa.Column('target_trim_package', sa.String(length=100), nullable=True),
    sa.Column('target_year', sa.Integer(), nullable=True),
    sa.Column('notes', sa.String(length=500), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_model')
    op.drop_table('parts_model')
    # ### end Alembic commands ###
