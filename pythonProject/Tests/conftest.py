import json

import base64
from requests import post
import pytest




client_id = "ckkk"
client_secret = "cccc"

@pytest.fixture( scope="session")
def get_token():
    auth_base64 = ""
    data = ""
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode ( "utf-8" )
    auth_base64 = str ( base64.b64encode ( auth_bytes ), "utf-8" )

    url = "https://accounts.spotify.com/api/token"
    headers = {"Authorization": "Basic " + auth_base64,
                   "Content-Type": "application/x-www-form-urlencoded"}

    data = {"grant_type": "client_credentials"}

    result = post ( url, headers=headers, data=data )
    json_results = json.loads ( result.content )
    access_token = json_results['access_token']
    return access_token

@pytest.fixture( scope="session")
def get_auth_header(token):
    return {"Authorization" : "Bearer "+ token}