import unittest
import json
from app import app
from db import db, Song

class TestSongAPI(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()
        
        # Inserting dummy data
        song1 = Song(id="5s8TNhF23nv2Pumf0JTe2h", title='Song 1', danceability=0.8, energy=0.6)
        song2 = Song(id="3yM1SaSngFZCla4gOOUn2b", title='Song 2', danceability=0.7, energy=0.5)
        db.session.add_all([song1, song2])
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
    def test_get_all_songs(self):
        response = self.app.get('/api/songs')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data.get('items')), 2)
        self.assertEqual(data['items'][0]['title'], 'Song 1')
        self.assertEqual(data['items'][1]['title'], 'Song 2')
        
    def test_get_all_songs_pagination(self):
        response = self.app.get('/api/songs', query_string={"page": 2, "per_page":1})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data.get('items')), 1)
        self.assertEqual(data.get('total'), 2)
        self.assertEqual(data.get('current_page'), 2)

    def test_get_song_by_title(self):
        response = self.app.get('/api/songs/Song 1')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['title'], 'Song 1')
        
    def test_get_song_by_invalid_title(self):
        response = self.app.get('/api/songs/Invalid Song')
        self.assertEqual(response.status_code, 404)
        
    def test_rate_song(self):
        song_id = "5s8TNhF23nv2Pumf0JTe2h"
        response = self.app.post(f'/api/songs/{song_id}/rate', json={'rating': 4})
        self.assertEqual(response.status_code, 200)
        
        # Check if the rating is updated
        song = Song.query.get(song_id)
        self.assertEqual(song.star_rating, 4)
        
    def test_rate_invalid_song(self):
        song_id = 999  # Assuming song with ID 999 does not exist
        response = self.app.post(f'/api/songs/{song_id}/rate', json={'rating': 4})
        self.assertEqual(response.status_code, 404)
        
    def test_invalid_rating_value(self):
        song_id = "5s8TNhF23nv2Pumf0JTe2h"
        response = self.app.post(f'/api/songs/{song_id}/rate', json={'rating': 6})
        self.assertEqual(response.status_code, 400)
        
if __name__ == '__main__':
    unittest.main()
