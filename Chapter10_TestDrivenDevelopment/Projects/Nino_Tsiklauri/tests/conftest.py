import tempfile
import os
import pytest
from src.ext import admin
from src import create_app
from src.commands import init_db, populate_db

@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app()
    app.config.update({
        "TESTING": True,
        "WTF_CSRF_ENABLED": False,
        "DEBUG": False,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///" + db_path + ".sqlite"
    })

    admin._views = []

    with app.app_context():
        init_db()
        populate_db()

    yield app

    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def server(app):
    return app.test_cli_runner()