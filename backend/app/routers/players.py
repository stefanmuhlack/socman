from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import schemas, crud

router = APIRouter()

# Get all players
@router.get("/", response_model=List[schemas.Player])
def get_players(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    players = crud.get_players(db, skip=skip, limit=limit)
    return players

# Get a player by ID
@router.get("/{player_id}", response_model=schemas.Player)
def get_player(player_id: int, db: Session = Depends(get_db)):
    player = crud.get_player(db, player_id=player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player

# Create a new player
@router.post("/", response_model=schemas.Player)
def create_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    return crud.create_player(db=db, player=player)

# Update a player
@router.put("/{player_id}", response_model=schemas.Player)
def update_player(player_id: int, player: schemas.PlayerUpdate, db: Session = Depends(get_db)):
    return crud.update_player(db=db, player_id=player_id, player=player)

# Delete a player
@router.delete("/{player_id}")
def delete_player(player_id: int, db: Session = Depends(get_db)):
    crud.delete_player(db=db, player_id=player_id)
    return {"message": "Player deleted"}
