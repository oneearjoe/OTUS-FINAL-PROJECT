import requests
from services.pet.endpoints import Endpoints
import json


class PetAPI:
    @staticmethod
    def create_pet(pet_data):
        response = requests.post(Endpoints.PET, json=pet_data)
        return response

    @staticmethod
    def update_pet(pet_data):
        response = requests.put(Endpoints.PET, json=pet_data)
        return response

    @staticmethod
    def get_pet_by_id(pet_id):
        return requests.get(Endpoints.PET_ID.format(pet_id))

    @staticmethod
    def delete_pet(pet_id):
        return requests.delete(Endpoints.PET_ID.format(pet_id))

    @staticmethod
    def find_pet_by_status(status):
        return requests.get(Endpoints.FIND_PET_BY_STATUS, params={"status": status})

    @staticmethod
    def upload_image(pet_id, image_path):
        with open(image_path, "rb") as f:
            files = {"file": f}
            return requests.post(Endpoints.UPLOAD_IMAGE.format(pet_id), files=files)
