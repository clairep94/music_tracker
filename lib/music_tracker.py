class MusicTracker:
    def __init__(self):
        self.tracks = {}
    
    def add(self,artist,song):
        # artist_list = list(self.tracks.keys())
        artist_list = [artist for artist in self.tracks]
        if artist.title() in artist_list:
            song_list = self.tracks[artist.title()]
            if song.title() in song_list:
                raise Exception("Track already added")
            else:
                song_list.append(song.title())
                self.tracks[artist.title()] = song_list
        else:
            self.tracks[artist.title()] = [song.title()]

    def all(self):
        return self.tracks