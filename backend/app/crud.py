from sqlalchemy.orm import Session
from . import models, schemas
from .auth import get_password_hash

# User CRUD operations

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Add similar CRUD functions for Club, Team, Player, League, Tournament, Match
