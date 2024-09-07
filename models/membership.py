from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from db.base import Base
from models.common_base import WithoutIDCommonBase

class Membership(Base, WithoutIDCommonBase):
    __tablename__ = "memberships"
    
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    organization_id = Column(Integer, ForeignKey('organizations.id'), primary_key=True)
    role = Column(String(50), nullable=False)
