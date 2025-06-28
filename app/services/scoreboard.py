import pandas as pd
from collections import defaultdict

from app.schemas.scoreboard import Record, Scoreboard, AddRecord, GameScoreboard, AddGamesPlayed

game_scoreboards = [defaultdict(list) for i in range(4)]
games_played = defaultdict(list)

# game_scoreboards[0][1] = ["user1", 100]
# game_scoreboards[0][2] = ["user2", 500]
# game_scoreboards[0][3] = ["user3", 300]
# game_scoreboards[0][4] = ["user4", 300]
# game_scoreboards[1][1] = ["user1", 100]
# game_scoreboards[1][2] = ["user2", 500]
# game_scoreboards[1][3] = ["user3", 300]
# game_scoreboards[1][4] = ["user4", 300]
# game_scoreboards[2][1] = ["user1", 100]
# game_scoreboards[2][2] = ["user2", 500]
# game_scoreboards[2][3] = ["user3", 300]
# game_scoreboards[2][4] = ["user4", 300]
# game_scoreboards[3][1] = ["user1", 100]
# game_scoreboards[3][2] = ["user2", 500]
# game_scoreboards[3][3] = ["user3", 300]
# game_scoreboards[3][4] = ["user4", 300]

class ScoreboardService():
    def __init__(self):
        pass

    async def add_record(self, record: AddRecord):
        game_id = (record.game_id - 1) % 4
        user_id = record.user_id
        if user_id in game_scoreboards[game_id]:
            value = game_scoreboards[game_id][user_id][1]
            game_scoreboards[game_id][user_id][1] = max(value, record.score)
            game_scoreboards[game_id][user_id][0] = record.nickname
        else:
            game_scoreboards[game_id][user_id] = [record.nickname, record.score]
        return record

    async def get_scoreboard(self):
        scores = [sorted([[key, *value] for key, value in game_scoreboards[i].items()], key=lambda x: x[2], reverse=True) for i in range(len(game_scoreboards))]
        dfs = [pd.DataFrame(scores[i], columns=['id', 'nickname', 'score']) for i in range(len(game_scoreboards))]
        for i in range(len(game_scoreboards)):
            dfs[i]['rank'] = dfs[i]['score'].rank(method='min', ascending=False).astype(int)
        scores = [dfs[i].values.tolist() for i in range(len(game_scoreboards))]
        return Scoreboard(
            scoreboards=[
                GameScoreboard(
                    scores=[
                        Record(
                            rank=score[3],
                            user_id=score[0],
                            nickname=score[1],
                            score=score[2]
                        ) for score in scores[i]] 
                ) for i in range(len(game_scoreboards))]
        )
    
    async def get_scoreboard_by_id(self, game_id: int):
        scores = sorted([[key, *value] for key, value in game_scoreboards[game_id].items()], key=lambda x: x[2], reverse=True)
        df = pd.DataFrame(scores, columns=['id', 'nickname', 'score'])
        df['rank'] = df['score'].rank(method='min', ascending=False).astype(int)
        scores = df.values.tolist()
        return GameScoreboard(
            scores=[
                Record(
                    rank=score[3],
                    user_id=score[0],
                    nickname=score[1],
                    score=score[2]
            ) for score in scores] 
        ) 
    
    async def get_games_played(self, user_id: int):
        return games_played[user_id]
    
    async def set_games_played(self, add_games_played: AddGamesPlayed):
        games_played[add_games_played.user_id] = add_games_played.user_played