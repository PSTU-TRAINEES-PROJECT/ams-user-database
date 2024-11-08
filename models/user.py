from db.base import Base
from models.common_base import CommonBase
from sqlalchemy import Column, Enum, ForeignKey, Integer, String, Boolean
from utils.enums import Status


class User(Base, CommonBase):
    __tablename__ = "users"

    email = Column(String(100), index=True)
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    password_hash = Column(String(255))
    mobile = Column(String(20), nullable=True)
    email_verified = Column(Boolean, default=False, nullable=False)
    status = Column(Enum(Status), nullable=False, default=Status.INACTIVE.value, server_default=Status.INACTIVE.value)
    profile_image = Column(String(255), nullable=True)
    tag = Column(String(50), nullable=True)


    # Adding the language_code foreign key
    language_code = Column(String(10), ForeignKey('languages.code'), nullable=True)