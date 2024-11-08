"""added tag field in user table

Revision ID: c948de332c77
Revises: b098f3ca4a6f
Create Date: 2024-11-08 21:20:46.266270

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c948de332c77'
down_revision: Union[str, None] = 'b098f3ca4a6f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('tag', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'tag')
    # ### end Alembic commands ###
