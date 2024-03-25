## Flask APIs for Song Data Management

This Flask application provides a RESTful API for managing song data stored in a SQLite database. The API allows users to retrieve information about songs, rate songs, and interact with the song database.

### Features:

1. **Retrieve All Songs:**

   - Endpoint: `/api/songs`
   - Method: GET
   - Description: Retrieves all songs stored in the database. Supports pagination for large datasets.
2. **Retrieve Song by Title:**

   - Endpoint: `/api/songs/<title>`
   - Method: GET
   - Description: Retrieves information about a specific song by its title.
3. **Rate a Song:**

   - Endpoint: `/api/songs/<song_id>/rate`
   - Method: POST
   - Description: Allows users to rate a song using a star rating system (1 to 5 stars). Updates the star rating for the specified song in the database.

### Additional Features:

- **Pagination:** The API supports pagination for retrieving large datasets, improving performance and usability.
- **Unit Tests:** Unit tests are provided to ensure the correctness and reliability of the API endpoints and methods.
- **Data Loading:** A script is available to load data from a JSON file into the SQLite database, populating it with song information.

### Technologies Used:

- **Flask:** Python micro-framework used for building the RESTful API.
- **SQLAlchemy:** ORM library for interacting with the SQLite database.
- **SQLite:** Lightweight, serverless database used for storing song data.

### Getting Started:

1. Clone the repository.
2. Create virtual environment using `venv` or `virtualenv` in `Python3`
3. Activate the python virtual environment in terminal.
4. Install the required libraries using cmd - `pip install -r requirements.txt    `
5. Run the Flask application.
6. Use the provided endpoints to interact with the song data.

### Commands to Execute

Run Flask App - `flask run`

Run Unit Test - `python test_app.py`

Run Script to Load Database - `python normalize_playlist.py`
