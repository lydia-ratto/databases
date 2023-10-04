from lib.album import *

def test_album_initialised():
    album = Album(1, 'Example title', '1990', 2)

    assert album.id == 1
    assert album.title == 'Example title'
    assert album.year == '1990'
    assert album.artist_id == 2

