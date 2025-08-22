import requests
from services.user.endpoints import Endpoints


class UserAPI:
    @staticmethod
    def create_user(user_data):
        return requests.post(Endpoints.CREATE_USER, json=user_data)

    @staticmethod
    def get_user_by_name(username):
        return requests.get(Endpoints.GET_USER.format(username))

    @staticmethod
    def login(username, password):
        return requests.get(Endpoints.USER_LOGIN.format(username, password))

    @staticmethod
    def logout():
        return requests.get(Endpoints.USER_LOGOUT)

    @staticmethod
    def update_user(username, updated_data):
        return requests.put(Endpoints.UPDATE_USER.format(username), json=updated_data)

    @staticmethod
    def delete_user(username):
        return requests.delete(Endpoints.DELETE_USER.format(username))
