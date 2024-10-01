from fastapi import FastAPI
from .routers import notifications, tactical_formations, players, teams, tournaments, matches

app = FastAPI()

# WebSocket for notifications
app.include_router(notifications.router)

# Additional routers
app.include_router(tactical_formations.router)
app.include_router(players.router)
app.include_router(teams.router)
app.include_router(tournaments.router)
app.include_router(matches.router)
