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

# Data Export API
@router.get("/players/export", response_class=FileResponse)
def export_player_data(db: Session = Depends(get_db)):
    players = crud.get_all_players(db)
    csv_data = "id,name,date_of_birth,height,weight,position\n"
    for player in players:
        csv_data += f"{player.id},{player.name},{player.date_of_birth},{player.height},{player.weight},{player.position}\n"
    with open("players.csv", "w") as file:
        file.write(csv_data)
    return FileResponse("players.csv")
