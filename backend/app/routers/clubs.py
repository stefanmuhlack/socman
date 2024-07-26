from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import SessionLocal, engine

router = APIRouter()

models.Base.metadata.create_all(bind=engine)

@router.post("/clubs/", response_model=schemas.Club)
def create_club(club: schemas.ClubCreate, db: Session = Depends(get_db)):
    return crud.create_club(db=db, club=club)

# Add similar routes for Team, Player, League, Tournament, Match
