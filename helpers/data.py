from helpers.helpers import (
    generate_random_digit,
    generate_random_string,
    get_random_from_list,
)


class BaseURL:
    URL = "https://qa-desk.education-services.ru"


class PathAPI(BaseURL):
    SINGUP = f"{BaseURL.URL}/api/signup"
    SINGIN = f"{BaseURL.URL}/api/signin"
    CREATE_ANNONCE = f"{BaseURL.URL}/api/create-listing"
    UPDATE_ANNONCE = f"{BaseURL.URL}/api/update-offer/"
    DELETE_ANNONCE = f"{BaseURL.URL}/api/listings/"
    DELETE_USER = f"{BaseURL.URL}/api/delete-user/"


class Messagess:
    DEFAULT_USER_NAME = "User"
    EMAIL_IN_USER = "Почта уже используется"
    UNATORIZED_MSG = "Оффер не найден или у вас нет прав на его редактирование"
    ANNONCED_DELETE_SUCCESSFULLY = "Объявление удалено успешно"


class StatusCode:
    BAD_REQUEST = 400
    UNAUTORIZED = 401


class AnnonceData:
    CONDITION = ["Новое", "Б/У"]
    CATEGORY = ["Авто", "Книги", "Садоводство", "Хобби", "Технологии"]
    ANNONCE_CITY = [
        "Москва",
        "Санкт-Петербург",
        "Новосибирск",
        "Екатеринбург",
        "Нижний Новгород",
        "Казань",
    ]
    ANNONCE = {
        "name": generate_random_string(),
        "category": get_random_from_list(CATEGORY),
        "condition": get_random_from_list(CONDITION),
        "city": get_random_from_list(ANNONCE_CITY),
        "description": generate_random_string(),
        "price": generate_random_digit(),
        "img1": None,
        "img2": None,
        "img3": None,
    }
