from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..dependencies import get_db

router = APIRouter()

# Create a new player
@router.post("/players/", response_model=schemas.Player)
def create_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    return crud.create_player(db=db, player=player)

# Get all players
@router.get("/players/", response_model=List[schemas.Player])
def get_players(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_players(db=db, skip=skip, limit=limit)

# Transfer a player
@router.post("/players/transfer/", response_model=schemas.Transfer)
def transfer_player(transfer: schemas.TransferCreate, db: Session = Depends(get_db)):
    return crud.transfer_player(db=db, transfer=transfer)
