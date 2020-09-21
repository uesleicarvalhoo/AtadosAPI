from flask import Flask
from atadosapi.ext.db.commands import create_db, drop_db


def init_app(app: Flask) -> None:
    app.cli.add_command(app.cli.command()(create_db))
    app.cli.add_command(app.cli.command()(drop_db))
