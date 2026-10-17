import pytest  # pylint: disable=import-error

from helpers import gen_user_data


@pytest.fixture()
def new_user_data():
    """Генерация пользваоетля передача в тест и удаление данных"""
    data = gen_user_data()
    yield data
