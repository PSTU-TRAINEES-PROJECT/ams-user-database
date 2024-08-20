# user.py
from db.base import Base
from models.common_base import CommonBase
from sqlalchemy import Column, ForeignKey, Integer, String


class User(Base, CommonBase):
    __tablename__ = "users"

    username = Column(String(30), unique=True)
    email = Column(String(100), index=True)
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    password_hash = Column(String(255))
    mobile = Column(String(20), nullable=True)

    # Adding the language_code foreign key
    language_code = Column(String(10), ForeignKey('languages.code'), nullable=True)