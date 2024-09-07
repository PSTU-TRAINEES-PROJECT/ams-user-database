from sqlalchemy import Column, String, Integer
from db.base import Base
from models.common_base import WithoutIDCommonBase

class Organization(Base, WithoutIDCommonBase):
    __tablename__ = "organizations"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
