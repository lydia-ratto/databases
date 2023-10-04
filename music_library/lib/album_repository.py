class AlbumRepository:
    def __init__(self, initial_list = None):
        self.list = [] if initial_list == None else initial_list

    def add(self, album):
        self.list.append(album)

    def all(self):
        return self.list