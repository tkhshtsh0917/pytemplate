"""
test_pytemplate
"""
import pytest

import pytemplate.functions_for_pytest_sample.tasting
from pytemplate.functions_for_pytest_sample.tasting import (
    fibonacci,
    is_prime,
    load_numbers_sorted,
    send,
)


def test_is_prime_default():
    """
    test_is_prime_default
    """

    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(6)
    assert is_prime(7)
    assert not is_prime(8)
    assert not is_prime(9)
    assert not is_prime(10)


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (8, False),
        (9, False),
        (10, False),
    ],
)
def test_is_prime_parametrized(number, expected):
    """
    test_is_prime_parametrized

    Args:
        number (int): The parameter pattern to the is_prime function.
        expected (bool): This is the assumed result pattern of the test.
    """
    assert is_prime(number) == expected


def test_load_numbers_sorted_fixtured(create_tmpfile):
    """
    test_load_numbers_sorted_fixtured

    Args:
        create_tmpfile (fixture): The path to the input file, whose created by fixture function.
    """
    assert load_numbers_sorted(create_tmpfile) == [1, 2, 3, 4, 5]


def test_fibonacci_output_captured(capsys):
    """
    test_fibonacci_output_captured

    Args:
        capsys (fixture): Stdout / Stderr capturer.
    """
    fibonacci(5)
    output, _ = capsys.readouterr()

    assert output == ("1\n" "1\n" "2\n" "3\n" "5\n")


def test_send_with_mocker_communication_success(mocker, capsys):
    """
    test_send_with_mocker_communication_success

    Args:
        mocker (fixture): Mocker.
        capsys (fixture): Stdout / Stderr capturer.
    """
    receive = mocker.patch(
        "pytemplate.functions_for_pytest_sample.tasting.receive",
        return_value=True,
    )

    send("Hello, mock!")
    receive.assert_called_once_with("Hello, mock!")

    assert receive.call_args_list == [mocker.call("Hello, mock!")]

    output, _ = capsys.readouterr()
    assert output == "Success\n"


def test_send_with_mocker_communication_failure(mocker, capsys):
    """
    test_send_with_mocker_communication_failure

    Args:
        mocker (fixture): Mocker.
        capsys (fixture): Stdout / Stderr capturer.
    """
    receive = mocker.patch(
        "pytemplate.functions_for_pytest_sample.tasting.receive",
        return_value=False,
    )

    send("Hello, mock!")
    receive.assert_called_once_with("Hello, mock!")

    assert receive.call_args_list == [mocker.call("Hello, mock!")]

    output, _ = capsys.readouterr()
    assert output == "Failure\n"


def test_send_with_mocker_spy(mocker, capsys):
    """
    test_send_with_mocker_spy

    Args:
        mocker (fixture): Mocker.
        capsys (fixture): Stdout / Stderr capturer.
    """
    receive = mocker.spy(
        pytemplate.functions_for_pytest_sample.tasting, "receive"
    )

    send("Hello, mock!")
    receive.assert_called_once_with("Hello, mock!")

    assert receive.call_args_list == [mocker.call("Hello, mock!")]

    output, _ = capsys.readouterr()
    assert output == ("Received: Hello, mock!\n" "Success\n")
