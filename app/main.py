from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware

from app.schemas.user import UserInfo
from app.schemas.scoreboard import Scoreboard, AddRecord, GameScoreboard, AddGamesPlayed

from app.services.user import UserService
from app.services.scoreboard import ScoreboardService

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_get_with_params(userId: int, nickname: str):
    return {"userId": userId, "nickname": nickname}

@app.get("/")
def read_get():
    return {"message": "GET handler working"}

@app.post("/")
def read_post():
    return {"message": "POST handler working"}

@app.get('/get_data/{userId}')
async def get_games_played(user_id: int, scoreboard_service: ScoreboardService = Depends()):
    return await scoreboard_service.get_games_played(user_id)

@app.get('/get_data', response_model=UserInfo)
async def get_info(user_service: UserService = Depends()):
    return await user_service.get_data()

@app.get('/scoreboard/{game_id}', response_model=GameScoreboard)
async def get_scoreboard_by_id(game_id: int, scoreboard_service: ScoreboardService = Depends()):
    return await scoreboard_service.get_scoreboard_by_id(game_id)

@app.get('/scoreboard', response_model=Scoreboard)
async def get_scoreboard(scoreboard_service: ScoreboardService = Depends()):
    return await scoreboard_service.get_scoreboard()

@app.post('/result', response_model=AddRecord)
async def add_record(record: AddRecord, scoreboard_service: ScoreboardService = Depends()):
    return await scoreboard_service.add_record(record)

@app.post('/update_played')
async def set_games_played(add_games_played: AddGamesPlayed, scoreboard_service: ScoreboardService = Depends()):
    return await scoreboard_service.set_games_played(add_games_played)