from helpers.data import Messagess, PathAPI, StatusCode
from helpers.methods import post


class TestUser:
    def test_create_user(self, new_user_data):
        data = post(PathAPI.SINGUP, json=new_user_data)
        assert "access_token" in data
        assert data["user"]["email"] == new_user_data["email"]
        assert data["user"]["name"] == Messagess.DEFAULT_USER_NAME

    def test_create_duplicate_user(self, new_user_data):
        post(PathAPI.SINGUP, json=new_user_data)
        data = post(PathAPI.SINGUP, new_user_data)
        assert data["statusCode"] == StatusCode.BAD_REQUEST
        assert data["message"] == Messagess.EMAIL_IN_USER

    def test_login_user(self, new_user_data):
        post(PathAPI.SINGUP, json=new_user_data)
        data = post(PathAPI.SINGIN, new_user_data)
        assert "token" in data
        assert data["user"]["email"] == new_user_data["email"]
