from sqlalchemy.orm import Session
from . import models, schemas
from .auth import get_password_hash

# Custom Metric
def create_custom_metric(db: Session, metric: schemas.CustomMetricCreate):
    db_metric = models.CustomMetric(name=metric.name, description=metric.description, coach_id=metric.coach_id)
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    return db_metric

# Player Transfers
def transfer_player(db: Session, transfer: schemas.TransferCreate):
    db_transfer = models.Transfer(player_id=transfer.player_id, from_team_id=transfer.from_team_id,
                                  to_team_id=transfer.to_team_id, transfer_date=transfer.transfer_date)
    db.add(db_transfer)
    db.commit()
    db.refresh(db_transfer)
    return db_transfer

# Historical player ratings
def get_player_rating_history(db: Session, player_id: int):
    return db.query(models.PlayerRatingHistory).filter(models.PlayerRatingHistory.player_id == player_id).all()

def create_self_assessment(db: Session, player_id: int, metrics: dict):
    db_assessment = models.PlayerSelfAssessment(player_id=player_id, metrics=metrics)
    db.add(db_assessment)
    db.commit()
    db.refresh(db_assessment)
    return db_assessment


# Store a rating history entry whenever a new player rating is submitted
def store_rating_history(db: Session, player_id: int, metrics: dict):
    db_history = models.PlayerRatingHistory(player_id=player_id, metrics=metrics)
    db.add(db_history)
    db.commit()
    db.refresh(db_history)
    return db_history

# Matches
def create_match(db: Session, match: schemas.MatchCreate):
    db_match = models.Match(team1_id=match.team1_id, team2_id=match.team2_id, date=match.date, 
                            result=match.result, goals_team1=match.goals_team1, goals_team2=match.goals_team2,
                            extra_time=match.extra_time, penalty_shootout=match.penalty_shootout)
    db.add(db_match)
    db.commit()
    db.refresh(db_match)
    return db_match

def create_match_statistics(db: Session, match_id: int, player_id: int, stats: dict):
    db_stats = models.MatchStatistics(
        match_id=match_id,
        player_id=player_id,
        goals=stats.get('goals', 0),
        assists=stats.get('assists', 0),
        tackles=stats.get('tackles', 0),
        passes_completed=stats.get('passes_completed', 0),
        fouls_committed=stats.get('fouls_committed', 0),
        minutes_played=stats.get('minutes_played', 0),
        team_id=stats['team_id']
    )
    db.add(db_stats)
    db.commit()
    db.refresh(db_stats)
    return db_stats
