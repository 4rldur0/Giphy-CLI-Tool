import click

from giphy_tool_project2.api import GiphyAPI

api = GiphyAPI()


class GiphyCLI:

    @click.group()
    @staticmethod
    def gif():
        print("hello from giphy cli!")

    @gif.command()
    @click.option("-n", type=int, help="Set limitation")
    @click.option("-p", is_flag=True, help="Print out the entire response")
    @click.option("-l", is_flag=True, help="List of all the titles and URLs")
    def trending(n, p, l):
        api.trending(n)
        if api.status != "OK":
            print("Failed to execute trending subcommand")
            print("Status: ", api.status)
            return
        click.echo("Successfully executed")
        if p:
            click.echo(api.data)
        if l:
            click.echo("\n **Trendings**\n=================")
            for i in range(n):
                click.echo(f"[{i+1}] {api.titles[i]}")
                click.echo(api.urls[i])

    @gif.command()
    @click.argument("q")
    @click.option("-n", type=int, help="Set limitation")
    @click.option("-p", is_flag=True, help="Print out the entire response")
    @click.option("-l", is_flag=True, help="List of all the titles and URLs")
    def search(q, n, p, l):
        api.search(q, n)
        if api.status != "OK":
            print("Failed to execute trending subcommand")
            print("Status: ", api.status)
            return
        click.echo("Successfully executed")
        if p:
            click.echo(api.data)
        if l:
            click.echo(
                '\n **Search Results for "{q}"**\n==============================='
            )
            for i in range(n):
                click.echo(f"[{i+1}] {api.titles[i]}")
                click.echo(api.urls[i])


def main():
    g = GiphyCLI()
    g.gif()
