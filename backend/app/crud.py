from sqlalchemy.orm import Session
from . import models, schemas
from .auth import get_password_hash

# User CRUD operations
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

# Club CRUD operations
def create_club(db: Session, club: schemas.ClubCreate):
    db_club = models.Club(name=club.name, admin_id=club.admin_id)
    db.add(db_club)
    db.commit()
    db.refresh(db_club)
    return db_club

def get_clubs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Club).offset(skip).limit(limit).all()

# Player CRUD operations
def create_player(db: Session, player: schemas.PlayerCreate):
    db_player = models.Player(name=player.name)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def transfer_player(db: Session, transfer: schemas.TransferCreate):
    db_transfer = models.Transfer(player_id=transfer.player_id, from_team_id=transfer.from_team_id,
                                  to_team_id=transfer.to_team_id, transfer_date=transfer.transfer_date)
    db.add(db_transfer)
    db.commit()
    db.refresh(db_transfer)
    return db_transfer

# Tournament CRUD operations
def create_tournament(db: Session, tournament: schemas.TournamentCreate):
    db_tournament = models.Tournament(name=tournament.name, type=tournament.type,
                                      group_stage=tournament.group_stage, knockout_stage=tournament.knockout_stage,
                                      admin_id=tournament.admin_id)
    db.add(db_tournament)
    db.commit()
    db.refresh(db_tournament)
    return db_tournament

def get_tournaments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Tournament).offset(skip).limit(limit).all()

# Match CRUD operations
def create_match(db: Session, match: schemas.MatchCreate):
    db_match = models.Match(team1_id=match.team1_id, team2_id=match.team2_id, date=match.date,
                            result=match.result, goals_team1=match.goals_team1, goals_team2=match.goals_team2,
                            extra_time=match.extra_time, penalty_shootout=match.penalty_shootout)
    db.add(db_match)
    db.commit()
    db.refresh(db_match)
    return db_match

def update_match_result(db: Session, match_id: int, result: schemas.MatchResultUpdate):
    db_match = db.query(models.Match).filter(models.Match.id == match_id).first()
    if db_match:
        db_match.result = result.result
        db_match.goals_team1 = result.goals_team1
        db_match.goals_team2 = result.goals_team2
        db_match.extra_time = result.extra_time
        db_match.penalty_shootout = result.penalty_shootout
        db.commit()
        db.refresh(db_match)
    return db_match
