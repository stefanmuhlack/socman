from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException
from .auth import get_password_hash

# Custom Metric
def create_custom_metric(db: Session, metric: schemas.CustomMetricCreate):
    db_metric = models.CustomMetric(name=metric.name, description=metric.description, coach_id=metric.coach_id)
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    return db_metric

# Create Player
def get_players(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Player).offset(skip).limit(limit).all()

def get_player(db: Session, player_id: int):
    return db.query(models.Player).filter(models.Player.id == player_id).first()

def create_player(db: Session, player: schemas.PlayerCreate):
    db_player = models.Player(**player.dict())
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def update_player(db: Session, player_id: int, player: schemas.PlayerUpdate):
    db_player = db.query(models.Player).filter(models.Player.id == player_id).first()
    if not db_player:
        return None
    for var, value in vars(player).items():
        setattr(db_player, var, value) if value else None
    db.commit()
    db.refresh(db_player)
    return db_player

def delete_player(db: Session, player_id: int):
    db_player = db.query(models.Player).filter(models.Player.id == player_id).first()
    db.delete(db_player)
    db.commit()



# Player Export
def get_all_players(db: Session):
    return db.query(models.Player).all()

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
    
def get_tournament_leaderboard(db: Session, tournament_id: int, page: int, page_size: int):
    offset = (page - 1) * page_size
    leaderboard = db.query(models.Team).filter_by(tournament_id=tournament_id).order_by(models.Team.points.desc()).offset(offset).limit(page_size).all()
    return leaderboard



# Store a rating history entry whenever a new player rating is submitted
def store_rating_history(db: Session, player_id: int, metrics: dict):
    db_history = models.PlayerRatingHistory(player_id=player_id, metrics=metrics)
    db.add(db_history)
    db.commit()
    db.refresh(db_history)
    return db_history
    
# Matches
def create_match(db: Session, match: schemas.MatchCreate):
    existing_match = db.query(models.Match).filter(
        models.Match.team1_id == match.team1_id,
        models.Match.team2_id == match.team2_id,
        models.Match.date == match.date
    ).first()
    
    if existing_match:
        raise HTTPException(status_code=400, detail="Match already scheduled on this date")

    db_match = models.Match(
        team1_id=match.team1_id,
        team2_id=match.team2_id,
        date=match.date,
        home_away=match.home_away,
        extra_time=match.extra_time,
        penalty_shootout=match.penalty_shootout,
    )
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

# Tactical Formations LineUps
def create_tactical_formation(db: Session, formation: schemas.TacticalFormationCreate, user_id: int):
    db_formation = models.TacticalFormation(
        name=formation.name,
        user_id=user_id,
        comment_german=formation.comment_german,
        comment_english=formation.comment_english
    )
    db.add(db_formation)
    db.commit()
    db.refresh(db_formation)
    
    # Add players to the formation
    for player in formation.players:
        player_position = models.TacticalPlayerPosition(
            player_id=player['player_id'],
            formation_id=db_formation.id,
            position=player['position']
        )
        db.add(player_position)
    db.commit()
    
    return db_formation

def get_formation_by_id(db: Session, formation_id: int):
    return db.query(models.TacticalFormation).filter(models.TacticalFormation.id == formation_id).first()

def get_all_formations(db: Session, user_id: int):
    return db.query(models.TacticalFormation).filter(models.TacticalFormation.user_id == user_id).all()

def update_tactical_formation(db: Session, formation_id: int, formation_update: schemas.TacticalFormationUpdate):
    formation = db.query(models.TacticalFormation).filter(models.TacticalFormation.id == formation_id).first()
    
    if formation_update.name:
        formation.name = formation_update.name
    
    if formation_update.comment_german:
        formation.comment_german = formation_update.comment_german
        
    if formation_update.comment_english:
        formation.comment_english = formation_update.comment_english

    if formation_update.players:
        # Clear current players
        db.query(models.TacticalPlayerPosition).filter_by(formation_id=formation_id).delete()
        
        # Re-add players
        for player in formation_update.players:https://github.com/stefanmuhlack/socman/blob/development/backend/app/crud.py
            player_position = models.TacticalPlayerPosition(
                player_id=player['player_id'],
                formation_id=formation.id,
                position=player['position']
            )
            db.add(player_position)
    db.commit()
    return formation
    
# Formations
def get_formations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.TacticalFormation).offset(skip).limit(limit).all()

def get_formation(db: Session, formation_id: int):
    return db.query(models.TacticalFormation).filter(models.TacticalFormation.id == formation_id).first()

    def create_formation(db: Session, formation: schemas.TacticalFormationCreate):
    db_formation = models.TacticalFormation(**formation.dict())
    db.add(db_formation)
    db.commit()
    db.refresh(db_formation)
    return db_formation

def update_formation(db: Session, formation_id: int, formation: schemas.TacticalFormationUpdate):
    db_formation = db.query(models.TacticalFormation).filter(models.TacticalFormation.id == formation_id).first()
    if not db_formation:
        return None
    for var, value in vars(formation).items():
        setattr(db_formation, var, value) if value else None
    db.commit()
    db.refresh(db_formation)
    return db_formation

def delete_formation(db: Session, formation_id: int):
    db_formation = db.query(models.TacticalFormation).filter(models.TacticalFormation.id == formation_id).first()
    db.delete(db_formation)
    db.commit()


# Tournament Leaderboard
def update_leaderboard(db: Session, tournament_id: int, team_id: int, result: str):
    leaderboard = db.query(models.TournamentLeaderboard).filter_by(
        tournament_id=tournament_id, team_id=team_id
    ).first()

    if not leaderboard:
        leaderboard = models.TournamentLeaderboard(
            tournament_id=tournament_id,
            team_id=team_id
        )
        db.add(leaderboard)

    if result == "win":
        leaderboard.wins += 1
        leaderboard.points += 3
    elif result == "loss":
        leaderboard.losses += 1
    elif result == "draw":
        leaderboard.draws += 1
        leaderboard.points += 1

    leaderboard.matches_played += 1
    db.commit()
    db.refresh(leaderboard)
    return leaderboard

# Tournaments

def get_tournaments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Tournament).offset(skip).limit(limit).all()

def get_tournament(db: Session, tournament_id: int):
    return db.query(models.Tournament).filter(models.Tournament.id == tournament_id).first()

def create_tournament(db: Session, tournament: schemas.TournamentCreate):
    db_tournament = models.Tournament(**tournament.dict())
    db.add(db_tournament)
    db.commit()
    db.refresh(db_tournament)
    return db_tournament

def update_tournament(db: Session, tournament_id: int, tournament: schemas.TournamentUpdate):
    db_tournament = db.query(models.Tournament).filter(models.Tournament.id == tournament_id).first()
    if not db_tournament:
        return None
    for var, value in vars(tournament).items():
        setattr(db_tournament, var, value) if value else None
    db.commit()
    db.refresh(db_tournament)
    return db_tournament

def delete_tournament(db: Session, tournament_id: int):
    db_tournament = db.query(models.Tournament).filter(models.Tournament.id == tournament_id).first()
    db.delete(db_tournament)
    db.commit()


def handle_promotion_relegation(db: Session, tournament: models.Tournament):
    teams = sorted(tournament.teams, key=lambda t: t.points, reverse=True)
    
    # Promote the best teams
    if tournament.promotion_to:
        for i in range(tournament.best_teams_promoted):
            promote_team(db, teams[i], tournament.promotion_to)
    
    # Relegate the worst teams
    if tournament.relegation_to:
        for i in range(tournament.worst_teams_relegated):
            relegate_team(db, teams[-(i+1)], tournament.relegation_to)
    
    # Handle third-place playoff
    if tournament.third_place_playoff:
        handle_third_place_playoff(db, teams)

def promote_team(db: Session, team: models.Team, promotion_tournament: models.Tournament):
    team.tournament_id = promotion_tournament.id
    db.commit()

def relegate_team(db: Session, team: models.Team, relegation_tournament: models.Tournament):
    team.tournament_id = relegation_tournament.id
    db.commit()

def get_teams(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Team).offset(skip).limit(limit).all()

def get_team(db: Session, team_id: int):
    return db.query(models.Team).filter(models.Team.id == team_id).first()

def create_team(db: Session, team: schemas.TeamCreate):
    db_team = models.Team(**team.dict())
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

def update_team(db: Session, team_id: int, team: schemas.TeamUpdate):
    db_team = db.query(models.Team).filter(models.Team.id == team_id).first()
    if not db_team:
        return None
    for var, value in vars(team).items():
        setattr(db_team, var, value) if value else None
    db.commit()
    db.refresh(db_team)
    return db_team

def delete_team(db: Session, team_id: int):
    db_team = db.query(models.Team).filter(models.Team.id == team_id).first()
    db.delete(db_team)
    db.commit()

