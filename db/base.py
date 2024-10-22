# base.py
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


from models.language import Language
from models.user import User
from models.organization import Organization
from models.membership import Membership
from models.department import Department
from models.user_document import UserDocument
from models.doctor import Doctor
from models.teacher import Teacher
from models.public_figure import PublicFigure
from models.engineer import Engineer
from models.lawyer import Lawyer
from models.business import Business

