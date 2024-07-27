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
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def create_club(db: Session, club: schemas.ClubCreate):
    db_club = models.Club(name=club.name, admin_id=club.admin_id)
    db.add(db_club)
    db.commit()
    db.refresh(db_club)
    return db_club

def get_clubs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Club).offset(skip).limit(limit).all()

def get_club(db: Session, club_id: int):
    return db.query(models.Club).filter(models.Club.id == club_id).first()

def update_club(db: Session, club: schemas.ClubUpdate):
    db_club = get_club(db, club.id)
    if db_club:
        db_club.name = club.name
        db.commit()
        db.refresh(db_club)
        return db_club
    return None

def delete_club(db: Session, club_id: int):
    db_club = get_club(db, club_id)
    if db_club:
        db.delete(db_club)
        db.commit()
    return db_club

# Add similar CRUD functions for Team, Player, League, Tournament, Match


# Team CRUD operations

def create_team(db: Session, team: schemas.TeamCreate):
    db_team = models.Team(name=team.name, club_id=team.club_id, league_id=team.league_id, tournament_id=team.tournament_id)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

def get_teams(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Team).offset(skip).limit(limit).all()

def get_team(db: Session, team_id: int):
    return db.query(models.Team).filter(models.Team.id == team_id).first()

def update_team(db: Session, team: schemas.TeamUpdate):
    db_team = get_team(db, team.id)
    if db_team:
        db_team.name = team.name
        db_team.club_id = team.club_id
        db_team.league_id = team.league_id
        db_team.tournament_id = team.tournament_id
        db.commit()
        db.refresh(db_team)
        return db_team
    return None

def delete_team(db: Session, team_id: int):
    db_team = get_team(db, team_id)
    if db_team:
        db.delete(db_team)
        db.commit()
    return db_team

# Add similar CRUD functions for Player, League, Tournament, Match
