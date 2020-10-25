# standard_workflow

I will be replicating the hypermodern python workflow as described by CLAUDIO JOLOWICZ in the following blog article:
https://cjolowicz.github.io/posts/hypermodern-python-01-setup/

This is a side project solely for my own edification. 

Notes to myself as I work my way through this project:
## Chapter 1: Setup
### TOML
TOML := Tom’s Obvious, Minimal Language
A data serialisation language designed to be minimal configuraation file format that's easy to read due to obvious semantics. Used as alternative to YAML and JSON as an unambigious hash table. 
The official github (https://github.com/toml-lang/toml)
But, my personal favorite is (https://learnxinyminutes.com/docs/toml/)

### src layout
The single biggest benefit seems to be testing.
Personally, as I do not know too much about testing atm, the most compelling reason is: Not having a separate `src` directory will force `setuptools` to put your project's root on `sys.path` -- with other junk.
** I will update `src`'s benefit to testing at a later date after understanding it better.

### naming in src layout
Use snake case for the package name, as opposed to the kebab case used for the repository name. So, I messed up this time, but note to self!

### registering `cli.py` on `pyproject.toml`:
```
[tool.poetry.scripts]
hypermodern-python = "hypermodern_python.console:main"
```
The above chunk needs to be included in the `pyproject.toml`, and the package reinstalled using 
```
poetry install
poetry run hypermodern-python #i.e repo name
```
to ensure that the package runs with the command line interface.

## Chapter 2: Testing
### __init__.py
Creating this empty folder serves to declare the test suite as a package.
This is not necessary, but mirroring the source layout seems to serve multiple benefits that will have to be explored further at a later date.

### click.testing.CliRunner()
Enables you to invoke cli inside a test.
Frequently used features of a test can be created into Fixtures

### Code Coverage
A measure of the degree to which the source code for your program is executed while running its test suite.
Implemented using `coverage.py`, which is introduced in https://coverage.readthedocs.io/en/coverage-5.3/
Code Coverage is often used to gauge the effectiveness of tests.

The blog instructs to download `pytest-cov` using:
```
poetry add --dev coverage[toml] pytest-cov
```
with the additional `[toml]` configuration. But, this does not seem to be necessary, as I was ablew to get the same result using just:
```
poetry add --dev pytest-cov
```
The author merely claims that having 100% code coverage is important, but does not give full explanation as to what the costs are of actually having less than 100% coverage.
So, I will heed his advice for this particular project, but will 

### nox
the tool automates testing in multiple Python environments
By default, Nox deletes and recreates virtualenvs every time it is run. This is usually fine for most projects and continuous integration environments as pip’s caching makes re-install rather quick.
But for any other scenario, you may want to consider using the following command for repeated reuse:
```
nox -r
```

