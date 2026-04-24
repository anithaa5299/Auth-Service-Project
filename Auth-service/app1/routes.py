from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import User
from .auth import hash_password, verify_password, create_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(email: str, password: str, db: Session = Depends(get_db)):
    user = User(
        email=email,
        hashed_password=hash_password(password)
    )
    db.add(user)
    db.commit()
    return {"msg": "user created"}


@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()

    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"user_id": user.id})
    return {"access_token": token}