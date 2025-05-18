from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

class AddRecord(BaseModel):
    game_id: int
    user_id: int
    nickname: str
    score: int

    model_config = ConfigDict(from_attributes=True, alias_generator=to_camel, populate_by_name=True)

class Record(BaseModel):
    rank: int
    user_id: int
    nickname: str
    score: int

    model_config = ConfigDict(from_attributes=True, alias_generator=to_camel, populate_by_name=True)

class GameScoreboard(BaseModel):
    scores: list[Record]

    model_config = ConfigDict(from_attributes=True, alias_generator=to_camel, populate_by_name=True)

class Scoreboard(BaseModel):
    scoreboards: list[GameScoreboard]

    model_config = ConfigDict(from_attributes=True, alias_generator=to_camel, populate_by_name=True)

class AddGamesPlayed(BaseModel):
    user_id: int
    user_played: list[int]

    model_config = ConfigDict(from_attributes=True, alias_generator=to_camel, populate_by_name=True)
