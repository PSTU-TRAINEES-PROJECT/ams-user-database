from sqlalchemy import Column, String, Integer, ARRAY
from db.base import Base
from models.common_base import WithoutIDCommonBase

class Teacher(Base, WithoutIDCommonBase):
    __tablename__ = "teachers"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    institute_name = Column(String(100), nullable=False)
    department_id = Column(Integer, nullable=False)
    document_id_list = Column(ARRAY(Integer), nullable=False)
