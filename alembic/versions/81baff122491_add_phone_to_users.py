"""add_phone_to_users

Revision ID: 81baff122491
Revises: 0075b33e3da1
Create Date: 2026-10-06 21:52:40.392223

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '81baff122491'
down_revision: Union[str, Sequence[str], None] = '0075b33e3da1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'users',
        sa.Column('phone', sa.String(20), nullable=True)
    )

    op.create_index(
        'ix_users_phone',
        'users',
        ['phone'],
        unique=False
    )


def downgrade() -> None:
    op.drop_index('ix_users_phone', table_name='users')
    op.drop_column('users', 'phone')
