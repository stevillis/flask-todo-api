"""empty message

Revision ID: 56e6acbc9bd7
Revises: 1abeb3ff9017
Create Date: 2023-03-29 22:00:39.655187

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "56e6acbc9bd7"
down_revision = "1abeb3ff9017"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("todo", schema=None) as batch_op:
        batch_op.add_column(sa.Column("project_id", sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, "project", ["project_id"], ["id"])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("todo", schema=None) as batch_op:
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.drop_column("project_id")

    # ### end Alembic commands ###
