# -*- coding: utf-8 -*-
"""
main
"""


from pytemplate.performance_upward.cythonic import prime_eratosthenes


def prime_search():
    """
    prime_search
    """

    primelist = prime_eratosthenes(1_000)
    print(primelist)


def main():
    """
    main
    """

    print("Hello, world")


if __name__ == "__main__":
    main()
