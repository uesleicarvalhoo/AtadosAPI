import click
from . import db


def create_db() -> None:
    """Cria o banco de dados"""
    db.create_all()
    click.echo("Database criada com sucesso!")


def drop_db() -> None:
    """Limpa o banco de dados"""
    db.drop_all()
    click.echo("Database limpa com sucesso!")
