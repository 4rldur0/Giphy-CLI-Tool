from click.testing import CliRunner

from giphy_tool_project2.cli import GiphyCLI

gCLI = GiphyCLI()
runner = CliRunner()


# Test for trending subcommand
def test_trending_cli():
    result = runner.invoke(gCLI.gif, ["trending"])
    assert not result.exception
    assert "trending subcommand called!\n" in result.output


# Test for option -p
def test_trending_cli_p():
    result = runner.invoke(gCLI.gif, ["trending", "-p"])
    assert not result.exception
    assert "'msg': 'OK'" in result.output


# Test for option -n
def test_trending_cli_n():
    result = runner.invoke(gCLI.gif, ["trending", "-n", 1, "-p"])
    assert not result.exception
    assert "Successfully executed" in result.output
    assert "'count': 1" in result.output


# Test for option -l
def test_trending_cli_l():
    result = runner.invoke(gCLI.gif, ["trending", "-ln", 3])
    assert not result.exception
    assert "**Trendings**" in result.output
    assert "[3]" in result.output


# Test for search subcommand
def test_serach_cli():
    result = runner.invoke(gCLI.gif, ["search", "hi"])
    assert not result.exception
    assert "search subcommand called!\n" in result.output


# Test for no argument
def test_search_cli_no_argument():
    result = runner.invoke(gCLI.gif, ["search"])
    assert result.exception
    assert "Error: Missing argument 'Q'." in result.output


# Test for option -p
def test_search_cli_p():
    result = runner.invoke(gCLI.gif, ["search", "hi", "-p"])
    assert not result.exception
    assert "'msg': 'OK'" in result.output


# Test for option -n
def test_search_cli_n():
    result = runner.invoke(gCLI.gif, ["search", "hi", "-n", 1, "-p"])
    assert not result.exception
    assert "Successfully executed" in result.output
    assert "'count': 1" in result.output


# Test for option -l
def test_search_cli_l():
    result = runner.invoke(gCLI.gif, ["search", "hi", "-ln", 3])
    assert not result.exception
    assert "**Search Results for" in result.output
    assert "[3]" in result.output
