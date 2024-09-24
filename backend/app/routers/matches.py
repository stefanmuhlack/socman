from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..dependencies import get_db

router = APIRouter()

# Create a new match
@router.post("/matches/", response_model=schemas.Match)
def create_match(match: schemas.MatchCreate, db: Session = Depends(get_db)):
    return crud.create_match(db=db, match=match)

# Update a match result
@router.put("/matches/{match_id}", response_model=schemas.Match)
def update_match_result(match_id: int, result: schemas.MatchResultUpdate, db: Session = Depends(get_db)):
    return crud.update_match_result(db=db, match_id=match_id, result=result)

# Get all matches
@router.get("/matches/", response_model=List[schemas.Match])
def get_matches(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_matches(db=db, skip=skip, limit=limit)
