import click.testing
import pytest

from standard_workflow import console

# pytest fixture are simple functions declared with the pytest.fixture decorator. T
# test cases can use a test fixture by including a function parameter with the same name as the test fixture
@pytest.fixture
def runner():
    return click.testing.CliRunner()
    ## the testing.CliRunner can invoke the cli from within a test case!!!


def test_main_succeeds(runner):
    result = runner.invoke(console.main)
    assert result.exit_code == 0


# The below code has been simplified using a pytest fixture
# def test_main_succeeds():
#     runner = click.testing.CliRunner()
#     ## the testing.CliRunner can invoke the cli from within a test case!!!
#     result = runner.invoke(console.main)
#     assert result.exit_code == 0