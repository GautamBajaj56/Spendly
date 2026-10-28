# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands
- **Run App**: `python app.py` (runs on port 5001)
- **Run Tests**: `pytest`
- **Run Single Test**: `pytest path/to/test_file.py`
- **Install Dependencies**: `pip install -r requirements.txt`

## Architecture
The project is a Flask-based expense tracker application.

- **`app.py`**: Main entry point. Contains the Flask application instance and route definitions.
- **`database/`**: Handles data persistence.
    - `db.py`: Intended to house database connection logic (`get_db`), initialization (`init_db`), and seeding (`seed_db`) for a SQLite database.
- **`static/`**: Contains frontend assets (CSS in `static/css` and JS in `static/js`).
- **`templates/`**: Contains Jinja2 HTML templates for the application pages.

The application follows a traditional Flask structure where routes in `app.py` render templates from the `templates` directory.
