from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import schemas, crud

router = APIRouter()

# Get all teams
@router.get("/", response_model=List[schemas.Team])
def get_teams(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    teams = crud.get_teams(db, skip=skip, limit=limit)
    return teams

# Get a team by ID
@router.get("/{team_id}", response_model=schemas.Team)
def get_team(team_id: int, db: Session = Depends(get_db)):
    team = crud.get_team(db, team_id=team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

# Create a new team
@router.post("/", response_model=schemas.Team)
def create_team(team: schemas.TeamCreate, db: Session = Depends(get_db)):
    return crud.create_team(db=db, team=team)

# Update a team
@router.put("/{team_id}", response_model=schemas.Team)
def update_team(team_id: int, team: schemas.TeamUpdate, db: Session = Depends(get_db)):
    return crud.update_team(db=db, team_id=team_id, team=team)

# Delete a team
@router.delete("/{team_id}")
def delete_team(team_id: int, db: Session = Depends(get_db)):
    crud.delete_team(db=db, team_id=team_id)
    return {"message": "Team deleted"}
