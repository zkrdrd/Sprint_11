from copy import deepcopy
from itertools import product

import pytest
from requests_toolbelt import MultipartEncoder

from helpers import (
    AnnonceData,
    Messagess,
    PathAPI,
    StatusCode,
    delete,
    delete_excess_fields,
    gen_user_data,
    patch,
    post,
)


class TestAnnonce:

    @pytest.mark.parametrize(
        "condition, category",
        list(product(AnnonceData.CONDITION, AnnonceData.CATEGORY)),
    )
    def test_create_annonce(self, new_user_data, condition, category):
        token = post(PathAPI.SINGUP, new_user_data)
        token = token["access_token"]["access_token"]
        AnnonceData.ANNONCE["condition"] = condition
        AnnonceData.ANNONCE["category"] = category
        m_path = MultipartEncoder(
            fields=AnnonceData.ANNONCE,
        )
        response = post(
            PathAPI.CREATE_ANNONCE,
            data=m_path,
            headers={
                "Accept": "application/json",
                "Authorization": f"Bearer {token}",
                "Content-Type": m_path.content_type,
            },
        )
        assert response["name"] == AnnonceData.ANNONCE["name"]
        assert response["category"] == category
        assert response["condition"] == condition
        assert response["city"] == AnnonceData.ANNONCE["city"]
        assert response["description"] == AnnonceData.ANNONCE["description"]
        assert str(response["price"]) == AnnonceData.ANNONCE["price"]
        assert response["img1"] is None
        assert response["img2"] is None
        assert response["img3"] is None

    @pytest.mark.parametrize(
        "field_name, value",
        [
            ("name", "name"),
            ("category", AnnonceData.CATEGORY[1]),
            ("condition", AnnonceData.CONDITION[1]),
            ("city", AnnonceData.ANNONCE_CITY[1]),
            ("description", "description"),
            ("price", "1234"),
        ],
    )
    def test_edit_annonced(self, new_user_data, field_name, value):
        token = post(PathAPI.SINGUP, new_user_data)
        token = token["access_token"]["access_token"]
        AnnonceData.ANNONCE["city"] = AnnonceData.ANNONCE_CITY[0]
        AnnonceData.ANNONCE["condition"] = AnnonceData.CONDITION[0]
        AnnonceData.ANNONCE["category"] = AnnonceData.CATEGORY[0]
        m_path = MultipartEncoder(
            fields=AnnonceData.ANNONCE,
        )
        response_post = post(
            PathAPI.CREATE_ANNONCE,
            data=m_path,
            headers={
                "Accept": "application/json",
                "Authorization": f"Bearer {token}",
                "Content-Type": m_path.content_type,
            },
        )
        id_element = str(response_post["id"])
        delete_excess_fields(response_post)
        response_post_copy = deepcopy(response_post)
        response_post[field_name] = value
        m_path = MultipartEncoder(
            fields=response_post,
        )
        response_patch = patch(
            PathAPI.UPDATE_ANNONCE + id_element,
            data=m_path,
            headers={
                "Accept": "application/json",
                "Authorization": f"Bearer {token}",
                "Content-Type": m_path.content_type,
            },
        )
        delete_excess_fields(response_patch)
        dif = set(response_patch.values()) - set(response_post_copy.values())
        assert dif == {value}

    def test_edit_annonce_with_another_token(self, new_user_data):
        user_1 = post(PathAPI.SINGUP, new_user_data)
        token_user_1 = user_1["access_token"]["access_token"]
        m_path = MultipartEncoder(
            fields=AnnonceData.ANNONCE,
        )
        response_post = post(
            PathAPI.CREATE_ANNONCE,
            data=m_path,
            headers={
                "Accept": "application/json",
                "Authorization": f"Bearer {token_user_1}",
                "Content-Type": m_path.content_type,
            },
        )
        user_2 = post(PathAPI.SINGUP, gen_user_data())
        token_user_2 = user_2["access_token"]["access_token"]
        id_element = str(response_post["id"])
        delete_excess_fields(response_post)
        response_post["name"] = "name_2"
        m_path = MultipartEncoder(
            fields=response_post,
        )
        response_patch = patch(
            PathAPI.UPDATE_ANNONCE + id_element,
            data=m_path,
            headers={
                "Accept": "application/json",
                "Authorization": f"Bearer {token_user_2}",
                "Content-Type": m_path.content_type,
            },
        )
        assert response_patch["message"] == Messagess.UNATORIZED_MSG
        assert response_patch["statusCode"] == StatusCode.UNAUTORIZED

    def test_delete_annonce(self, new_user_data):
        user_1 = post(PathAPI.SINGUP, new_user_data)
        token_user_1 = user_1["access_token"]["access_token"]
        m_path = MultipartEncoder(
            fields=AnnonceData.ANNONCE,
        )
        response_post = post(
            PathAPI.CREATE_ANNONCE,
            data=m_path,
            headers={
                "Accept": "application/json",
                "Authorization": f"Bearer {token_user_1}",
                "Content-Type": m_path.content_type,
            },
        )
        response = delete(
            PathAPI.DELETE_ANNONCE + str(response_post["id"]),
            headers={
                "Accept": "application/json",
                "Authorization": f"Bearer {token_user_1}",
            },
        )
        assert response["message"] == Messagess.ANNONCED_DELETE_SUCCESSFULLY
