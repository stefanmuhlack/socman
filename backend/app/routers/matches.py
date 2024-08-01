from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import SessionLocal, engine
from ..auth import get_current_admin_or_higher
from typing import List

router = APIRouter()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/matches/", response_model=schemas.Match)
def create_match(match: schemas.MatchCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_admin_or_higher)):
    return crud.create_match(db=db, match=match)

@router.get("/matches/", response_model=List[schemas.Match])
def read_matches(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    matches = crud.get_matches(db, skip=skip, limit=limit)
    return matches

@router.get("/matches/{match_id}", response_model=schemas.Match)
def read_match(match_id: int, db: Session = Depends(get_db)):
    db_match = crud.get_match(db, match_id)
    if db_match is None:
        raise HTTPException(status_code=404, detail="Match not found")
    return db_match

@router.put("/matches/{match_id}", response_model=schemas.Match)
def update_match(match_id: int, match: schemas.MatchUpdate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_admin_or_higher)):
    return crud.update_match(db=db, match=match)

@router.delete("/matches/{match_id}", response_model=schemas.Match)
def delete_match(match_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_admin_or_higher)):
    db_match = crud.delete_match(db=db, match_id=match_id)
    if db_match is None:
        raise HTTPException(status_code=404, detail="Match not found")
    return db_match
