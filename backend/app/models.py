from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
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
    __tablename__ = 'player_teams'
    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    team_id = Column(Integer, ForeignKey('teams.id'))
    role = Column(String)  # Primary or secondary team?
    player = relationship("Player", back_populates="player_teams")
    team = relationship("Team", back_populates="player_teams")

class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    club_id = Column(Integer, ForeignKey('clubs.id'))
    league_id = Column(Integer, ForeignKey('leagues.id'))
    tournament_id = Column(Integer, ForeignKey('tournaments.id'))
    club = relationship("Club", back_populates="teams")
    league = relationship("League", back_populates="teams")
    tournament = relationship("Tournament", back_populates="teams")
    player_teams = relationship("PlayerTeam", back_populates="team")

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    date_of_birth = Column(DateTime)  # Date of Birth
    height = Column(Float)  # Height in cm
    weight = Column(Float)  # Weight in kg
    position = Column(String)  # Player position (e.g., Defender, Midfielder, Forward)
    player_teams = relationship("PlayerTeam", back_populates="player")
    rating_history = relationship("PlayerRatingHistory", back_populates="player")

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
    promotion_to = Column(Integer, ForeignKey('tournaments.id'))  # Link to upper league
    relegation_to = Column(Integer, ForeignKey('tournaments.id'))  # Link to lower league
    teams = relationship("Team", back_populates="tournament")


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
    team1_id = Column(Integer, ForeignKey('teams.id'))
    team2_id = Column(Integer, ForeignKey('teams.id'))
    date = Column(DateTime)
    goals_team1 = Column(Integer, default=0)
    goals_team2 = Column(Integer, default=0)
    extra_time = Column(Boolean, default=False)  # Extra time played
    penalty_shootout = Column(Boolean, default=False)  # Penalty shootout if true
    home_away = Column(String)  # "home" or "away"
    result = Column(String)  # Store result as "win", "draw", "loss"
    
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
    metrics = Column(JSON)
    timestamp = Column(DateTime, default=datetime.utcnow)

class DynamicMetric(Base):
    __tablename__ = 'dynamic_metrics'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
