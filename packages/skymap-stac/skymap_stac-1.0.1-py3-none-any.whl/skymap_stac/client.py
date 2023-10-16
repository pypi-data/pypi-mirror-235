import requests
from browser.local_storage import storage
from item_search import ItemSearch

class Client:
    def __init__(self, **kwargs):
        self.token = storage.get('token')

    @classmethod
    def open(self) -> "Client":
        if self.token:
            return self.token

    def search(self) -> "ItemSearch":
        pass