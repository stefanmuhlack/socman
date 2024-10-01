from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import schemas, crud

router = APIRouter()

# Get all formations
@router.get("/", response_model=List[schemas.TacticalFormation])
def get_formations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    formations = crud.get_formations(db, skip=skip, limit=limit)
    return formations

# Get a formation by ID
@router.get("/{formation_id}", response_model=schemas.TacticalFormation)
def get_formation(formation_id: int, db: Session = Depends(get_db)):
    formation = crud.get_formation(db, formation_id=formation_id)
    if not formation:
        raise HTTPException(status_code=404, detail="Formation not found")
    return formation

# Create a new formation
@router.post("/", response_model=schemas.TacticalFormation)
def create_formation(formation: schemas.TacticalFormationCreate, db: Session = Depends(get_db)):
    return crud.create_formation(db=db, formation=formation)

# Update a formation
@router.put("/{formation_id}", response_model=schemas.TacticalFormation)
def update_formation(formation_id: int, formation: schemas.TacticalFormationUpdate, db: Session = Depends(get_db)):
    return crud.update_formation(db=db, formation_id=formation_id, formation=formation)

# Delete a formation
@router.delete("/{formation_id}")
def delete_formation(formation_id: int, db: Session = Depends(get_db)):
    crud.delete_formation(db=db, formation_id=formation_id)
    return {"message": "Formation deleted"}
