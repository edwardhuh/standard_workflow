import click
import textwrap

from . import __version__, wikipedia

# API specification refactired to wikipedia.py
# API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
@click.option(
    "--language",
    "-l",
    default="en",
    help="Language edition of Wikipedia",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main():
	"""The hypermodern Python project."""
	# with requests.get(API_URL) as response:
	# 	response.raise_for_status()
	# 	data = response.json()

	data = wikipedia.random_page()

	title = data["title"]
	extract = data["extract"]

	click.secho(title, fg='green', bg='white') #click.secho is a combination of echo() and style()
	click.echo(textwrap.fill(extract))