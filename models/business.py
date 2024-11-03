from sqlalchemy import ARRAY, Column, String, Integer
from db.base import Base
from models.common_base import WithoutIDCommonBase

class Business(Base, WithoutIDCommonBase):
    __tablename__ = "businesses"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    industry_type = Column(String(100), nullable=False)
    business_address = Column(String(100), nullable=False)
    department_id = Column(Integer, nullable=False)
    document_id_list = Column(ARRAY(Integer), nullable=False)
