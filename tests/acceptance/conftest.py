import pytest
from src.Application.App import App
from src.Services.ApiService import ApiService


@pytest.fixture
def app():
    app_instance = App(ApiService())._app
    return app_instance


@pytest.fixture
def client(app):
    return app.test_client()
