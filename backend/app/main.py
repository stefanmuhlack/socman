from fastapi.security import OAuth2PasswordRequestForm
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, auth
from .database import SessionLocal, engine

# Import routers for different modules
from .routers import notifications, formations, players, teams, tournaments

# Create all models in the database (if not created)
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Include WebSocket for notifications
app.include_router(notifications.router)

# Include router for tactical formations
app.include_router(formations.router, prefix="/formations", tags=["Formations"])

# Include router for players
app.include_router(players.router, prefix="/players", tags=["Players"])

# Include router for teams
app.include_router(teams.router, prefix="/teams", tags=["Teams"])

# Include router for tournaments
app.include_router(tournaments.router, prefix="/tournaments", tags=["Tournaments"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root endpoint (health check)
@app.get("/")
async def read_root():
    return {"message": "SocMan API is running"}

# Authentication route for login
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
