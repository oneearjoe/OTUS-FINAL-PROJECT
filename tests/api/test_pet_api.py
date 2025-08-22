import pytest
from services.pet.pet_api import PetAPI
from services.base import Base


def test_add_new_pet(pet_data):
    response = PetAPI.create_pet(pet_data)
    assert response.status_code == 200
    assert response.json()["name"] == pet_data["name"]


def test_edit_existing_pet(pet_data):
    # Сначала создаем пета
    PetAPI.create_pet(pet_data)

    pet_data["status"] = "sold"
    response = PetAPI.update_pet(pet_data)
    assert response.status_code == 200
    assert response.json()["status"] == "sold"


def test_delete_pet(pet_data):
    PetAPI.create_pet(pet_data)
    response = PetAPI.delete_pet(pet_data["id"])
    assert response.status_code == 200


def test_find_pet_by_id(pet_data):
    PetAPI.create_pet(pet_data)
    response = Base.wait_for_status(PetAPI.get_pet_by_id, 200, pet_id=pet_data["id"])
    assert response.status_code == 200
    assert response.json()["id"] == pet_data["id"]


@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_find_pet_by_status(status):
    response = PetAPI.find_pet_by_status(status)
    assert response.status_code == 200
    for pet in response.json():
        assert pet["status"] == status


def test_add_image_to_pet(pet_data):
    PetAPI.create_pet(pet_data)
    response = PetAPI.upload_image(pet_data["id"], "test_data/image.jpg")
    assert response.status_code == 200
    assert "message" in response.json()
