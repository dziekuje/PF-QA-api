import pytest
import requests


class API_Client:
    """
    Simplified client for working with API
    Initialized by the base url to which requests will go
    """
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path="/", params=None):
        return requests.get(url=self.base_url + path, params=params)

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_url + path
        return requests.post(url=url, params=params, data=data, headers=headers)


# TODO: refactor, make configurable base_url
@pytest.fixture(scope="session")
def api_client(request):
    base_url = "https://jsonplaceholder.typicode.com"
    return API_Client(base_url=base_url)