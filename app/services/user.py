from app.schemas.user import UserInfo

class UserService():
    def __init__(self):
        pass

    async def get_data(self):
        return UserInfo(
            user_id=200,
            nickname="NickName"
        )