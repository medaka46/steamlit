import datetime
from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    name: str
    mail_add: str
    pw: str

class UserResponse(BaseModel):
    id: int
    name: str
    mail_add: str
    pw: str
# ---------------------------------------------------
# class Link(Base):
#     __tablename__ = "links"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     url = Column(String, unique=True, index=True)
    
class LinkCreate(BaseModel):
    name: str
    url: str
    category: str
    status: str
    
    id_user: int
    
    # mail_add: str
    

class LinkResponse(BaseModel):
    id: int
    name: str
    url: str
    category: str
    status: str
    
    id_user: int
    
    # mail_add: str

# ---------------------------------------------------
# class Meeting(Base):
#     __tablename__ = "meetings"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     email = Column(String, unique=True, index=True)
    
class MeetingCreate(BaseModel):
    name: str
    description: str
    category: str
    status: str
    
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime
    
    id_user: int

class MeetingResponse(BaseModel):
    id: int
    name: str
    description: str
    category: str
    status: str
    
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime
    
    id_user: int
# ----------------------
    
class ProjectCreate(BaseModel):
    name: str
    country: str
    client: str
    type_of_building: str
    total_floor_area: float
    m_amount: float
    currency: str
    date_of_submission: datetime.date
    
    id_user: int
    

class ProjectResponse(BaseModel):
    id: int
    name: str
    country: str
    client: str
    type_of_building: str
    total_floor_area: float
    m_amount: float
    currency: str
    date_of_submission: datetime.date
  
    id_user: int
    
    
    
    
    
    

# Create the database tables
# Base.metadata.create_all(bind=engine)

# Database session dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()