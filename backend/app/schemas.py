from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import datetime

# User Schemas
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    role: str

    class Config:
        orm_mode = True

# Club Schemas
class ClubBase(BaseModel):
    name: str

class ClubCreate(ClubBase):
    admin_id: int

class Club(ClubBase):
    id: int

    class Config:
        orm_mode = True

# Team Schemas
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

# Player Schemas
class PlayerBase(BaseModel):
    name: str

class PlayerCreate(PlayerBase):
    pass

class Player(PlayerBase):
    id: int

    class Config:
        orm_mode = True

class PlayerTeamBase(BaseModel):
    player_id: int
    team_id: int
    role: str

class PlayerTeam(PlayerTeamBase):
    id: int

    class Config:
        orm_mode = True

# Tournament Schemas
class TournamentBase(BaseModel):
    name: str
    type: str
    group_stage: bool
    knockout_stage: bool

class TournamentCreate(TournamentBase):
    admin_id: int

class Tournament(TournamentBase):
    id: int

    class Config:
        orm_mode = True

# Player Rating Schemas
class PlayerRatingBase(BaseModel):
    player_id: int
    coach_id: int
    metrics: Dict[str, int]  # Dynamic metrics stored as a dictionary
    rating_date: datetime

class PlayerRatingCreate(PlayerRatingBase):
    pass

class PlayerRating(PlayerRatingBase):
    id: int

    class Config:
        orm_mode = True
