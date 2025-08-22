from services.base import Base


class Endpoints:
    def __init__(self):
        self.base = Base()

    CREATE_USER = f"{Base.BASE_URL}/v2/user"
    UPDATE_USER = f"{Base.BASE_URL}/v2/user/{{}}"
    GET_USER = f"{Base.BASE_URL}/v2/user/{{}}"
    DELETE_USER = f"{Base.BASE_URL}/v2/user/{{}}"
    USER_LOGIN = f"{Base.BASE_URL}/v2/user/login?username={{}}&password={{}}"
    USER_LOGOUT = f"{Base.BASE_URL}/v2/user/logout"
