import uvicorn
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from mangum import Mangum
from app.database import SessionLocal
from app.models import Role

app = FastAPI()
handler = Mangum(app)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/roles")
def get_roles(db: Session = Depends(get_db)):
    db = SessionLocal()
    roles = db.query(Role).all()
    db.close()
    return roles


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
