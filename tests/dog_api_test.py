import requests
import pytest

# utils part
# TODO: refactor this part, move into separate module
def word_found(whole_string, word_to_find):
   if whole_string.find(word_to_find) != -1:
      return True
   return False

# test part
def test_dog_api_response_is_200():
    r = requests.get('https://dog.ceo/api/breeds/list/all')
    assert r.status_code == 200

    print("\n------- status/headers ---------")
    print(r.status_code)
    print(r.headers['content-type'])
    print("--------------------------------")

@pytest.mark.parametrize("breed_param", ['hound', 'terrier', "stbernard"])
def test_dog_api_receive_random_image_by_breed(breed_param):
    # print(breed_param)

    r = requests.get(f'https://dog.ceo/api/breed/{breed_param}/images/random')
    # print(r.json())
    # print(type(r.json()))

    dog_link = r.json()['message']
    # print(dog_link)
    # print(word_found(dog_link, breed_param))

    assert r.status_code == 200
    assert word_found(dog_link, breed_param) == True


@pytest.mark.parametrize("breed_param, sub_breed_list", [('hound', ['afghan', 'basset', 'blood', 'english', 'ibizan', 'plott', 'walker']), ('terrier', ['american', 'australian', 'bedlington', 'border', 'dandie', 'fox', 'irish', 'kerryblue', 'lakeland', 'norfolk', 'norwich', 'patterdale', 'russell', 'scottish', 'sealyham', 'silky', 'tibetan', 'toy', 'westhighland', 'wheaten', 'yorkshire']), ('stbernard', [])])
def test_dog_api_list_all_subbreed(breed_param, sub_breed_list):
    r = requests.get(f'https://dog.ceo/api/breed/{breed_param}/list')
    assert r.status_code == 200
    # print(r.json()['message'])
    response_list = r.json()['message']

    assert response_list == sub_breed_list
