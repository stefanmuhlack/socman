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
def create_player(db: Session, player: schemas.PlayerCreate):
    db_player = models.Player(name=player.name, date_of_birth=player.date_of_birth, 
                              height=player.height, weight=player.weight, position=player.position)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player


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
    db_formation = models.TacticalFormation(name=formation.name, user_id=user_id)
    db.add(db_formation)
    db.commit()
    db.refresh(db_formation)
    
    # Add players to the formation
    for player in formation.players:
        player_position = models.TacticalPlayerPosition(
            player_id=player.player_id,
            formation_id=db_formation.id,
            position=player.position
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
    
    if formation_update.players:
        # Clear current players
        db.query(models.TacticalPlayerPosition).filter_by(formation_id=formation_id).delete()
        
        # Re-add players
        for player in formation_update.players:
            player_position = models.TacticalPlayerPosition(
                player_id=player.player_id,
                formation_id=formation.id,
                position=player.position
            )
            db.add(player_position)
    db.commit()
    return formation




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

def create_tournament(db: Session, tournament: schemas.TournamentCreate):
    db_tournament = models.Tournament(
        name=tournament.name,
        type=tournament.type,
        teams_number=tournament.teams_number,
        home_away=tournament.home_away,
        best_teams_promoted=tournament.best_teams_promoted,
        worst_teams_relegated=tournament.worst_teams_relegated,
        third_place_playoff=tournament.third_place_playoff,
        penalty_shootout=tournament.penalty_shootout,
        promotion_to=tournament.promotion_to,
        relegation_to=tournament.relegation_to,
    )
    db.add(db_tournament)
    db.commit()
    db.refresh(db_tournament)
    return db_tournament


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

def create_team(db: Session, team: schemas.TeamCreate):
    db_team = models.Team(
        name=team.name,
        club_id=team.club_id,
        tactical_formation=team.tactical_formation,
        home_jersey_main_color=team.home_jersey_main_color,
        home_jersey_secondary_color=team.home_jersey_secondary_color,
        home_jersey_number_color=team.home_jersey_number_color,
        away_jersey_main_color=team.away_jersey_main_color,
        away_jersey_secondary_color=team.away_jersey_secondary_color,
        away_jersey_number_color=team.away_jersey_number_color,
    )
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team
