from lib.album_repository import *

def test_empty_repository_initialised():
    repository = AlbumRepository()

    assert repository.list == []

def test_add_album_alters_list_attribute():
    repository = AlbumRepository()
    repository.add('album')

    assert repository.list == ['album']

def test_all_returns_list_attribute():
    repository = AlbumRepository()
    repository.add('album')

    assert repository.all() == ['album']
