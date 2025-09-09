import allure
import pytest
from services.pet.pet_api import PetAPI
from services.base import Base

@pytest.mark.api
@allure.feature("Pet API")
@allure.story("Edit existing pet")
def test_add_new_pet(pet_data):
    response = PetAPI.create_pet(pet_data)
    PetAPI.check_response_status_code(response, 200)
    assert response.json()["name"] == pet_data["name"], f"Имя питомца не совпадает: ожидалось {pet_data['name']}, получено {response.json()['name']}"

@pytest.mark.api
@allure.feature("Pet API")
@allure.story("Редактирование существующего питомца")
def test_edit_existing_pet(pet_data):
    PetAPI.create_pet(pet_data)
    pet_data["status"] = "sold"
    response = PetAPI.update_pet(pet_data)
    PetAPI.check_response_status_code(response, 200)
    assert response.json()["status"] == "sold", f"Статус питомца не совпадает: ожидалось 'sold', получено {response.json()['status']}"

@pytest.mark.api
@allure.feature("Pet API")
@allure.story("Удаление питомца")
def test_delete_pet(pet_data):
    PetAPI.create_pet(pet_data)
    response = PetAPI.delete_pet(pet_data["id"])
    PetAPI.check_response_status_code(response, 200)

@pytest.mark.api
@allure.feature("Pet API")
@allure.story("Поиск питомца по ID")
def test_find_pet_by_id(pet_data):
    PetAPI.create_pet(pet_data)
    response = Base.wait_for_status(PetAPI.get_pet_by_id, 200, pet_id=pet_data["id"])
    PetAPI.check_response_status_code(response, 200)
    assert response.json()["id"] == pet_data["id"], f"ID питомца не совпадает: ожидалось {pet_data['id']}, получено {response.json()['id']}"

@pytest.mark.api
@allure.feature("Pet API")
@allure.story("Поиск питомцев по статусу")
@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_find_pet_by_status(status):
    response = PetAPI.find_pet_by_status(status)
    PetAPI.check_response_status_code(response, 200)
    for pet in response.json():
        assert pet["status"] == status, f"Статус питомца не совпадает: ожидалось {status}, получено {pet['status']}"

@pytest.mark.api
@allure.feature("Pet API")
@allure.story("Добавление изображения к питомцу")
def test_add_image_to_pet(pet_data):
    PetAPI.create_pet(pet_data)
    response = PetAPI.upload_image(pet_data["id"], "test_data/image.jpg")
    PetAPI.check_response_status_code(response, 200)
