import requests
import json
import pytest
from faker import Faker

faker = Faker()     # Генерация тестовых данных

def random_test_data(): # Функция генерирует рандомные имя и профессию.
    return {
        "name": faker.first_name(),
        "job": faker.job(),
           }

url='https://reqres.in/api/users'
#data = {'name': 'Michael', 'job': 'Art therapist'}
data=random_test_data()

r=requests.post(url, data=data)

def func_post_get_json():
    return requests.post(url, data=data).json()

@pytest.mark.smoke
def test_post_smoke():
    # валидация кода ответа, типа ответа и кодировки
    assert r.status_code == 201
    assert r.headers['content-type'].split()[0] == 'application/json;'
    assert r.encoding == 'utf-8'

def test_post_check_mame():
    assert r.json().get("name") == data["name"]

def test_post_check_job():
    assert r.json().get("job") == data["job"]

@pytest.mark.xfail(reason="тестовая api  возвращает только захардкоженные данные с id от 1 до 12")
def test_post_check_id():
    res = requests.get(f"{url}/{id}")
    assert res.status_code ==200


def func_db():
    """Функция сканирует все страницы (выбрано первые 15 id) и заносит найденные ID в словарь"""
    list = []
    for page in range(1, 16):
        #print(f"{url}/{page}", requests.get(f"{url}/{page}").status_code)
        if requests.get(f"{url}/{page}").status_code == 200:
            list.append(page)
    return list

@pytest.mark.regression
def test_post_check_existed_id():
    """  создается новая запись и проверяется перезаписан ли id , из сохраненного списка"""
    list_id=func_db()
    id = requests.post(url, data=data).json().get("id")
    assert id not in list_id

@pytest.mark.regression
def test_post_similar_name():
    """При добавлении одинаковых имени и профессии проверяется что будут присвоены разные ID,
     к примеру "Галя, старший кассир" может обитать в каждом магазине, но id у каждой Гали свой"""
    assert func_post_get_json().get("id") != func_post_get_json().get("id")

