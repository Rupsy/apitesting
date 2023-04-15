import json

import requests
from requests import get

from Config.config import Configu


class Artist:

    def search_for_artist_id( header , artist_name):

        url = Configu.BASE_URL+"/search"
        query = f"?q={artist_name}&type=artist&limit=1"
        query_url = url + query

        req = requests.get(query_url , headers = header)
        #headers = {"HTTP_HOST": "MyVeryOwnHost"}
        json_response = json.loads(req.content)
        artists_rec =    json_response['artists']['items']
        for rec in   artists_rec:
            artisit_id = rec['id']
        return artisit_id




