from sqlalchemy import Column, String, Integer
from db.base import Base
from models.common_base import WithoutIDCommonBase

class Department(Base, WithoutIDCommonBase):
    __tablename__ = "departments"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    platform_type = Column(Integer, nullable=False)
