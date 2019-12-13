def song_decoder(song):
    return ' '.join(song.replace('WUB', ' ').strip().split())
