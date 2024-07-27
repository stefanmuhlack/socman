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

# Player CRUD operations

def create_player(db: Session, player: schemas.PlayerCreate):
    db_player = models.Player(**player.dict())
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def get_players(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Player).offset(skip).limit(limit).all()

def get_player(db: Session, player_id: int):
    return db.query(models.Player).filter(models.Player.id == player_id).first()

def update_player(db: Session, player: schemas.PlayerUpdate):
    db_player = get_player(db, player.id)
    if db_player:
        for var, value in vars(player).items():
            setattr(db_player, var, value) if value else None
        db.commit()
        db.refresh(db_player)
        return db_player
    return None

def delete_player(db: Session, player_id: int):
    db_player = get_player(db, player_id)
    if db_player:
        db.delete(db_player)
        db.commit()
    return db_player

# League CRUD operations

def create_league(db: Session, league: schemas.LeagueCreate):
    db_league = models.League(**league.dict())
    db.add(db_league)
    db.commit()
    db.refresh(db_league)
    return db_league

def get_leagues(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.League).offset(skip).limit(limit).all()

def get_league(db: Session, league_id: int):
    return db.query(models.League).filter(models.League.id == league_id).first()

def update_league(db: Session, league: schemas.LeagueUpdate):
    db_league = get_league(db, league.id)
    if db_league:
        for var, value in vars(league).items():
            setattr(db_league, var, value) if value else None
        db.commit()
        db.refresh(db_league)
        return db_league
    return None

def delete_league(db: Session, league_id: int):
    db_league = get_league(db, league_id)
    if db_league:
        db.delete(db_league)
        db.commit()
    return db_league

# Tournament CRUD operations

def create_tournament(db: Session, tournament: schemas.TournamentCreate):
    db_tournament = models.Tournament(**tournament.dict())
    db.add(db_tournament)
    db.commit()
    db.refresh(db_tournament)
    return db_tournament

def get_tournaments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Tournament).offset(skip).limit(limit).all()

def get_tournament(db: Session, tournament_id: int):
    return db.query(models.Tournament).filter(models.Tournament.id == tournament_id).first()

def update_tournament(db: Session, tournament: schemas.TournamentUpdate):
    db_tournament = get_tournament(db, tournament.id)
    if db_tournament:
        for var, value in vars(tournament).items():
            setattr(db_tournament, var, value) if value else None
        db.commit()
        db.refresh(db_tournament)
        return db_tournament
    return None

def delete_tournament(db: Session, tournament_id: int):
    db_tournament = get_tournament(db, tournament_id)
    if db_tournament:
        db.delete(db_tournament)
        db.commit()
    return db_tournament

# Match CRUD operations

def create_match(db: Session, match: schemas.MatchCreate):
    db_match = models.Match(**match.dict())
    db.add(db_match)
    db.commit()
    db.refresh(db_match)
    return db_match

def get_matches(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Match).offset(skip).limit(limit).all()

def get_match(db: Session, match_id: int):
    return db.query(models.Match).filter(models.Match.id == match_id).first()

def update_match(db: Session, match: schemas.MatchUpdate):
    db_match = get_match(db, match.id)
    if db_match:
        for var, value in vars(match).items():
            setattr(db_match, var, value) if value else None
        db.commit()
        db.refresh(db_match)
        return db_match
    return None

def delete_match(db: Session, match_id: int):
    db_match = get_match(db, match_id)
    if db_match:
        db.delete(db_match)
        db.commit()
    return db_match



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
