import json

import requests
from requests import get

from Config.config import Configu


class Albums:

    def search_for_artist( header , artist_name):

        url = Configu.BASE_URL+"/search"
        query = f"?q={artist_name}&type=artist&limit=1"
        query_url = url + query

        req = requests.get(query_url , headers = header)
        #headers = {"HTTP_HOST": "MyVeryOwnHost"}
        json_response = json.loads(req.content)
        print  (json_response)



