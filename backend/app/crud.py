from sqlalchemy.orm import Session
from . import models, schemas
from .auth import get_password_hash

# Player Transfers
def transfer_player(db: Session, transfer: schemas.TransferCreate):
    db_transfer = models.Transfer(player_id=transfer.player_id, from_team_id=transfer.from_team_id,
                                  to_team_id=transfer.to_team_id, transfer_date=transfer.transfer_date)
    db.add(db_transfer)
    db.commit()
    db.refresh(db_transfer)
    return db_transfer

# Matches
def create_match(db: Session, match: schemas.MatchCreate):
    db_match = models.Match(team1_id=match.team1_id, team2_id=match.team2_id, date=match.date, 
                            result=match.result, goals_team1=match.goals_team1, goals_team2=match.goals_team2,
                            extra_time=match.extra_time, penalty_shootout=match.penalty_shootout)
    db.add(db_match)
    db.commit()
    db.refresh(db_match)
    return db_match
