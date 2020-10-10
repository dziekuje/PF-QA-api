import requests
import pytest


# TODO: refactor this part, move into separate common file
def string_found(string1, string2):
   if string2.find(string1):
      return True
   return False


def test_dog_api_response_is_200():
    r = requests.get('https://dog.ceo/api/breeds/list/all')
    assert r.status_code == 200

    print("\n------- status/headers ---------")
    print(r.status_code)
    print(r.headers['content-type'])
    print("--------------------------------")

@pytest.mark.parametrize("breed_param", ['hound', 'terrier', "stbernard"])
def test_dog_api_receive_random_image_by_breed(breed_param):
    print(breed_param)
    r = requests.get(f'https://dog.ceo/api/breed/{breed_param}/images/random')
    print(r.json())
    print(type(r.json()))

    dog_link = r.json()['message']

    assert r.status_code == 200
    assert string_found(dog_link, breed_param)