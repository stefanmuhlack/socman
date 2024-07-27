from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Club(Base):
    __tablename__ = 'clubs'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    admin_id = Column(Integer, ForeignKey('users.id'))

class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    club_id = Column(Integer, ForeignKey('clubs.id'))
    league_id = Column(Integer, ForeignKey('leagues.id'))
    tournament_id = Column(Integer, ForeignKey('tournaments.id'))

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    team_id = Column(Integer, ForeignKey('teams.id'))
    primary_team_id = Column(Integer, ForeignKey('teams.id'))

class League(Base):
    __tablename__ = 'leagues'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    admin_id = Column(Integer, ForeignKey('users.id'))

class Tournament(Base):
    __tablename__ = 'tournaments'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)
    admin_id = Column(Integer, ForeignKey('users.id'))

class Match(Base):
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True, index=True)
    team1_id = Column(Integer, ForeignKey('teams.id'))
    team2_id = Column(Integer, ForeignKey('teams.id'))
    date = Column(DateTime)
    result = Column(String)


class MatchFact(Base):
    __tablename__ = 'match_facts'
    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    kilometers_run = Column(Float)
    sprints = Column(Integer)
    intensive_runs = Column(Integer)
    distance_run = Column(Float)
    match_date = Column(DateTime)

class PlayerRating(Base):
    __tablename__ = 'player_ratings'
    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    coach_id = Column(Integer, ForeignKey('users.id'))
    ball_manipulation = Column(Integer)
    kicking_ability = Column(Integer)
    passing_ability = Column(Integer)
    duel_tackling = Column(Integer)
    field_coverage = Column(Integer)
    blocking_ability = Column(Integer)
    game_strategy = Column(Integer)
    playmaking_risk = Column(Integer)
    rating_date = Column(DateTime)
