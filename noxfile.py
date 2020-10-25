import nox


@nox.session(python=["3.8"])
def tests(session):
    session.run("poetry", "install", external=True)
    session.run("pytest", "--cov")
    session..run("pytest", *args)
    # this enables user to pass additional arguments to pytest
    # now, you can run a specific test module inside the environments:
    # nox -- tests/test_console.py
