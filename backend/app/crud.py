import logging
from sqlalchemy.orm import Session
from . import models, schemas
from .auth import get_password_hash

logger = logging.getLogger(__name__)

# User CRUD operations
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    logger.info(f"Created user {user.username}")
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

# Club CRUD operations
def create_club(db: Session, club: schemas.ClubCreate):
    db_club = models.Club(name=club.name, admin_id=club.admin_id)
    db.add(db_club)
    db.commit()
    db.refresh(db_club)
    logger.info(f"Created club {club.name}")
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
        logger.info(f"Updated club {club.id}")
        return db_club
    logger.warning(f"Club {club.id} not found for update")
    return None

def delete_club(db: Session, club_id: int):
    db_club = get_club(db, club_id)
    if db_club:
        db.delete(db_club)
        db.commit()
        logger.info(f"Deleted club {club_id}")
        return db_club
    logger.warning(f"Club {club_id} not found for deletion")
    return None

# Team CRUD operations
def create_team(db: Session, team: schemas.TeamCreate):
    db_team = models.Team(name=team.name, club_id=team.club_id, league_id=team.league_id, tournament_id=team.tournament_id)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    logger.info(f"Created team {team.name}")
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
        logger.info(f"Updated team {team.id}")
        return db_team
    logger.warning(f"Team {team.id} not found for update")
    return None

def delete_team(db: Session, team_id: int):
    db_team = get_team(db, team_id)
    if db_team:
        db.delete(db_team)
        db.commit()
        logger.info(f"Deleted team {team_id}")
        return db_team
    logger.warning(f"Team {team_id} not found for deletion")
    return None

# Player CRUD operations
def create_player(db: Session, player: schemas.PlayerCreate):
    db_player = models.Player(**player.dict())
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    logger.info(f"Created player {player.name}")
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
        logger.info(f"Updated player {player.id}")
        return db_player
    logger.warning(f"Player {player.id} not found for update")
    return None

def delete_player(db: Session, player_id: int):
    db_player = get_player(db, player_id)
    if db_player:
        db.delete(db_player)
        db.commit()
        logger.info(f"Deleted player {player_id}")
        return db_player
    logger.warning(f"Player {player_id} not found for deletion")
    return None

# League CRUD operations
def create_league(db: Session, league: schemas.LeagueCreate):
    db_league = models.League(**league.dict())
    db.add(db_league)
    db.commit()
    db.refresh(db_league)
    logger.info(f"Created league {league.name}")
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
        logger.info(f"Updated league {league.id}")
        return db_league
    logger.warning(f"League {league.id} not found for update")
    return None

def delete_league(db: Session, league_id: int):
    db_league = get_league(db, league_id)
    if db_league:
        db.delete(db_league)
        db.commit()
        logger.info(f"Deleted league {league_id}")
        return db_league
    logger.warning(f"League {league_id} not found for deletion")
    return None

# Tournament CRUD operations
def create_tournament(db: Session, tournament: schemas.TournamentCreate):
    db_tournament = models.Tournament(**tournament.dict())
    db.add(db_tournament)
    db.commit()
    db.refresh(db_tournament)
    logger.info(f"Created tournament {tournament.name}")
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
        logger.info(f"Updated tournament {tournament.id}")
        return db_tournament
    logger.warning(f"Tournament {tournament.id} not found for update")
    return None

def delete_tournament(db: Session, tournament_id: int):
    db_tournament = get_tournament(db, tournament_id)
    if db_tournament:
        db.delete(db_tournament)
        db.commit()
        logger.info(f"Deleted tournament {tournament_id}")
        return db_tournament
    logger.warning(f"Tournament {tournament_id} not found for deletion")
    return None

# Match CRUD operations
def create_match(db: Session, match: schemas.MatchCreate):
    db_match = models.Match(**match.dict())
    db.add(db_match)
    db.commit()
    db.refresh(db_match)
    logger.info(f"Created match between team {match.team1_id} and team {match.team2_id}")
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
        logger.info(f"Updated match {match.id}")
        return db_match
    logger.warning(f"Match {match.id} not found for update")
    return None

def delete_match(db: Session, match_id: int):
    db_match = get_match(db, match_id)
    if db_match:
        db.delete(db_match)
        db.commit()
        logger.info(f"Deleted match {match_id}")
        return db_match
    logger.warning(f"Match {match_id} not found for deletion")
    return None

# Dynamic Metric CRUD operations
def create_dynamic_metric(db: Session, metric: schemas.DynamicMetricCreate):
    db_metric = models.DynamicMetric(**metric.dict())
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    logger.info(f"Created dynamic metric {metric.name}")
    return db_metric

def get_dynamic_metrics(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.DynamicMetric).offset(skip).limit(limit).all()

def get_dynamic_metric(db: Session, metric_id: int):
    return db.query(models.DynamicMetric).filter(models.DynamicMetric.id == metric_id).first()

def update_dynamic_metric(db: Session, metric: schemas.DynamicMetricUpdate):
    db_metric = get_dynamic_metric(db, metric.id)
    if db_metric:
        for var, value in vars(metric).items():
            setattr(db_metric, var, value) if value else None
        db.commit()
        db.refresh(db_metric)
        logger.info(f"Updated dynamic metric {metric.id}")
        return db_metric
    logger.warning(f"Dynamic metric {metric.id} not found for update")
    return None

def delete_dynamic_metric(db: Session, metric_id: int):
    db_metric = get_dynamic_metric(db, metric_id)
    if db_metric:
        db.delete(db_metric)
        db.commit()
        logger.info(f"Deleted dynamic metric {metric_id}")
        return db_metric
    logger.warning(f"Dynamic metric {metric_id} not found for deletion")
    return None
