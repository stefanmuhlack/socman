from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, models, schemas
from ..database import SessionLocal, engine

router = APIRouter()

models.Base.metadata.create_all(bind=engine)

@router.post("/player-ratings/", response_model=schemas.PlayerRating)
def create_player_rating(player_rating: schemas.PlayerRatingCreate, db: Session = Depends(get_db)):
    return crud.create_player_rating(db=db, player_rating=player_rating)

@router.get("/player-ratings/{player_id}", response_model=List[schemas.PlayerRating])
def read_player_ratings(player_id: int, db: Session = Depends(get_db)):
    return crud.get_player_ratings(db=db, player_id=player_id)
