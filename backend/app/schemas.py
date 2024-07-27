from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

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
    ball_manipulation: int
    kicking_ability: int
    passing_ability: int
    duel_tackling: int
    field_coverage: int
    blocking_ability: int
    game_strategy: int
    playmaking_risk: int
    rating_date: datetime

class PlayerRatingCreate(PlayerRatingBase):
    pass

class PlayerRating(PlayerRatingBase):
    id: int

    class Config:
        orm_mode = True

# Define similar schemas for Team, Player, League, Tournament, Match
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
    ball_manipulation: int
    kicking_ability: int
    passing_ability: int
    duel_tackling: int
    field_coverage: int
    blocking_ability: int
    game_strategy: int
    playmaking_risk: int
    rating_date: datetime

class PlayerRatingCreate(PlayerRatingBase):
    pass

class PlayerRating(PlayerRatingBase):
    id: int

    class Config:
        orm_mode = True

