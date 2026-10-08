"""rename_content_to_body_in_posts

Revision ID: c7b5b798200c
Revises: 81baff122491
Create Date: 2026-10-06 21:56:19.593281

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c7b5b798200c'
down_revision: Union[str, Sequence[str], None] = '81baff122491'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        'posts',
        'content',
        new_column_name='body'
    )


def downgrade() -> None:
    op.alter_column(
        'posts',
        'body',
        new_column_name='content'
    )
