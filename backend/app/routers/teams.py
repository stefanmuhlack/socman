from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.post("/teams/", response_model=schemas.Team)
def create_team(team: schemas.TeamCreate, db: Session = Depends(get_db)):
    return crud.create_team(db, team)

@router.get("/teams/{team_id}", response_model=schemas.Team)
def read_team(team_id: int, db: Session = Depends(get_db)):
    return crud.get_team(db, team_id)

@router.put("/teams/{team_id}", response_model=schemas.Team)
def update_team(team_id: int, team: schemas.TeamUpdate, db: Session = Depends(get_db)):
    return crud.update_team(db, team_id, team)

@router.delete("/teams/{team_id}")
def delete_team(team_id: int, db: Session = Depends(get_db)):
    crud.delete_team(db, team_id)
    return {"message": "Team deleted"}
