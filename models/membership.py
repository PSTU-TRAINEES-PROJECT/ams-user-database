from sqlalchemy import Column, Integer, ForeignKey, String
from db.base import Base

class Membership(Base):
    __tablename__ = "memberships"
    
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    organization_id = Column(Integer, ForeignKey('organizations.id'), primary_key=True)
    role = Column(String(50), nullable=False)
