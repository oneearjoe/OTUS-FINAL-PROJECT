from services.base import Base


class Endpoints:
    def __init__(self):
        self.base = Base()

    PET = f"{Base.BASE_URL}/v2/pet"
    PET_ID = f"{PET}/{{}}"
    FIND_PET_BY_STATUS = f"{PET}/findByStatus"
    UPLOAD_IMAGE = f"{Base.BASE_URL}/v2/pet/{{}}/uploadImage"
