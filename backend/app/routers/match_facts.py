from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, models, schemas
from ..database import SessionLocal, engine

router = APIRouter()

models.Base.metadata.create_all(bind=engine)

@router.post("/match-facts/", response_model=schemas.MatchFact)
def create_match_fact(match_fact: schemas.MatchFactCreate, db: Session = Depends(get_db)):
    return crud.create_match_fact(db=db, match_fact=match_fact)

@router.get("/match-facts/", response_model=List[schemas.MatchFact])
def read_match_facts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_match_facts(db=db, skip=skip, limit=limit)

@router.get("/match-facts/{match_fact_id}", response_model=schemas.MatchFact)
def read_match_fact(match_fact_id: int, db: Session = Depends(get_db)):
    db_match_fact = crud.get_match_fact(db=db, match_fact_id=match_fact_id)
    if db_match_fact is None:
        raise HTTPException(status_code=404, detail="MatchFact not found")
    return db_match_fact

@router.put("/match-facts/{match_fact_id}", response_model=schemas.MatchFact)
def update_match_fact(match_fact_id: int, match_fact: schemas.MatchFactUpdate, db: Session = Depends(get_db)):
    return crud.update_match_fact(db=db, match_fact=match_fact)

@router.delete("/match-facts/{match_fact_id}", response_model=schemas.MatchFact)
def delete_match_fact(match_fact_id: int, db: Session = Depends(get_db)):
    db_match_fact = crud.delete_match_fact(db=db, match_fact_id=match_fact_id)
    if db_match_fact is None:
        raise HTTPException(status_code=404, detail="MatchFact not found")
    return db_match_fact
