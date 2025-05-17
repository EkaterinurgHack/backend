import pandas as pd
from collections import defaultdict

from app.schemas.scoreboard import Record, Scoreboard, AddRecord

scoreboard = defaultdict(list)

scoreboard[1] = ["user1", 100]
scoreboard[2] = ["user2", 500]
scoreboard[3] = ["user3", 300]
scoreboard[4] = ["user4", 300]

class ScoreboardService():
    def __init__(self):
        pass

    async def add_record(self, record: AddRecord):
        user_id = record.user_id
        if user_id in scoreboard:
            value = scoreboard[user_id][1]
            scoreboard[user_id][1] = max(value, record.score)
            scoreboard[user_id][0] = record.nickname
        else:
            scoreboard[user_id] = [record.nickname, record.score]
        return record

    async def get_scoreboard(self):
        scores = sorted([[key, *value] for key, value in scoreboard.items()], key=lambda x: x[2], reverse=True)
        df = pd.DataFrame(scores, columns=['id', 'nickname', 'score'])
        df['rank'] = df['score'].rank(method='min', ascending=False).astype(int)
        scores = df.values.tolist()
        print(scores)
        return Scoreboard(
            scores=[Record(
                rank=score[3],
                user_id=score[0],
                nickname=score[1],
                score=score[2]
            ) for score in scores]
        )