"""empty message

Revision ID: 2960090617c3
Revises: 7159134abe5b
Create Date: 2021-12-16 19:29:06.690174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2960090617c3'
down_revision = '7159134abe5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('emails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mailname', sa.String(length=150), nullable=True),
    sa.Column('mailsurname', sa.String(length=150), nullable=True),
    sa.Column('mailemail', sa.String(length=150), nullable=True),
    sa.Column('mailnumber', sa.String(length=150), nullable=True),
    sa.Column('mailtext', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('facts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('facts',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('fact_number', sa.VARCHAR(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('emails')
    # ### end Alembic commands ###
