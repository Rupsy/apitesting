import pytest

from Resources.albums import Albums
from Resources.authentication import Authentication


def test_search(get_token  ):
   token = get_token
   headers = Authentication.get_auth_headers(token)
   Albums.search_for_artist(headers , "Adele")



