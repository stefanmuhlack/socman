from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import SessionLocal, engine
from ..auth import get_current_admin_or_higher, get_current_user

router = APIRouter()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/clubs/", response_model=schemas.Club)
def create_club(club: schemas.ClubCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_admin_or_higher)):
    return crud.create_club(db=db, club=club)

@router.get("/clubs/", response_model=list[schemas.Club])
def read_clubs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_clubs(db, skip=skip, limit=limit)

@router.get("/clubs/{club_id}", response_model=schemas.Club)
def read_club(club_id: int, db: Session = Depends(get_db)):
    db_club = crud.get_club(db, club_id)
    if db_club is None:
        raise HTTPException(status_code=404, detail="Club not found")
    return db_club

@router.put("/clubs/{club_id}", response_model=schemas.Club)
def update_club(club_id: int, club: schemas.ClubUpdate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_admin_or_higher)):
    return crud.update_club(db=db, club=club)

@router.delete("/clubs/{club_id}", response_model=schemas.Club)
def delete_club(club_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_admin_or_higher)):
    db_club = crud.delete_club(db=db, club_id=club_id)
    if db_club is None:
        raise HTTPException(status_code=404, detail="Club not found")
    return db_club
