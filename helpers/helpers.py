from random import choice, randint
from string import ascii_lowercase


def generate_random_digit() -> str:
    return str(randint(1, 10000))


def get_random_from_list(array: list) -> str:
    return choice(array)


def generate_random_string(length: int = 10) -> str:
    """Генерирует случайную строку из строчных букв."""
    letters = ascii_lowercase
    return "".join(choice(letters) for _ in range(length))


def generate_unique_email() -> str:
    """Генерирует уникальный email."""
    return f"{generate_random_string()}@example.com"


def gen_user_data() -> dict[str, str]:
    return {
        "email": generate_unique_email(),
        "password": generate_random_string(),
    }


def delete_excess_fields(array: list):
    del array["id"]
    del array["owner"]
    del array["updatedAt"]
    del array["createdAt"]
    del array["isFavorite"]
    array["price"] = str(array["price"])
