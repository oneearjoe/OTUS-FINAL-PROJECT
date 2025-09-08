from services.base import Base
from services.user.endpoints import Endpoints


class UserAPI(Base):
    @staticmethod
    def create_user(user_data):
        return UserAPI.post(Endpoints.CREATE_USER, json=user_data)

    @staticmethod
    def get_user_by_name(username):
        return UserAPI.get(Endpoints.GET_USER.format(username))

    @staticmethod
    def login(username, password):
        return UserAPI.get(Endpoints.USER_LOGIN.format(username, password))

    @staticmethod
    def logout():
        return UserAPI.get(Endpoints.USER_LOGOUT)

    @staticmethod
    def update_user(username, updated_data):
        return UserAPI.put(Endpoints.UPDATE_USER.format(username), json=updated_data)

    @staticmethod
    def delete_user(username):
        return UserAPI.delete(Endpoints.DELETE_USER.format(username))
