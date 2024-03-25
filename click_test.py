import click
from click.testing import CliRunner

from cli import GiphyCLI

gCLI = GiphyCLI()
runner = CliRunner()

def test_trending_cli():
    result = runner.invoke(gCLI.trending)
    assert not result.exception
    assert "trending subcommand called!\n" in result.output

    result = runner.invoke(gCLI.trending, ['-s'])
    assert not result.exception
    assert "'msg: 'OK'" in result.output

    result = runner.invoke(gCLI.search, ['-l', 1, '-s'])
    assert not result.exception
    assert "'count': 1" in result.output
    
def test_serach_cli_argument():
    result = runner.invoke(gCLI.search, ['hi'])
    assert not result.exception
    assert "search subcommand called!\n" in result.output

    result = runner.invoke(gCLI.search, ['hi', '-s'])
    assert not result.exception
    assert "'msg: 'OK'" in result.output

    result = runner.invoke(gCLI.search, ['hi', '-l', 1, '-s'])
    assert not result.exception
    assert "'count': 1" in result.output
