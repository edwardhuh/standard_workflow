import click.testing
import pytest

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
# even in the mock fixture, you need to give it the proper return value.
	mock = mocker.patch("requests.get")
	mock.return_value.__enter__.return_value.json.return_value = {
		"title": "Lorem",
		"extract": "stuff stuff stuff",
	}
	return mock


def test_main_succeeds(runner, mock_requests_get):
    result = runner.invoke(console.main)
    assert result.exit_code == 0


# The below code has been simplified using a pytest fixture
# def test_main_succeeds():
#     runner = click.testing.CliRunner()
#     ## the testing.CliRunner can invoke the cli from within a test case!!!
#     result = runner.invoke(console.main)
#     assert result.exit_code == 0