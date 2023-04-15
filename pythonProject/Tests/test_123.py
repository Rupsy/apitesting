import pytest

from Resources.artist import Artist
from Resources.albums import Albums
from Resources.authentication import Authentication


def test_search(get_token  ):
   headers = get_token
   artist_id = Artist.search_for_artist_id(headers , "Adele")
   print("Artist ID == " , artist_id)
   list_of_albums = Albums.search_for_albums_by_artist(headers  , artist_id)
   print (list_of_albums)



