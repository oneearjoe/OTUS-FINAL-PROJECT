from services.base import Base
from services.store.endpoints import Endpoints


class StoreAPI(Base):
    @staticmethod
    def create_order(order_data):
        return StoreAPI.post(Endpoints.PLACE_ORDER, json=order_data)

    @staticmethod
    def get_order(order_id):
        return StoreAPI.get(Endpoints.FIND_ORDER.format(order_id))

    @staticmethod
    def delete_order(order_id):
        return StoreAPI.delete(Endpoints.DELETE_ORDER.format(order_id))

    @staticmethod
    def get_inventory():
        return StoreAPI.get(Endpoints.GET_INVENTORY)
