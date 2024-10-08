"""empty message

Revision ID: 09d949268a01
Revises: 963f0f1597ac
Create Date: 2024-05-31 12:34:41.279816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09d949268a01'
down_revision = '963f0f1597ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('begin_at', sa.Date(), nullable=False),
    sa.Column('end_at', sa.Date(), nullable=False),
    sa.Column('max_users', sa.Integer(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('event')
    # ### end Alembic commands ###
