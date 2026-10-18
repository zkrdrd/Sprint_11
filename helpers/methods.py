import requests


def post(url: str, json: dict = None, data=None, headers: dict = None) -> dict:
    """Шаблон post запроса"""
    return requests.post(url, json=json, data=data, headers=headers, timeout=10).json()


def patch(url: str, json: dict = None, data=None, headers: dict = None) -> dict:
    """Шаблон patch запроса"""
    return requests.patch(url, json=json, data=data, headers=headers, timeout=10).json()


def delete(url: str, headers: dict = None) -> dict:
    """Шаблон Delete запроса"""
    return requests.delete(url, headers=headers, timeout=10).json()
