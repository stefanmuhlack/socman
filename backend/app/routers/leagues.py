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

@router.post("/leagues/", response_model=schemas.League)
def create_league(league: schemas.LeagueCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_admin_or_higher)):
    return crud.create_league(db=db, league=league)

@router.get("/leagues/", response_model=List[schemas.League])
def read_leagues(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    leagues = crud.get_leagues(db, skip=skip, limit=limit)
    return leagues

@router.get("/leagues/{league_id}", response_model=schemas.League)
def read_league(league_id: int, db: Session = Depends(get_db)):
    db_league = crud.get_league(db, league_id)
    if db_league is None:
        raise HTTPException(status_code=404, detail="League not found")
    return db_league

@router.put("/leagues/{league_id}", response_model=schemas.League)
def update_league(league_id: int, league: schemas.LeagueUpdate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_admin_or_higher)):
    return crud.update_league(db=db, league=league)

@router.delete("/leagues/{league_id}", response_model=schemas.League)
def delete_league(league_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_admin_or_higher)):
    db_league = crud.delete_league(db=db, league_id=league_id)
    if db_league is None:
        raise HTTPException(status_code=404, detail="League not found")
    return db_league
