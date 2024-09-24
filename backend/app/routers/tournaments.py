from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..dependencies import get_db

router = APIRouter()

# Create a new tournament
@router.post("/tournaments/", response_model=schemas.Tournament)
def create_tournament(tournament: schemas.TournamentCreate, db: Session = Depends(get_db)):
    return crud.create_tournament(db=db, tournament=tournament)

# Get all tournaments
@router.get("/tournaments/", response_model=List[schemas.Tournament])
def get_tournaments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_tournaments(db=db, skip=skip, limit=limit)
