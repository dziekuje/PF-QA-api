import pytest
from brew_utils.brew_utils import *
import pprint


def test_api_response_is_200(api_client):
    res = api_client.get(path="/posts")
    assert res.status_code == 200


def test_api_get_all_users(api_client):
    res = api_client.get(path="/posts")
    # print(res.json())
    assert res.status_code == 200
    assert len(res.json()) > 1


@pytest.mark.parametrize("id", [1, 2, 3, 4])
def test_api_get_user_by_ID(api_client, id):
    res = api_client.get(path=f"/posts/{id}")
    print(res.json())
    assert res.status_code == 200
    assert res.json()["id"] == id


@pytest.mark.parametrize("user_id", [1, 2, 3, 4])
def test_api_get_user_by_userID(api_client, user_id):
    res = api_client.get(path="/posts", params=f"userId={user_id}")
    print(res.json())
    assert res.status_code == 200
    assert res.json()[0]["userId"] == user_id
