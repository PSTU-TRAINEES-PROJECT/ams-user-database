# base.py
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


from models.language import Language
from models.user import User
from models.organization import Organization
from models.membership import Membership