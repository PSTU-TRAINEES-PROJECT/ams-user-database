from sqlalchemy import Column, String, Integer
from db.base import Base
from models.common_base import WithoutIDCommonBase

class UserDocument(Base, WithoutIDCommonBase):
    __tablename__ = "user_documents"
    
    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String(200), unique=True, nullable=False)
    # object_key = Column(String(100), nullable=False)
    # owner_type = Column(Integer, nullable=False)
