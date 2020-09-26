# -*- coding: utf-8 -*-

from app import create_app

app = create_app("development")


@app.cli.command()
def test():
    pass


@app.cli.command('fill_db')
def fill_db():
    """Fills database with random data."""

    # Import your functions here
    #from utils.fake_generator import
