from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import SessionLocal, engine
from typing import List

router = APIRouter()

models.Base.metadata.create_all(bind=engine)

@router.post("/players/", response_model=schemas.Player)
def create_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    return crud.create_player(db=db, player=player)

@router.get("/players/", response_model=List[schemas.Player])
def read_players(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    players = crud.get_players(db, skip=skip, limit=limit)
    return players

@router.get("/players/{player_id}", response_model=schemas.Player)
def read_player(player_id: int, db: Session = Depends(get_db)):
    db_player = crud.get_player(db, player_id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player

@router.put("/players/{player_id}", response_model=schemas.Player)
def update_player(player_id: int, player: schemas.PlayerUpdate, db: Session = Depends(get_db)):
    return crud.update_player(db=db, player=player)

@router.delete("/players/{player_id}", response_model=schemas.Player)
def delete_player(player_id: int, db: Session = Depends(get_db)):
    db_player = crud.delete_player(db=db, player_id=player_id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player
