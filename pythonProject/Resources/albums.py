import json

import requests
from requests import get

from Config.config import Configu


class Albums:

    def search_for_albums_by_artist( header , artist_id):

        url = Configu.BASE_URL+f"/artists/{artist_id}/top-tracks?country=US"

        ans = []

        req = requests.get(url , headers = header)
        #headers = {"HTTP_HOST": "MyVeryOwnHost"}
        json_response = json.loads(req.content)
        all_tracks_artist_det = json_response['tracks']

        for i in range(len(all_tracks_artist_det)):
            ans.append(all_tracks_artist_det[i]['name'])








