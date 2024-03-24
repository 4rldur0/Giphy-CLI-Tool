from data import Data
import click
import sys
import os

api_key = os.environ["GIPHY_API_KEY"]

@click.group()
def gif():
    print("hello from giphy cli!")


@gif.command()
@click.option('-s', is_flag=True)
def trending(s):
    print("trending subcommand called!")
    params = {
        "api_key": api_key,
        "limit": 25,
        "offset": 0,
        "rating": "g",
        "bundle": "messaging_non_clips"
    }
    d = Data("trending", api_key, params)
    if s:
        click.echo(d.get_data())
    return d.get_data()

@gif.command()
@click.argument('q')
def search(q):
    print("search subcommand called!")
    params = {
        "api_key": api_key,
        "q": q,
        "limit": 25,
        "offset": 0,
        "rating": "g",
        "bundle": "messaging_non_clips"
    }
    d = Data("search", api_key, params)
    return d.get_data()
    
if __name__ == "__main__":
    print(api_key)
    gif()
