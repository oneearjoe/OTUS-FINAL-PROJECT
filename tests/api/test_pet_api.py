import allure
import pytest
from services.pet.pet_api import PetAPI
from services.base import Base

@pytest.mark.api
@allure.feature("Pet API")
@allure.story("Edit existing pet")
def test_add_new_pet(pet_data):
    response = PetAPI.create_pet(pet_data)
    assert response.status_code == 200, f"Ожидался статус 200 при создании питомца, получен {response.status_code}"
    assert response.json()["name"] == pet_data["name"], f"Имя питомца не совпадает: ожидалось {pet_data['name']}, получено {response.json()['name']}"

@pytest.mark.api
@allure.feature("Pet API")
@allure.story("Редактирование существующего питомца")
def test_edit_existing_pet(pet_data):
    PetAPI.create_pet(pet_data)
    pet_data["status"] = "sold"
    response = PetAPI.update_pet(pet_data)
    assert response.status_code == 200, f"Ожидался статус 200 при обновлении питомца, получен {response.status_code}"
    assert response.json()["status"] == "sold", f"Статус питомца не совпадает: ожидалось 'sold', получено {response.json()['status']}"

@pytest.mark.api
@allure.feature("Pet API")
@allure.story("Удаление питомца")
def test_delete_pet(pet_data):
    PetAPI.create_pet(pet_data)
    response = PetAPI.delete_pet(pet_data["id"])
    assert response.status_code == 200, f"Ожидался статус 200 при удалении питомца, получен {response.status_code}"

@pytest.mark.api
@allure.feature("Pet API")
@allure.story("Поиск питомца по ID")
def test_find_pet_by_id(pet_data):
    PetAPI.create_pet(pet_data)
    response = Base.wait_for_status(PetAPI.get_pet_by_id, 200, pet_id=pet_data["id"])
    assert response.status_code == 200, f"Ожидался статус 200 при поиске питомца по ID, получен {response.status_code}"
    assert response.json()["id"] == pet_data["id"], f"ID питомца не совпадает: ожидалось {pet_data['id']}, получено {response.json()['id']}"

@pytest.mark.api
@allure.feature("Pet API")
@allure.story("Поиск питомцев по статусу")
@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_find_pet_by_status(status):
    response = PetAPI.find_pet_by_status(status)
    assert response.status_code == 200, f"Ожидался статус 200 при поиске питомцев по статусу {status}, получен {response.status_code}"
    for pet in response.json():
        assert pet["status"] == status, f"Статус питомца не совпадает: ожидалось {status}, получено {pet['status']}"

@pytest.mark.api
@allure.feature("Pet API")
@allure.story("Добавление изображения к питомцу")
def test_add_image_to_pet(pet_data):
    PetAPI.create_pet(pet_data)
    response = PetAPI.upload_image(pet_data["id"], "test_data/image.jpg")
    assert response.status_code == 200, f"Ожидался статус 200 при загрузке изображения, получен {response.status_code}"