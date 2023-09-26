from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Role

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

api_router = APIRouter()
@api_router.get("/")
def index():
    return {"message": "Hello World"}

@api_router.get("/roles")
def get_roles(db: Session = Depends(get_db)):
    db = SessionLocal()
    roles = db.query(Role).all()
    db.close()
    return roles
