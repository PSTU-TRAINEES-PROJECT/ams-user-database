from sqlalchemy import Column, String, Integer, ARRAY
from db.base import Base
from models.common_base import WithoutIDCommonBase

class Doctor(Base, WithoutIDCommonBase):
    __tablename__ = "doctors"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    department_id = Column(Integer, nullable=False)
    college_name = Column(String(100), nullable=False)
    degree_name = Column(String(100), nullable=False)
    document_id_list = Column(ARRAY(Integer), nullable=False)
