"""
tasting
"""


def is_prime(num):
    """
    is_prime

    Args:
        num (int): Target value.

    Returns:
        bool: If arg is prime number, return True. Else, return False.
    """

    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False

    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2

    return True


def load_numbers_sorted(text):
    """
    load_numbers_sorted

    Args:
        text (str): The path to the input file.

    Returns:
        [int]: Value read from text.
    """
    numbers = []
    with open(text) as file:
        numbers = sorted(map(lambda num: int(num), file))

    return numbers


def fibonacci(num):
    """
    fibonacci

    Args:
        num (int): Output values number.
    """
    tmp1 = 0
    tmp2 = 1

    for _ in range(num):
        print(tmp2)

        tmp1, tmp2 = tmp2, tmp1 + tmp2


def send(message):
    """
    send

    Args:
        message (str): Message text.
    """
    result = receive(message)

    if result:
        print("Success")
    else:
        print("Failure")


def receive(message):
    """
    receive

    Args:
        message (str): Message text.

    Returns:
        bool: Communication status (always True).
    """
    print("Received: {}".format(message))
    return True
