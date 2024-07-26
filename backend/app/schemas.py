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

# Define similar schemas for Team, Player, League, Tournament, Match