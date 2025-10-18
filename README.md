## Flask Comment App (Flask Comment App | Backend CRUD + Automated Testing Project)

A simple Flask-based REST API that allows users to create, read, update, and delete (CRUD) comments for a given task.
This project follows proper RESTful principles and includes automated tests using pytest.

# Technology Stack
Flask – as the main web framework

SQLAlchemy – for database ORM (Object Relational Mapping)

SQLite – as the database 

Pytest – for automated testing of all API endpoints

Postman – for manual verification and API testing
   
# Features

  Add new comments to tasks

  Retrieve comments by task ID

  Update existing comments

  Delete comments by comment ID

  Automated tests for all CRUD operations

# Project Structure

    flask_comment_app/
    │
    ├── app.py                 # Main application entry point
    ├── extensions.py          # Database (SQLAlchemy) initialization
    ├── models.py              # Comment model definition
    ├── routes/
    │   └── comments.py        # Comment CRUD routes (Blueprint)
    ├── test_comments.py       # Automated tests using pytest
    ├── __init__.py            # Package initializer
    └── requirements.txt       # Dependencies (Flask, SQLAlchemy, pytest, etc.)
