"""remove age from user setting

Revision ID: 5a0110e162d8
Revises: 2311d35b2828
Create Date: 2014-10-29 19:47:44.413921

"""

# revision identifiers, used by Alembic.
revision = '5a0110e162d8'
down_revision = '2311d35b2828'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'user_settings', 'age')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'user_settings', sa.Column('age', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    ### end Alembic commands ###