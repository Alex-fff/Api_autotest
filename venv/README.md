Пример авто-тестов для API.

Тестовое api для примера выбрано : url = https://reqres.in/

метод GET  -> url + /api/users/2 
метод Post (create) -> url + /api/users


В test_api_post.py приведены примеры :
 - маркировки тестов  на виды тестирования, например запустить смоук можно Api_autotest\venv>pytest -v test_api_post.py -m smoke
 - выбрана генерация тестовых данных( исп библ Faker)
 - помеченного xfail
Запуск: Api_autotest\venv>pytest -v test_api_post.py

В test_api_get.py приведен пример параметризации тестов.
Запуск:  \Api_autotest\venv>pytest -v test_api_get.py