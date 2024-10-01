from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.post("/tournaments/", response_model=schemas.Tournament)
def create_tournament(tournament: schemas.TournamentCreate, db: Session = Depends(get_db)):
    return crud.create_tournament(db, tournament)

@router.get("/tournaments/{tournament_id}", response_model=schemas.Tournament)
def read_tournament(tournament_id: int, db: Session = Depends(get_db)):
    return crud.get_tournament(db, tournament_id)

@router.put("/tournaments/{tournament_id}", response_model=schemas.Tournament)
def update_tournament(tournament_id: int, tournament: schemas.TournamentUpdate, db: Session = Depends(get_db)):
    return crud.update_tournament(db, tournament_id, tournament)

@router.delete("/tournaments/{tournament_id}")
def delete_tournament(tournament_id: int, db: Session = Depends(get_db)):
    crud.delete_tournament(db, tournament_id)
    return {"message": "Tournament deleted"}
