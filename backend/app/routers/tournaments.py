from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter()

# Create a new tournament
@router.post("/tournaments/", response_model=schemas.Tournament)
def create_tournament(tournament: schemas.TournamentCreate, db: Session = Depends(get_db)):
    return crud.create_tournament(db=db, tournament=tournament)

# Get all tournaments
@router.get("/tournaments/", response_model=List[schemas.Tournament])
def get_tournaments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_tournaments(db=db, skip=skip, limit=limit)

@router.get("/tournaments/{tournament_id}/leaderboard", response_model=List[schemas.TournamentLeaderboard])
def get_leaderboard(tournament_id: int, db: Session = Depends(get_db)):
    return crud.get_tournament_leaderboard(db=db, tournament_id=tournament_id)

@router.post("/tournaments/", response_model=schemas.Tournament)
def create_tournament(tournament: schemas.TournamentCreate, db: Session = Depends(get_db)):
    return crud.create_tournament(db=db, tournament=tournament)

@router.post("/matches/", response_model=schemas.Match)
def create_match(match: schemas.MatchCreate, db: Session = Depends(get_db)):
    return crud.create_match(db=db, match=match)

@router.post("/tournaments/promotion-relegation/")
def apply_promotion_relegation(tournament_id: int, db: Session = Depends(get_db)):
    tournament = crud.get_tournament_by_id(db, tournament_id)
    if not tournament:
        raise HTTPException(status_code=404, detail="Tournament not found")
    crud.handle_promotion_relegation(db=db, tournament=tournament)
