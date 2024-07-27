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
# MatchFact CRUD operations

def create_match_fact(db: Session, match_fact: schemas.MatchFactCreate):
    db_match_fact = models.MatchFact(**match_fact.dict())
    db.add(db_match_fact)
    db.commit()
    db.refresh(db_match_fact)
    return db_match_fact

def get_match_facts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.MatchFact).offset(skip).limit(limit).all()

def get_match_fact(db: Session, match_fact_id: int):
    return db.query(models.MatchFact).filter(models.MatchFact.id == match_fact_id).first()

# PlayerRating CRUD operations

def create_player_rating(db: Session, player_rating: schemas.PlayerRatingCreate):
    db_player_rating = models.PlayerRating(**player_rating.dict())
    db.add(db_player_rating)
    db.commit()
    db.refresh(db_player_rating)
    return db_player_rating

def get_player_ratings(db: Session, player_id: int):
    return db.query(models.PlayerRating).filter(models.PlayerRating.player_id == player_id).all()


# Add similar CRUD functions for Player, League, Tournament, Match


# Player Rating CRUD operations

def rate_player(db: Session, player_id: int, rating: schemas.RatingCreate):
    db_rating = models.Rating(
        player_id=player_id, 
        metric=rating.metric, 
        value=rating.value
    )
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating

def get_player_ratings(db: Session, player_id: int):
    return db.query(models.Rating).filter(models.Rating.player_id == player_id).all()

# Additional CRUD functions for managing metrics

def create_metric(db: Session, metric: schemas.MetricCreate):
    db_metric = models.Metric(
        name=metric.name,
        description=metric.description,
        classification=metric.classification
    )
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    return db_metric

def get_metrics(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Metric).offset(skip).limit(limit).all()

def get_metric(db: Session, metric_id: int):
    return db.query(models.Metric).filter(models.Metric.id == metric_id).first()

def update_metric(db: Session, metric: schemas.MetricUpdate):
    db_metric = get_metric(db, metric.id)
    if db_metric:
        db_metric.name = metric.name
        db_metric.description = metric.description
        db_metric.classification = metric.classification
        db.commit()
        db.refresh(db_metric)
        return db_metric
    return None

def delete_metric(db: Session, metric_id: int):
    db_metric = get_metric(db, metric_id)
    if db_metric:
        db.delete(db_metric)
        db.commit()
    return db_metric
