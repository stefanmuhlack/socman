from fastapi import FastAPI
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from . import crud, models, schemas, auth
from .database import SessionLocal, engine
from .routers import notifications

app = FastAPI()

# WebSocket for notifications
app.include_router(notifications.router)

# Other routes
