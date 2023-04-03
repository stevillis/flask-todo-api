"""empty message

Revision ID: 3edab8029287
Revises: 6c16c8b8b0f3
Create Date: 2023-04-02 22:27:19.048998

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "3edab8029287"
down_revision = "6c16c8b8b0f3"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column("email", sa.String(length=100), nullable=False),
        sa.Column("password", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user")
    # ### end Alembic commands ###