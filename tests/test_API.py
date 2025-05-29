import allure
import requests
from pytest import mark


@mark.api
@allure.title("Find Pets by status")
def test_get_pets_by_status():
    url = "https://petstore.swagger.io/v2/pet/findByStatus?status=available&status=pending&status=sold"
    response = requests.get(url)

    # Verify status code
    assert response.status_code == 200
    # Verify content-type
    assert response.headers["Content-Type"] == "application/json"
    # Verify response structure (assuming a pet object with 'id' and 'status')
    pets = response.json()
    for pet in pets:
      assert pet["id"]
      assert pet["status"]

@mark.api
@allure.title("Update an existing pet")
def test_update_pet():
    url = "https://petstore.swagger.io/v2/pet" 
    pet_id = 98  # Existing pet ID to update
    updated_pet = {"id": pet_id, "category": {"id": 2, "name": "dolphin"}, "name": "willy"}
    response = requests.put(url, json=updated_pet)

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

    # Verify update was successful
    pet = response.json()
    assert pet["id"] == pet_id
    assert pet["category"] == updated_pet["category"]
    assert pet["name"] == updated_pet["name"]

@mark.api
@allure.title("Add a new pet to the store")
def test_create_pet():
    url = "https://petstore.swagger.io/v2/pet"
    pet_id = 99
    new_pet = {"id": pet_id, "category": {"id": 2, "name": "сat"}, "name": "kitty"}
    response = requests.post(url, json=new_pet)

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

    # Check if the pet was created
    pet = response.json()
    assert pet["id"] == pet_id
    assert pet["category"] == new_pet["category"]
    assert pet["name"] == new_pet["name"]

@mark.api
@allure.title("Find pet by ID")
@mark.parametrize("pet_id, status_code", [
    (99, 200),    # Valid pet ID
    (999, 404),  # Non-existent pet ID
])
def test_get_pet(pet_id, status_code):
    url = f"https://petstore.swagger.io/v2/pet/{pet_id}"
    response = requests.get(url)

    assert response.status_code == status_code
    assert response.headers["Content-Type"] == "application/json"


@mark.api
@allure.title("Delete a pet")
@mark.parametrize("pet_id, status_code", [
    (99, 200),    # Valid pet ID
    (999, 404),  # Non-existent pet ID
])
def test_delete_pet(pet_id, status_code):
    url = f"https://petstore.swagger.io/v2/pet/{pet_id}"
    response = requests.delete(url)
    assert response.status_code == status_code


@mark.api
@allure.title("Create list of users with given input array")
@mark.parametrize("request_body, status_code", [
    ([{"id": 0, "username": "ivalchuk", "firstName": "Ivan", "lastName": "Valchuk", "email": "ivan.valchuk@gmail.com", "password": "", "phone": "+342344324324"}], 200),    # Valid body
    ('{"id": 23, "category": {"id": 5, "name": "Ivan Valchuk"}}', 500),  # Wrong body
])
def test_create_list_of_users(request_body, status_code):
    url = "https://petstore.swagger.io/v2/user/createWithList"
    response = requests.post(url, json=request_body)
    assert response.status_code == status_code
    assert response.headers["Content-Type"] == "application/json"


@mark.api
@allure.title("Place an order for a pet")
@mark.parametrize("request_body, status_code", [
    ({"id": 0, "petId": 0, "quantity": 0, "shipDate": "2025-05-29T18:04:43.451Z", "status": "placed", "complete": True}, 200),    # Valid body
    ({"id:": 0, "petId": 0, "quantity": 0, "shipDate": "2025-29T18:04:43.451Z", "status": "placed", "complete": True}, 500),  # Wrong body
])
def test_create_order_for_pet(request_body, status_code):
    url = "https://petstore.swagger.io/v2/store/order"
    response = requests.post(url, json=request_body)
    a = response.status_code
    assert response.status_code == status_code
    assert response.headers["Content-Type"] == "application/json"