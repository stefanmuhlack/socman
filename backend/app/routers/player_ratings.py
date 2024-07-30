from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..auth import get_current_user, verify_role
from .. import crud, models, schemas
from ..database import get_db
from typing import List

router = APIRouter()

@router.post("/players/{player_id}/ratings/", response_model=schemas.Rating)
def rate_player(
    player_id: int,
    rating: schemas.RatingCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    if not verify_role(current_user, ["coach"]):
        raise HTTPException(status_code=403, detail="Not authorized to rate players.")
    return crud.rate_player(db=db, player_id=player_id, rating=rating)

@router.get("/players/{player_id}/ratings/", response_model=List[schemas.Rating])
def read_player_ratings(
    player_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.get_player_ratings(db=db, player_id=player_id)
