from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, models
from ..dependencies import get_db

router = APIRouter()

# Create a new team
@router.post("/teams/", response_model=schemas.Team)
def create_team(team: schemas.TeamCreate, db: Session = Depends(get_db)):
    return crud.create_team(db=db, team=team)

# Get all teams
@router.get("/teams/", response_model=List[schemas.Team])
def get_teams(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_teams(db=db, skip=skip, limit=limit)

# Get a single team by ID
@router.get("/teams/{team_id}", response_model=schemas.Team)
def get_team(team_id: int, db: Session = Depends(get_db)):
    db_team = crud.get_team(db=db, team_id=team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return db_team
