from api import GiphyAPI
import click

api = GiphyAPI()

class GiphyCLI:

    @click.group()
    @staticmethod
    def gif():
        print("hello from giphy cli!")

    @gif.command()
    @click.option('-s', is_flag=True)
    def trending(s):
        data = api.trending()
        if s:
            click.echo(data)
        return data

    @gif.command()
    @click.argument('q')
    @click.option('-s', is_flag=True)
    def search(q, s):
        data = api.search(q)
        if s:
            click.echo(data)
        return data

if __name__ == "__main__":
    g = GiphyCLI()
    g.gif()
