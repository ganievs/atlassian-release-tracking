"""Init

Revision ID: 8871f15b5061
Revises: 
Create Date: 2022-10-07 17:59:10.127227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a31859d6950'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'Application',
        sa.Column('name', sa.String(), nullable=False, unique=True),
        sa.PrimaryKeyConstraint('name'),
        sa.Column('version', sa.String(), default="0.0.0", nullable=False)
    )

def downgrade() -> None:
    op.drop_table('Application')
