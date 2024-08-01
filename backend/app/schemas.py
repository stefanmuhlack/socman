from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, Dict

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    role: str

    class Config:
        orm_mode = True

class ClubBase(BaseModel):
    name: str

class ClubCreate(ClubBase):
    admin_id: int

class Club(ClubBase):
    id: int

    class Config:
        orm_mode = True

class TeamBase(BaseModel):
    name: str

class TeamCreate(TeamBase):
    club_id: int
    league_id: Optional[int] = None
    tournament_id: Optional[int] = None

class Team(TeamBase):
    id: int

    class Config:
        orm_mode = True

class PlayerBase(BaseModel):
    name: str

class PlayerCreate(PlayerBase):
    primary_team_id: int

class Player(PlayerBase):
    id: int

    class Config:
        orm_mode = True

class LeagueBase(BaseModel):
    name: str

class LeagueCreate(LeagueBase):
    admin_id: int

class League(LeagueBase):
    id: int

    class Config:
        orm_mode = True

class TournamentBase(BaseModel):
    name: str
    type: str

class TournamentCreate(TournamentBase):
    admin_id: int

class Tournament(TournamentBase):
    id: int

    class Config:
        orm_mode = True

class MatchBase(BaseModel):
    team1_id: int
    team2_id: int
    date: datetime
    result: Optional[str] = None

class MatchCreate(MatchBase):
    pass

class Match(MatchBase):
    id: int

    class Config:
        orm_mode = True

class MatchFactBase(BaseModel):
    player_id: int
    kilometers_run: float
    sprints: int
    intensive_runs: int
    distance_run: float
    match_date: datetime

class MatchFactCreate(MatchFactBase):
    pass

class MatchFact(MatchFactBase):
    id: int

    class Config:
        orm_mode = True

class PlayerRatingBase(BaseModel):
    player_id: int
    coach_id: int
    metrics: Dict[str, int]
    rating_date: datetime

class PlayerRatingCreate(PlayerRatingBase):
    pass

class PlayerRating(PlayerRatingBase):
    id: int

    class Config:
        orm_mode = True

class DynamicMetricBase(BaseModel):
    name: str
    description: str

class DynamicMetricCreate(DynamicMetricBase):
    pass

class DynamicMetric(DynamicMetricBase):
    id: int

    class Config:
        orm_mode = True
