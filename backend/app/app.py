from fastapi import FastAPI
from .routers import notifications

app = FastAPI()

# WebSocket for notifications
app.include_router(notifications.router)

# Other routes
