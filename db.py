from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Song(db.Model):
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String(250), index=True)
    danceability = db.Column(db.Float)
    energy = db.Column(db.Float)
    key = db.Column(db.Integer)
    loudness = db.Column(db.Float)
    mode = db.Column(db.Integer)
    acousticness = db.Column(db.Float)
    instrumentalness = db.Column(db.Float)
    liveness = db.Column(db.Float)
    valence = db.Column(db.Float)
    tempo = db.Column(db.Float)
    duration_ms = db.Column(db.Integer)
    time_signature = db.Column(db.Integer)
    num_bars = db.Column(db.Integer)
    num_sections = db.Column(db.Integer)
    num_segments = db.Column(db.Integer)
    song_class = db.Column('class', db.Integer)
    star_rating = db.Column(db.Integer)  # Added for bonus point

    def to_dict(self):
        return {c.name: getattr(self, c._label, getattr(self, c.name, None)) for c in self.__table__.columns}
