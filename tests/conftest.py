"""
conftest
"""
import pytest


@pytest.fixture
def create_tmpfile(tmpdir, scope="session"):
    """
    create_tmpfile

    Args:
        tmpdir (fixture): Temporary directory path (/tmp).
        scope (str, optional): This fixture function's scope, defaults to "session".

    Yields:
        str: The path to created filepath.
    """
    tmpfile = tmpdir.join("numbers.txt")

    with tmpfile.open("w") as file:
        _ = [file.write("{}\n".format(n)) for n in [2, 5, 4, 3, 1]]
    yield str(tmpfile)

    tmpfile.remove()
