import pytest
from flask import Flask
from atadosapi.app import create_app


@pytest.fixture(scope="session")
def app() -> Flask:
    return create_app()
