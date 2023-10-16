import requests
from typing import Optional
from skymap_stac.item_search import (
    ItemSearch, 
    CollectionsLike, 
    IntersectsLike, 
    DatetimeLike,
    FilterLike,
    SortbyLike
)

ROLODEX_API_URL='http://192.168.4.204:8080'



class Client:
    def __init__(self, **kwargs):
        self.token = kwargs.get('token')
        # self.token = storage.get('token')

    @classmethod
    def open(cls):
        s = requests.Session()
        s.headers.update({
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTQ2NiwibmFtZSI6Imh1b25nLnZ0IiwiZW1haWwiOiJodW9uZ3Z0MjMwNEBnbWFpbC5jb20iLCJjb3VudHJ5IjoiVmlldG5hbSIsInBpY3R1cmUiOm51bGwsImlhdCI6MTY5NDYwMzYwNywiZXhwIjoxNjk3MTk1NjA3fQ.gvyfBCFaj6O2KxpbIc-qVhouipJWwzKUG1h9c7912wz5xBe-B7s6aNZhyB3tts2zw4SU1nBmMYDUQNVq_OhGvg',
        })

        data = {
            "product_name": "sen2",
            "aoi": {
                "type": "Polygon",
                "coordinates": [[
                    [104.14858238680847, 1.189077295023921],
                    [103.52866124251142, 1.189077295023921],
                    [103.52866124251142, 1.5405272307583147],
                    [104.14858238680847, 1.5405272307583147],
                    [104.14858238680847, 1.189077295023921]
                ]]
            },
            "time_range": "2023-09-13,2023-09-15"
        }

        response = s.post(f'{ROLODEX_API_URL}/api/cube/datasets', json=data)
        return response.json()

    def search(self,
               method: Optional[str] = 'POST',
               max_items: Optional[int] = None, 
               collections: Optional[CollectionsLike] = None, 
               intersects: Optional[IntersectsLike] = None, 
               datetime: Optional[DatetimeLike] = None, 
               filter: Optional[FilterLike] = None, 
               sortby: Optional[SortbyLike] = None
    ) -> "ItemSearch":
        return ItemSearch()