"""First Version

Revision ID: 14faaf096d0d
Revises: 
Create Date: 2022-06-10 00:00:30.223220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14faaf096d0d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('thumbnail_url', sa.String(), nullable=True),
    sa.Column('local_id', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('publish_date', sa.DateTime(), nullable=True),
    sa.Column('tags', sa.JSON(), nullable=True),
    sa.Column('source', sa.String(), nullable=True),
    sa.Column('created_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('news_shares',
    sa.Column('news_id', sa.Integer(), nullable=False),
    sa.Column('channel', sa.String(), nullable=False),
    sa.Column('created_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['news_id'], ['news.id'], ),
    sa.PrimaryKeyConstraint('news_id', 'channel')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('news_shares')
    op.drop_table('news')
    # ### end Alembic commands ###
