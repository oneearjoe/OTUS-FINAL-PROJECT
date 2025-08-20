from services.base import Base


class Endpoints:

    def __init__(self):
        self.base = Base()
    


    PLACE_ORDER = f"{Base.BASE_URL}/v2/store/order"
    FIND_ORDER = f"{Base.BASE_URL}/v2/store/order/{{}}"
    DELETE_ORDER = f"{Base.BASE_URL}/v2/store/order/{{}}"
    GET_INVENTORY = f"{Base.BASE_URL}/v2/store/inventory"