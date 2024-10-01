from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Boolean, JSON
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String)  # Role-based access (super-admin, admin, coach, player)

class CustomMetric(Base):
    __tablename__ = 'custom_metrics'
    id = Column(Integer, primary_key=True, index=True)
    coach_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String, index=True)
    description = Column(String)
    coach = relationship("User", back_populates="custom_metrics")

class Club(Base):
    __tablename__ = 'clubs'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    admin_id = Column(Integer, ForeignKey('users.id'))
    admin = relationship("User", back_populates="clubs")

class PlayerTeam(Base):
    __tablename__ = 'player_team'
    player_id = Column(Integer, ForeignKey('players.id'), primary_key=True)
    team_id = Column(Integer, ForeignKey('teams.id'), primary_key=True)
    player = relationship("Player", back_populates="teams")
    team = relationship("Team", back_populates="players")
    start_position = Column(String, nullable=True)  # Player's position for the match
    
class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    club_id = Column(Integer, ForeignKey('clubs.id'))
    players = relationship("PlayerTeam", back_populates="team")
    tactical_formation = Column(String)  # Tactical formation (e.g., 4-4-2, 4-3-3, etc.)
    
    # Home jersey details
    home_jersey_main_color = Column(String)
    home_jersey_secondary_color = Column(String)
    home_jersey_number_color = Column(String)
    
    # Away jersey details
    away_jersey_main_color = Column(String)
    away_jersey_secondary_color = Column(String)
    away_jersey_number_color = Column(String)

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    date_of_birth = Column(DateTime, nullable=False)
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    position = Column(String, nullable=False)  # Detailed position like TW, LV, DMZ
    jersey_number = Column(Integer, nullable=False)
    is_captain = Column(Boolean, default=False)
    start_lineup = Column(Boolean, default=False)  # Whether the player is in the starting 11
    teams = relationship("PlayerTeam", back_populates="player")

class PlayerSelfAssessment(Base):
    __tablename__ = 'player_self_assessments'
    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    metrics = Column(JSON)  # Player's self-assessment metrics
    assessment_date = Column(DateTime, default=datetime.utcnow)


class Transfer(Base):
    __tablename__ = 'transfers'
    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    from_team_id = Column(Integer, ForeignKey('teams.id'))
    to_team_id = Column(Integer, ForeignKey('teams.id'))
    transfer_date = Column(DateTime)
    player = relationship("Player", back_populates="transfers")
    from_team = relationship("Team", foreign_keys=[from_team_id])
    to_team = relationship("Team", foreign_keys=[to_team_id])

class League(Base):
    __tablename__ = 'leagues'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    admin_id = Column(Integer, ForeignKey('users.id'))
    admin = relationship("User", back_populates="leagues")
    teams = relationship("Team", back_populates="league")

class Tournament(Base):
    __tablename__ = 'tournaments'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)  # 'liga' or 'knockout'
    teams_number = Column(Integer)  # Number of teams in the tournament
    home_away = Column(Boolean, default=False)  # True for home/away matches
    best_teams_promoted = Column(Integer, default=2)  # Number of teams promoted
    worst_teams_relegated = Column(Integer, default=2)  # Number of teams relegated
    third_place_playoff = Column(Boolean, default=False)  # If true, playoff for third place
    penalty_shootout = Column(Boolean, default=False)  # Enable penalty shootouts if necessary
    max_starting_players = Column(Integer, default=11)  # Max players to start a match
    max_substitutes = Column(Integer, default=5)  # Max substitutes allowed in a match
    substitution_limit = Column(Integer, default=3)  # Number of substitution windows


class TournamentLeaderboard(Base):
    __tablename__ = 'tournament_leaderboards'
    id = Column(Integer, primary_key=True, index=True)
    tournament_id = Column(Integer, ForeignKey('tournaments.id'))
    team_id = Column(Integer, ForeignKey('teams.id'))
    points = Column(Integer, default=0)
    matches_played = Column(Integer, default=0)
    wins = Column(Integer, default=0)
    losses = Column(Integer, default=0)
    draws = Column(Integer, default=0)


class Match(Base):
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True, index=True)
    home_team_id = Column(Integer, ForeignKey('teams.id'))
    away_team_id = Column(Integer, ForeignKey('teams.id'))
    match_date = Column(DateTime, default=datetime.utcnow)
    home_team = relationship("Team", foreign_keys=[home_team_id])
    away_team = relationship("Team", foreign_keys=[away_team_id])
    home_score = Column(Integer, default=0)
    away_score = Column(Integer, default=0)
    tactical_formation_home = Column(String)  # Tactical formation of the home team
    tactical_formation_away = Column(String)  # Tactical formation of the away team
    
class MatchStatistics(Base):
    __tablename__ = 'match_statistics'
    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer, ForeignKey('matches.id'))
    player_id = Column(Integer, ForeignKey('players.id'))
    goals = Column(Integer, default=0)
    assists = Column(Integer, default=0)
    tackles = Column(Integer, default=0)
    passes_completed = Column(Integer, default=0)
    fouls_committed = Column(Integer, default=0)
    minutes_played = Column(Integer, default=0)
    team_id = Column(Integer, ForeignKey('teams.id'))

class PlayerRating(Base):
    __tablename__ = 'player_ratings'
    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    coach_id = Column(Integer, ForeignKey('users.id'))
    metrics = Column(JSON)  # Store metrics as JSON
    rating_date = Column(DateTime)

class PlayerRatingHistory(Base):
    __tablename__ = 'player_rating_history'
    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    metrics = Column(JSON)  # Store rating metrics
    timestamp = Column(DateTime, default=datetime.utcnow)

class DynamicMetric(Base):
    __tablename__ = 'dynamic_metrics'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

class TacticalFormation(Base):
    __tablename__ = 'tactical_formations'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)  # Name of the tactical formation (e.g., 4-4-2, 4-3-3)
    user_id = Column(Integer, ForeignKey('users.id'))  # Link to the user creating the formation
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Players assigned to this formation
    players = relationship("TacticalPlayerPosition", back_populates="formation")
    
    # Optional: Reference to opponent formation for comparisons
    opponent_formation_id = Column(Integer, ForeignKey('tactical_formations.id'))

class TacticalPlayerPosition(Base):
    __tablename__ = 'tactical_player_positions'
    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    formation_id = Column(Integer, ForeignKey('tactical_formations.id'))
    
    # Player's position in this specific tactical formation (e.g., STZ, LV, DMZ)
    position = Column(String, nullable=False)
    
    formation = relationship("TacticalFormation", back_populates="players")
    player = relationship("Player", back_populates="positions")

class JerseyColor(Base):
    __tablename__ = 'jersey_colors'
    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey('teams.id'))
    main_color = Column(String)  # Main jersey color
    secondary_color = Column(String)  # Secondary color
    number_color = Column(String)  # Color of the jersey number
    is_home = Column(Boolean, default=True)  # Home or Away Jersey
    
    team = relationship("Team", back_populates="jersey_colors")
