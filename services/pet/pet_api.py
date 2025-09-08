from services.base import Base
from services.pet.endpoints import Endpoints

class PetAPI(Base):
    @staticmethod
    def create_pet(pet_data): 
        return PetAPI.post(Endpoints.PET, json=pet_data)

    @staticmethod
    def update_pet(pet_data):
        return PetAPI.put(Endpoints.PET, json=pet_data)

    @staticmethod
    def get_pet_by_id(pet_id):
        return PetAPI.get(Endpoints.PET_ID.format(pet_id))

    @staticmethod
    def delete_pet(pet_id):
        return PetAPI.delete(Endpoints.PET_ID.format(pet_id))

    @staticmethod
    def find_pet_by_status(status):
        return PetAPI.get(Endpoints.FIND_PET_BY_STATUS, params={"status": status})

    @staticmethod
    def upload_image(pet_id, image_path):
        with open(image_path, "rb") as f:
            files = {"file": f}
            return PetAPI.post(Endpoints.UPLOAD_IMAGE.format(pet_id), files=files)
