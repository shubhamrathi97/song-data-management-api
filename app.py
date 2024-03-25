from flask import Flask
from db import db
from api import songs_api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./songs.db'
app.register_blueprint(songs_api)
db.init_app(app)
app.app_context().push()


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
