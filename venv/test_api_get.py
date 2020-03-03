import requests
import json
import pytest

url = 'https://reqres.in/api/users/4'

resp = requests.get(url)
resp_json = resp.json()

def test_api_get_status_code():   # валидация кода ответа
    assert resp.status_code == 200

def test_api_get_resp_type():    # валидация формата ответа
    assert resp.headers['content-type'].split()[0] == 'application/json;'

def test_api_get_resp_charset(): # валидация кодировки
    assert resp.encoding == 'utf-8'

# существующий пример для сравнения
example_for_smoke={'data': {'id': 4,
  'email': 'eve.holt@reqres.in',
  'first_name': 'Eve',
  'last_name': 'Holt',
  'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/marcoramires/128.jpg'}}

def test_api_get_resp_json_smoke():  # праверка ранее полученного ответа
    assert resp_json == example_for_smoke

def test_api_get_not_exist():
    bad_id=9999999 #  ID не существующего клиента
    res=requests.get(f"{url}{bad_id}")
    assert res.status_code == 404

#пример параметризации , запуск функции с разными ID 
data_id=[2,6,8]
@pytest.mark.parametrize("id",data_id)
def test_api_get_status(id):   # валидация кода ответа
    resp=requests.get(f"https://reqres.in/api/users/{id}")
    assert resp.status_code == 200

#пример №2 параметризации , запуск функции с разными headers (эмитация работы разных браузеров)
headers = [({"User-Agent": "Mozilla/5.0"}),
           ({'User-Agent': "Google Chrome 53"})]

@pytest.mark.parametrize("headers",headers)
def test_api_get_status_headers(headers):   # валидация кода ответа
    resp=requests.get(url,headers=headers)
    assert resp.status_code == 200




