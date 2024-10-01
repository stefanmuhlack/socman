from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import schemas, crud

router = APIRouter()

# Get all tournaments
@router.get("/", response_model=List[schemas.Tournament])
def get_tournaments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tournaments = crud.get_tournaments(db, skip=skip, limit=limit)
    return tournaments

# Get a tournament by ID
@router.get("/{tournament_id}", response_model=schemas.Tournament)
def get_tournament(tournament_id: int, db: Session = Depends(get_db)):
    tournament = crud.get_tournament(db, tournament_id=tournament_id)
    if not tournament:
        raise HTTPException(status_code=404, detail="Tournament not found")
    return tournament

# Create a new tournament
@router.post("/", response_model=schemas.Tournament)
def create_tournament(tournament: schemas.TournamentCreate, db: Session = Depends(get_db)):
    return crud.create_tournament(db=db, tournament=tournament)

# Update a tournament
@router.put("/{tournament_id}", response_model=schemas.Tournament)
def update_tournament(tournament_id: int, tournament: schemas.TournamentUpdate, db: Session = Depends(get_db)):
    return crud.update_tournament(db=db, tournament_id=tournament_id, tournament=tournament)

# Delete a tournament
@router.delete("/{tournament_id}")
def delete_tournament(tournament_id: int, db: Session = Depends(get_db)):
    crud.delete_tournament(db=db, tournament_id=tournament_id)
    return {"message": "Tournament deleted"}
