from flask import Blueprint, jsonify, request
from db import Song, db

songs_api = Blueprint("songs", __name__)

@songs_api.route('/api/songs', methods=['GET'])
def get_all_songs():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    songs = Song.query.paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({"items": [song.to_dict() for song in songs.items],"current_page": page, "total": songs.total})

@songs_api.route('/api/songs/<title>', methods=['GET'])
def get_song_by_title(title):
    song = Song.query.filter_by(title=title).first()
    if song:
        return jsonify(song.to_dict())
    else:
        return jsonify({'error': 'Song not found'}), 404

# Endpoint for rating a song
@songs_api.route('/api/songs/<string:song_id>/rate', methods=['POST'])
def rate_song(song_id):
    song = Song.query.get(song_id)
    if not song:
        return jsonify({'error': 'Song not found'}), 404
    rating = request.json.get('rating')
    if rating is None or not isinstance(rating, int) or rating < 1 or rating > 5:
        return jsonify({'error': 'Invalid rating. Rating must be an integer between 1 and 5.'}), 400
    
    song.star_rating = rating
    db.session.commit()
    return jsonify({'message': 'Rating updated successfully'})
