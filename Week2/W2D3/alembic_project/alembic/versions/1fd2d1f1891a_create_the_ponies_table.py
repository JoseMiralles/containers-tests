"""create the ponies table

Revision ID: 1fd2d1f1891a
Revises: 6a4505dea246
Create Date: 2022-07-03 18:02:59.297006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fd2d1f1891a'
down_revision = '6a4505dea246'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "ponies",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("breed", sa.String(20), nullable=False),
        sa.Column("birth_year", sa.Integer, nullable=False),
        sa.Column(
            "owner_id",
            sa.Integer,
            sa.ForeignKey("owners.id"),
            nullable=False
        )
    )


def downgrade() -> None:
    op.drop_table("ponies")
