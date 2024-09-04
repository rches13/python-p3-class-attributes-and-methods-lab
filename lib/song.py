class Song:
    
    count = 0
    genres = []
    artists = []


    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.genres.append(self.genre)
        Song.artists.append(artist)
        Song.genre_count[self.genre] = Song.genre_count.get(self.genre, 0) + 1
        Song.artist_count[self.artist] = Song.artist_count.get(self.artist, 0) + 1

    @classmethod
    def genre_count(cls):
        return cls.count
    
    @classmethod
    def artist_count(cls):
        return cls.count
    

    