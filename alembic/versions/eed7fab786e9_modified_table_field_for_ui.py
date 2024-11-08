"""modified table field for ui

Revision ID: eed7fab786e9
Revises: 61998390a94b
Create Date: 2024-11-04 09:42:13.965796

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eed7fab786e9'
down_revision: Union[str, None] = '61998390a94b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('businesses', sa.Column('user_id', sa.Integer(), nullable=False))
    op.add_column('businesses', sa.Column('years_of_experience', sa.Integer(), nullable=False))
    op.add_column('businesses', sa.Column('current_working_institution', sa.String(length=100), nullable=False))
    op.add_column('businesses', sa.Column('name_of_degree', sa.String(length=100), nullable=False))
    op.drop_column('businesses', 'industry_type')
    op.drop_column('businesses', 'name')
    op.drop_column('businesses', 'business_address')
    op.add_column('doctors', sa.Column('user_id', sa.Integer(), nullable=False))
    op.add_column('doctors', sa.Column('years_of_experience', sa.Integer(), nullable=False))
    op.add_column('doctors', sa.Column('current_working_institution', sa.String(length=100), nullable=False))
    op.add_column('doctors', sa.Column('name_of_degree', sa.String(length=100), nullable=False))
    op.drop_column('doctors', 'college_name')
    op.drop_column('doctors', 'name')
    op.drop_column('doctors', 'degree_name')
    op.add_column('engineers', sa.Column('user_id', sa.Integer(), nullable=False))
    op.add_column('engineers', sa.Column('years_of_experience', sa.Integer(), nullable=False))
    op.add_column('engineers', sa.Column('current_working_institution', sa.String(length=100), nullable=False))
    op.add_column('engineers', sa.Column('name_of_degree', sa.String(length=100), nullable=False))
    op.drop_column('engineers', 'college_name')
    op.drop_column('engineers', 'name')
    op.drop_column('engineers', 'degree_name')
    op.add_column('lawyers', sa.Column('user_id', sa.Integer(), nullable=False))
    op.add_column('lawyers', sa.Column('years_of_experience', sa.Integer(), nullable=False))
    op.add_column('lawyers', sa.Column('current_working_institution', sa.String(length=100), nullable=False))
    op.add_column('lawyers', sa.Column('name_of_degree', sa.String(length=100), nullable=False))
    op.drop_column('lawyers', 'specialization')
    op.drop_column('lawyers', 'law_firm_id')
    op.drop_column('lawyers', 'name')
    op.add_column('public_figures', sa.Column('user_id', sa.Integer(), nullable=False))
    op.add_column('public_figures', sa.Column('years_of_experience', sa.Integer(), nullable=False))
    op.add_column('public_figures', sa.Column('current_working_institution', sa.String(length=100), nullable=False))
    op.add_column('public_figures', sa.Column('name_of_degree', sa.String(length=100), nullable=False))
    op.drop_column('public_figures', 'biography')
    op.drop_column('public_figures', 'name')
    op.add_column('teachers', sa.Column('user_id', sa.Integer(), nullable=False))
    op.add_column('teachers', sa.Column('years_of_experience', sa.Integer(), nullable=False))
    op.add_column('teachers', sa.Column('current_working_institution', sa.String(length=100), nullable=False))
    op.add_column('teachers', sa.Column('name_of_degree', sa.String(length=100), nullable=False))
    op.drop_column('teachers', 'institute_name')
    op.drop_column('teachers', 'name')
    op.add_column('user_documents', sa.Column('file_name', sa.String(length=200), nullable=False))
    op.drop_constraint('user_documents_name_key', 'user_documents', type_='unique')
    op.create_unique_constraint(None, 'user_documents', ['file_name'])
    op.drop_column('user_documents', 'owner_type')
    op.drop_column('user_documents', 'name')
    op.drop_column('user_documents', 'object_key')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_documents', sa.Column('object_key', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.add_column('user_documents', sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.add_column('user_documents', sa.Column('owner_type', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'user_documents', type_='unique')
    op.create_unique_constraint('user_documents_name_key', 'user_documents', ['name'])
    op.drop_column('user_documents', 'file_name')
    op.add_column('teachers', sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.add_column('teachers', sa.Column('institute_name', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.drop_column('teachers', 'name_of_degree')
    op.drop_column('teachers', 'current_working_institution')
    op.drop_column('teachers', 'years_of_experience')
    op.drop_column('teachers', 'user_id')
    op.add_column('public_figures', sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.add_column('public_figures', sa.Column('biography', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.drop_column('public_figures', 'name_of_degree')
    op.drop_column('public_figures', 'current_working_institution')
    op.drop_column('public_figures', 'years_of_experience')
    op.drop_column('public_figures', 'user_id')
    op.add_column('lawyers', sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.add_column('lawyers', sa.Column('law_firm_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('lawyers', sa.Column('specialization', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.drop_column('lawyers', 'name_of_degree')
    op.drop_column('lawyers', 'current_working_institution')
    op.drop_column('lawyers', 'years_of_experience')
    op.drop_column('lawyers', 'user_id')
    op.add_column('engineers', sa.Column('degree_name', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.add_column('engineers', sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.add_column('engineers', sa.Column('college_name', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.drop_column('engineers', 'name_of_degree')
    op.drop_column('engineers', 'current_working_institution')
    op.drop_column('engineers', 'years_of_experience')
    op.drop_column('engineers', 'user_id')
    op.add_column('doctors', sa.Column('degree_name', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.add_column('doctors', sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.add_column('doctors', sa.Column('college_name', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.drop_column('doctors', 'name_of_degree')
    op.drop_column('doctors', 'current_working_institution')
    op.drop_column('doctors', 'years_of_experience')
    op.drop_column('doctors', 'user_id')
    op.add_column('businesses', sa.Column('business_address', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.add_column('businesses', sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.add_column('businesses', sa.Column('industry_type', sa.VARCHAR(length=100), autoincrement=False, nullable=False))
    op.drop_column('businesses', 'name_of_degree')
    op.drop_column('businesses', 'current_working_institution')
    op.drop_column('businesses', 'years_of_experience')
    op.drop_column('businesses', 'user_id')
    # ### end Alembic commands ###
