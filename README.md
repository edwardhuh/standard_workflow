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
