from typing import List
from . import models
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

# Generate a round-robin schedule for all teams
def generate_round_robin_schedule(teams: List[models.Team], start_date: datetime) -> List[models.Match]:
    schedule = []
    if len(teams) % 2 != 0:  # Add a dummy team if odd number of teams
        teams.append(None)
    
    total_rounds = len(teams) - 1
    half_size = len(teams) // 2
    
    for round_num in range(total_rounds):
        for i in range(half_size):
            team1 = teams[i]
            team2 = teams[len(teams) - i - 1]
            if team1 and team2:
                match_date = start_date + timedelta(days=round_num * 7)
                schedule.append((team1, team2, match_date))  # Home game for team1
                schedule.append((team2, team1, match_date + timedelta(days=3)))  # Home game for team2
        
        # Rotate the teams for the next round
        teams.insert(1, teams.pop())
    
    return schedule

# Generate knockout matches based on the teams
def generate_knockout_schedule(teams: List[models.Team], start_date: datetime) -> List[models.Match]:
    schedule = []
    round_num = 1
    
    while len(teams) > 1:
        next_round_teams = []
        for i in range(0, len(teams), 2):
            team1 = teams[i]
            team2 = teams[i + 1] if i + 1 < len(teams) else None
            if team2:  # Only create a match if there are two teams
                match_date = start_date + timedelta(days=round_num * 7)
                schedule.append((team1, team2, match_date))
                next_round_teams.append(team1)  # Advance winner placeholder, logic for winner would be needed later
        teams = next_round_teams
        round_num += 1
    
    return schedule
