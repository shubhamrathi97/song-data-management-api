import json
from app import app
from db import db, Song

def load_db_from_json_file(json_file):
    with app.app_context():
        db.create_all()
        with open(json_file, 'r') as f:
            data = json.load(f)
            songs = []
            for id in range(len(data['id'])):
                id = str(id)
                song = Song(
                    id = data.get('id', {}).get(id, None),
                    title= data.get('title', {}).get(id, None),
                    danceability=data.get('danceability', {}).get(id, None),
                    energy=data.get('energy', {}).get(id, None),
                    key=data.get('key', {}).get(id, None),
                    loudness=data.get('loudness', {}).get(id, None),
                    mode=data.get('mode', {}).get(id, None),
                    acousticness=data.get('acousticness', {}).get(id, None),
                    instrumentalness=data.get('instrumentalness', {}).get(id, None),
                    liveness=data.get('liveness', {}).get(id, None),
                    valence=data.get('valence', {}).get(id, None),
                    tempo=data.get('tempo', {}).get(id, None),
                    duration_ms=data.get('duration_ms', {}).get(id, None),
                    time_signature=data.get('time_signature', {}).get(id, None),
                    num_bars=data.get('num_bars', {}).get(id, None),
                    num_sections=data.get('num_sections', {}).get(id, None),
                    num_segments=data.get('num_segments', {}).get(id, None),
                    song_class=data.get('class', {}).get(id, None)
                )
                songs.append(song)
            db.session.add_all(songs)
            db.session.commit()

if __name__ == '__main__':
    json_file = 'playlist[76].json'
    load_db_from_json_file(json_file)
    print('Data loaded successfully.')
