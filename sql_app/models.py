from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float, Date
from .database import Base 

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    mail_add = Column(String, index=True)
    pw = Column(String, index=True)
    
class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    url = Column(String, unique=True, index=True)
    category = Column(String, index=True)
    status = Column(String, index=True)
    
    id_user = Column(Integer)
    
class Meeting(Base):
    __tablename__ = "meetings"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    category = Column(String, index=True)
    status = Column(String, index=True)
    
    start_datetime = Column(DateTime, nullable=False)
    end_datetime = Column(DateTime, nullable=False)
    
    id_user = Column(Integer)
    
class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    country = Column(String, index=True)
    client = Column(String, index=True)
    type_of_building = Column(String, index=True)
    total_floor_area = Column(Float, index=True)
    m_amount = Column(Float, index=True)
    currency = Column(String)
    date_of_submission = Column(Date)
    
    id_user = Column(Integer)
    
    
    