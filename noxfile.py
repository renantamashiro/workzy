import tempfile

import nox


nox.options.session = "lint", "tests"


def install_with_constraints(session, *args, **kwargs) -> None:
    """Create a temporary file and install dependencies managed by Poetry."""
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            f"--output={requirements.name}",
            external=True,
        )
        session.install(f"--constraint={requirements.name}", *args, **kwargs)


@nox.session(python=["3.8"])
def tests(session) -> None:
    """Run the test suite."""
    args = session.posargs or ["--cov", "-m", "not e2e"]
    session.run("poetry", "install", "--no-dev", external=True)
    install_with_constraints(session, "coverage[toml]", "pytest", "pytest-cov")
    session.run("pytest", *args)


locations = "workzy", "tests", "noxfile.py", "docs/conf.py"


@nox.session(python=["3.8"])
def lint(session) -> None:
    """Flake8 lint"""
    args = session.posargs or locations
    install_with_constraints(
        session,
        "flake8",
        "flake8-black",
        "flake8-import-order",
    )
    session.run("flake8", *args)


@nox.session(python=["3.8"])
def black(session) -> None:
    """Black code formatter"""
    args = session.posargs or locations
    install_with_constraints(session, "black")
    session.run("black", *args)


@nox.session(python=["3.8"])
def docs(session) -> None:
    """Build documentation."""
    session.run("poetry", "install", "--no-dev", external=True)
    install_with_constraints(session, "sphinx", "sphinx-autodoc-typehints")
    session.run("sphinx-build", "docs", "docs/_build")
