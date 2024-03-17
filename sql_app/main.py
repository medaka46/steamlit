# from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from typing import List

# from . import crud, schemas
from .database import SessionLocal, engine, Base
from .models import User, Link, Meeting, Project
from .schemas import UserResponse, LinkResponse, MeetingResponse, ProjectResponse, UserCreate, LinkCreate, MeetingCreate, ProjectCreate


# API_URL = "http://127.0.0.1:8000/users"
# API_URL_link = "http://localhost:8000/links/"

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# Database session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# ---------------------------------------------       
# FastAPI CRUD operations

@app.post("/users/", response_model=UserResponse)
async def create_user(data: UserCreate, db: Session = Depends(get_db)):
    # db_user = User(name=data.name, email=data.email)
    db_user = User(name=data.name, mail_add=data.mail_add, pw = data.pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



@app.post("/links/", response_model=LinkResponse)
async def create_link(data: LinkCreate, db: Session = Depends(get_db)):
    db_link = Link(name=data.name, url=data.url, category=data.category, status= data.status, id_user=data.id_user)
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link

@app.post("/meetings/", response_model=MeetingResponse)
async def create_Meeting(data: MeetingCreate, db: Session = Depends(get_db)):
    db_meeting = Meeting(name=data.name, description=data.description, category=data.category, status=data.status, start_datetime=data.start_datetime, end_datetime=data.end_datetime, id_user=data.id_user)
    db.add(db_meeting)
    db.commit()
    db.refresh(db_meeting)
    return db_meeting

@app.post("/projects/", response_model=ProjectResponse)
async def create_Project(data: ProjectCreate, db: Session = Depends(get_db)):
    db_project = Project(name=data.name, country=data.country, client=data.client, type_of_building=data.type_of_building, total_floor_area=data.total_floor_area, m_amount=data.m_amount, currency=data.currency, date_of_submission=data.date_of_submission, id_user=data.id_user)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

# ---------------------------------------------

@app.put("/users/{data_id}", response_model=UserResponse)
async def update_user(data_id: int, data: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == data_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    for var, value in vars(data).items():
        if value: setattr(db_user, var, value)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.put("/links/{data_id}", response_model=LinkResponse)
async def update_link(data_id: int, data: LinkCreate, db: Session = Depends(get_db)):
    db_link = db.query(Link).filter(Link.id == data_id).first()
    if db_link is None:
        raise HTTPException(status_code=404, detail="link not found")
    for var, value in vars(data).items():
        if value: setattr(db_link, var, value)
    db.commit()
    db.refresh(db_link)
    return db_link

@app.put("/meetings/{data_id}", response_model=MeetingResponse)
async def update_meeting(data_id: int, data: MeetingCreate, db: Session = Depends(get_db)):
    db_meeting = db.query(Meeting).filter(Meeting.id == data_id).first()
    if db_meeting is None:
        raise HTTPException(status_code=404, detail="meeting not found")
    for var, value in vars(data).items():
        if value: setattr(db_meeting, var, value)
    db.commit()
    db.refresh(db_meeting)
    return db_meeting

@app.put("/projects/{data_id}", response_model=ProjectResponse)
async def update_project(data_id: int, data: ProjectCreate, db: Session = Depends(get_db)):
    db_project = db.query(Project).filter(Project.id == data_id).first()
    if db_project is None:
        raise HTTPException(status_code=404, detail="project not found")
    for var, value in vars(data).items():
        if value: setattr(db_project, var, value)
    db.commit()
    db.refresh(db_project)
    return db_project

# ----------------------------------------------------------------

@app.get("/users/{data_id}", response_model=UserResponse)
async def read_user(data_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == data_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/links/{data_id}", response_model=LinkResponse)
async def read_link(data_id: int, db: Session = Depends(get_db)):
    db_link = db.query(Link).filter(Link.id == data_id).first()
    if db_link is None:
        raise HTTPException(status_code=404, detail="link not found")
    return db_link

@app.get("/meetings/{data_id}", response_model=MeetingResponse)
async def read_meeting(data_id: int, db: Session = Depends(get_db)):
    db_meeting = db.query(Meeting).filter(Meeting.id == data_id).first()
    if db_meeting is None:
        raise HTTPException(status_code=404, detail="meeting not found")
    return db_meeting

@app.get("/projects/{data_id}", response_model=ProjectResponse)
async def read_project(data_id: int, db: Session = Depends(get_db)):
    db_project = db.query(Project).filter(Project.id == data_id).first()
    if db_project is None:
        raise HTTPException(status_code=404, detail="project not found")
    return db_project

# ----------------------------------------------------------------
@app.get("/users/", response_model=List[UserResponse])
async def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.get("/links/", response_model=List[LinkResponse])
async def read_links(db: Session = Depends(get_db)):
    return db.query(Link).all()

@app.get("/meetings/", response_model=List[MeetingResponse])
async def read_meetings(db: Session = Depends(get_db)):
    return db.query(Meeting).all()

@app.get("/projects/", response_model=List[ProjectResponse])
async def read_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()

# ----------------------------------------------------------------


@app.delete("/users/{data_id}", response_model=UserResponse)
async def delete_user(data_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == data_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return db_user

@app.delete("/links/{data_id}", response_model=LinkResponse)
async def delete_link(data_id: int, db: Session = Depends(get_db)):
    db_link = db.query(Link).filter(Link.id == data_id).first()
    if db_link is None:
        raise HTTPException(status_code=404, detail="Link not found")
    db.delete(db_link)
    db.commit()
    return db_link

@app.delete("/meetings/{data_id}", response_model=MeetingResponse)
async def delete_meeting(data_id: int, db: Session = Depends(get_db)):
    db_meeting = db.query(Meeting).filter(Meeting.id == data_id).first()
    if db_meeting is None:
        raise HTTPException(status_code=404, detail="meeting not found")
    db.delete(db_meeting)
    db.commit()
    return db_meeting

@app.delete("/projects/{data_id}", response_model=ProjectResponse)
async def delete_project(data_id: int, db: Session = Depends(get_db)):
    db_project = db.query(Project).filter(Project.id == data_id).first()
    if db_project is None:
        raise HTTPException(status_code=404, detail="project not found")
    db.delete(db_project)
    db.commit()
    return db_project
# ----------------------------------------------------------------



