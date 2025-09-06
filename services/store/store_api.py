import requests
from services.store.endpoints import Endpoints


class StoreAPI:
    @staticmethod
    def create_order(order_data):
        return requests.post(Endpoints.PLACE_ORDER, json=order_data)

    @staticmethod
    def get_order(order_id: int):
        return requests.get(Endpoints.FIND_ORDER.format(order_id))

    @staticmethod
    def delete_order(order_id: int):
        return requests.delete(Endpoints.DELETE_ORDER.format(order_id))

    @staticmethod
    def get_inventory():
        return requests.get(Endpoints.GET_INVENTORY)
