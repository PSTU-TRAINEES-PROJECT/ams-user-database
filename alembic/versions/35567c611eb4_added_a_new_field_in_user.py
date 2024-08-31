"""added a new field in user

Revision ID: 35567c611eb4
Revises: a04115158079
Create Date: 2024-08-31 16:04:32.787907

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '35567c611eb4'
down_revision: Union[str, None] = 'a04115158079'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email_verified', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'email_verified')
    # ### end Alembic commands ###
