from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import datetime

# Formation Schemas
class TacticalFormationCreate(BaseModel):
    name: str
    comment_german: Optional[str] = None
    comment_english: Optional[str] = None
    players: List[dict]

class TacticalFormationUpdate(TacticalFormationCreate):
    pass

class TacticalFormation(BaseModel):
    id: int
    name: str
    comment_german: Optional[str] = None
    comment_english: Optional[str] = None

    class Config:
        orm_mode = True

# Team Schemas

class TeamBase(BaseModel):
    name: str
    club_id: int

class TeamCreate(TeamBase):
    pass

class TeamUpdate(TeamBase):
    pass

class Team(TeamBase):
    id: int

    class Config:
        orm_mode = True


# Tactical Formations

class TacticalFormationCreate(BaseModel):
    name: str
    comment_german: Optional[str] = None
    comment_english: Optional[str] = None
    players: List[dict]  # List of players with their positions

class TacticalFormationUpdate(BaseModel):
    name: Optional[str]
    comment_german: Optional[str] = None
    comment_english: Optional[str] = None
    players: Optional[List[dict]] = None

class TacticalFormation(BaseModel):
    id: int
    name: str
    comment_german: Optional[str]
    comment_english: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True



# Player Schemas
class PlayerBase(BaseModel):
    name: str
    age: int
    position: str
    team_id: int

class PlayerCreate(PlayerBase):
    pass

class PlayerUpdate(PlayerBase):
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

class PlayerRatingHistoryBase(BaseModel):
    player_id: int
    metrics: Dict[str, int]
    timestamp: datetime

class PlayerRatingHistory(PlayerRatingHistoryBase):
    id: int

    class Config:
        orm_mode = True


# Transfer Schemas
class TransferBase(BaseModel):
    player_id: int
    from_team_id: int
    to_team_id: int
    transfer_date: datetime

class TransferCreate(TransferBase):
    pass

class Transfer(TransferBase):
    id: int

    class Config:
        orm_mode = True

# Tournament Schemas
class TournamentBase(BaseModel):
    name: str
    league_id: int
    start_date: str
    end_date: str

class TournamentCreate(TournamentBase):
    pass

class TournamentUpdate(TournamentBase):
    pass

class Tournament(TournamentBase):
    id: int

    class Config:
        orm_mode = True

class TournamentBase(BaseModel):
    name: str
    type: str
    teams_number: int
    max_starting_players: int = 11
    max_substitutes: int = 5
    substitution_limit: int = 3

class TournamentCreate(TournamentBase):
    admin_id: int

class Tournament(TournamentBase):
    id: int

    class Config:
        orm_mode = True

# Match Schemas
class MatchBase(BaseModel):
    team1_id: int
    team2_id: int
    date: datetime
    result: str
    goals_team1: int
    goals_team2: int
    extra_time: bool
    penalty_shootout: bool

class MatchCreate(MatchBase):
    pass

class Match(MatchBase):
    id: int

    class PlayerBase(BaseModel):
    name: str
    date_of_birth: datetime
    height: Optional[float] = None
    weight: Optional[float] = None
    position: str  # Required field for player position

class PlayerCreate(PlayerBase):
    pass

class Player(PlayerBase):
    id: int

    class Config:
        orm_mode = True


    class Config:
        orm_mode = True
