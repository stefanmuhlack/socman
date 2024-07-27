from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..main import app, get_db
from ..database import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_team():
    response = client.post("/teams/", json={"name": "Test Team", "club_id": 1, "league_id": 1, "tournament_id": 1})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Team"

def test_read_teams():
    response = client.get("/teams/")
    assert response.status_code == 200
    assert len(response.json()) > 0