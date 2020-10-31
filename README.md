PyTemplate
==========

My python3 project template.
[Documention](https://tkhshtsh0917.github.io/pytemplate/)


[![Python3 version][shield-python3]](#)
[![Poetry version][shield-poetry]](#)
[![Coverage report][codecov]](#)
[![CI status][pytest-ci]](#)
[![Licensed][shield-license]](#)


Table of Contents
-----------------

  * [Requirements](#requirements)
  * [Usage](#usage)
  * [Contribution](#contribution)
  * [License](#license)


Requirements
------------

PyTemplate requires the following to run:

  * [Python3][python3] >= 3.9.0
  * [Poetry][poetry] >= 1.1.4


Usage
-----

```sh
git clone https://github.com/tkhshtsh0917/pytemplate.git

cd pytemplate

poetry install
```


## Caution

This project is managed using `poetry`.
Therefore, do not use the `pip install` command when installing external libraries.
In that case, please use the `poetry add` or `poetry add -D` command.


Contribution
------------

To contribute to this project, clone this repogitory locally and commit your code on a separate branch. 
Please write unit tests for your code, and run the linter before opening a pull-request.

```sh
pytest .  # Run all unit tests written in `pytest`.
pylint .  # Run the linter (`pylint`).
```

You can find more detail in our [contributing guide](/.github/CONTRIBUTING.md).


License
-------

Copyright &copy; 2020, Toshinori Takahashi


[python3]:        https://www.python.org
[poetry]:         https://python-poetry.org
[shield-python3]: https://img.shields.io/badge/Python3-v.3.9.0-blue
[shield-poetry]:  https://img.shields.io/badge/Poetry-v.1.1.4-blue
[codecov]:        https://codecov.io/gh/tkhshtsh0917/pytemplate/branch/main/graph/badge.svg?token=CF1Q6ANFPD
[pytest-ci]:      https://github.com/tkhshtsh0917/pytemplate/workflows/Pytest-CI/badge.svg
[shield-license]: https://img.shields.io/github/license/tkhshtsh0917/pytemplate