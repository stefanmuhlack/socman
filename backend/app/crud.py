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

def get_club(db: Session, club_id: int):
    return db.query(models.Club).filter(models.Club.id == club_id).first()

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

# Player CRUD operations
def create_player(db: Session, player: schemas.PlayerCreate):
    db_player = models.Player(name=player.name)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def get_players(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Player).offset(skip).limit(limit).all()

def get_player(db: Session, player_id: int):
    return db.query(models.Player).filter(models.Player.id == player_id).first()

def add_player_to_team(db: Session, player_id: int, team_id: int, role: str):
    db_player_team = models.PlayerTeam(player_id=player_id, team_id=team_id, role=role)
    db.add(db_player_team)
    db.commit()
    db.refresh(db_player_team)
    return db_player_team

def get_player_teams(db: Session, player_id: int):
    return db.query(models.PlayerTeam).filter(models.PlayerTeam.player_id == player_id).all()

# Tournament CRUD operations
def create_tournament(db: Session, tournament: schemas.TournamentCreate):
    db_tournament = models.Tournament(name=tournament.name, type=tournament.type, group_stage=tournament.group_stage, knockout_stage=tournament.knockout_stage, admin_id=tournament.admin_id)
    db.add(db_tournament)
    db.commit()
    db.refresh(db_tournament)
    return db_tournament

def get_tournaments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Tournament).offset(skip).limit(limit).all()

def get_tournament(db: Session, tournament_id: int):
    return db.query(models.Tournament).filter(models.Tournament.id == tournament_id).first()

# Player Rating CRUD operations
def rate_player(db: Session, rating: schemas.PlayerRatingCreate):
    db_rating = models.PlayerRating(player_id=rating.player_id, coach_id=rating.coach_id, metrics=rating.metrics, rating_date=rating.rating_date)
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating

def get_player_ratings(db: Session, player_id: int):
    return db.query(models.PlayerRating).filter(models.PlayerRating.player_id == player_id).all()
