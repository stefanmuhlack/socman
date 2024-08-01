from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, JSON
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String)  # Add role field for role-based access

class Club(Base):
    __tablename__ = 'clubs'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    admin_id = Column(Integer, ForeignKey('users.id'))
    admin = relationship("User", back_populates="clubs")

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

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    primary_team_id = Column(Integer, ForeignKey('teams.id'))
    primary_team = relationship("Team", back_populates="players")

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
    type = Column(String)
    admin_id = Column(Integer, ForeignKey('users.id'))
    admin = relationship("User", back_populates="tournaments")
    teams = relationship("Team", back_populates="tournament")

class Match(Base):
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True, index=True)
    team1_id = Column(Integer, ForeignKey('teams.id'))
    team2_id = Column(Integer, ForeignKey('teams.id'))
    date = Column(DateTime)
    result = Column(String)
    team1 = relationship("Team", foreign_keys=[team1_id])
    team2 = relationship("Team", foreign_keys=[team2_id])

class MatchFact(Base):
    __tablename__ = 'match_facts'
    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    kilometers_run = Column(Float)
    sprints = Column(Integer)
    intensive_runs = Column(Integer)
    distance_run = Column(Float)
    match_date = Column(DateTime)
    player = relationship("Player", back_populates="match_facts")

class PlayerRating(Base):
    __tablename__ = 'player_ratings'
    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    coach_id = Column(Integer, ForeignKey('users.id'))
    metrics = Column(JSON)  # Use JSON to store dynamic metrics
    rating_date = Column(DateTime)
    player = relationship("Player", back_populates="ratings")
    coach = relationship("User", back_populates="ratings")

class DynamicMetric(Base):
    __tablename__ = 'dynamic_metrics'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
