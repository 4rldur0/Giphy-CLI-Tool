from data import Data
import click
import sys
import os

class GiphyAPI:
    params = {
        "api_key": os.environ["GIPHY_API_KEY"],
        "limit": 25,
        "offset": 0,
        "rating": "g",
        "bundle": "messaging_non_clips"
    }

    @click.group()
    @staticmethod
    def gif():
        print("hello from giphy cli!")


    @gif.command()
    @click.option('-s', is_flag=True)
    def trending(s):
        print("trending subcommand called!")
        d = Data("trending", GiphyAPI.params)
        data = d.get_data()
        if s:
            click.echo(data)
        return data

    @gif.command()
    @click.argument('q')
    @click.option('-s', is_flag=True)
    def search(q, s):
        print("search subcommand called!")
        self.params['q'] = q
        d = Data("search", GiphyAPI.params)
        data = d.get_data()
        if s:
            click.echo(data)
        return data
    
if __name__ == "__main__":
    g = GiphyAPI()
    g.gif()
