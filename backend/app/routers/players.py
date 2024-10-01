from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.post("/players/", response_model=schemas.Player)
def create_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    return crud.create_player(db, player)

@router.get("/players/{player_id}", response_model=schemas.Player)
def read_player(player_id: int, db: Session = Depends(get_db)):
    return crud.get_player(db, player_id)

@router.put("/players/{player_id}", response_model=schemas.Player)
def update_player(player_id: int, player: schemas.PlayerUpdate, db: Session = Depends(get_db)):
    return crud.update_player(db, player_id, player)

@router.delete("/players/{player_id}")
def delete_player(player_id: int, db: Session = Depends(get_db)):
    crud.delete_player(db, player_id)
    return {"message": "Player deleted"}
