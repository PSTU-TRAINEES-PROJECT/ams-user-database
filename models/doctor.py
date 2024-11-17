from sqlalchemy import Column, String, Integer, ARRAY
from db.base import Base
from models.common_base import WithoutIDCommonBase

class Doctor(Base, WithoutIDCommonBase):
    __tablename__ = "doctors"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    years_of_experience = Column(Integer, nullable=False)
    current_working_institution = Column(String(100), nullable=False)
    name_of_degree = Column(String(100), nullable=False)
    department_id = Column(Integer, nullable=False)
    document_id_list = Column(ARRAY(Integer), nullable=False)
