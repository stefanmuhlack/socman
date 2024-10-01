from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.post("/formations/", response_model=schemas.TacticalFormation)
def create_formation(formation: schemas.TacticalFormationCreate, db: Session = Depends(get_db)):
    return crud.create_formation(db, formation)

@router.get("/formations/{formation_id}", response_model=schemas.TacticalFormation)
def read_formation(formation_id: int, db: Session = Depends(get_db)):
    return crud.get_formation(db, formation_id)

@router.put("/formations/{formation_id}", response_model=schemas.TacticalFormation)
def update_formation(formation_id: int, formation: schemas.TacticalFormationUpdate, db: Session = Depends(get_db)):
    return crud.update_formation(db, formation_id, formation)

@router.delete("/formations/{formation_id}")
def delete_formation(formation_id: int, db: Session = Depends(get_db)):
    crud.delete_formation(db, formation_id)
    return {"message": "Formation deleted"}
