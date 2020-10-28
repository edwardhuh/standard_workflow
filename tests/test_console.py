import click.testing
import pytest
import requests

from standard_workflow import console

# pytest fixture are simple functions declared with the pytest.fixture decorator. T
# test cases can use a test fixture by including a function parameter with the same name as the test fixture
@pytest.fixture
def runner():
    return click.testing.CliRunner()
    ## the testing.CliRunner can invoke the cli from within a test case!!!

# including a pytest fixture that adds a function parameter to test case
@pytest.fixture
def mock_requests_get(mocker):
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Lorem",
        "extract": "stuff stuff stuff",
    }
    return mock

@pytest.fixture
def mock_requests_get(mocker):
    return mocker.patch("requests.get")

def test_main_succeeds(runner, mock_requests_get):
    result = runner.invoke(console.main)
    assert result.exit_code == 0

def test_main_prints_title(runner, mock_requests_get):
    result = runner.invoke(console.main)
    assert "Lorem Ipsum" in result.output

def test_main_invokes_requests_get(runner, mock_requests_get):
    runner.invoke(console.main)
    assert mock_requests_get.called

def test_main_uses_en_wikipedia_org(runner, mock_requests_get):
    runner.invoke(console.main)
    args, _ = mock_requests_get.call_args
    assert "en.wikipedia.org" in args[0]

def test_main_fails_on_request_error(runner, mock_requests_get):
    mock_requests_get.side_effect = Exception("Boom")
    result = runner.invoke(console.main)
    assert result.exit_code == 1

@pytest.fixture
def mock_wikipedia_random_page(mocker):
    return mocker.patch("standard_workflow.wikipedia.random_page")


def test_main_uses_specified_language(runner, mock_wikipedia_random_page):
    runner.invoke(console.main, ["--language=pl"])
    mock_wikipedia_random_page.assert_called_with(language="pl")
