PyTemplate
==========

My python3 project template.
[Documention](https://tkhshtsh0917.github.io/pytemplate/)


[![Windows icon][shield-windows]](#)
[![Apple icon][shield-mac]](#)
[![Ubuntu icon][shield-ubuntu]](#)
[![VSCode icon][shield-vscode]](#)
[![Python3 version][shield-python3]](#)
[![Poetry version][shield-poetry]](#)
[![CI status][pytest-ci]](#)


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
[shield-windows]: https://img.shields.io/badge/-Windows-0078D6.svg?logo=windows&style=flat
[shield-mac]:     https://img.shields.io/badge/-MacOS-FFFFFF.svg?logo=apple&style=flat
[shield-ubuntu]:  https://img.shields.io/badge/-Ubuntu-6F52B5.svg?logo=ubuntu&style=flat
[shield-vscode]:  https://img.shields.io/badge/-Visual%20Studio%20Code-007ACC.svg?logo=visual-studio-code&style=flat
[shield-python3]: https://img.shields.io/badge/Python3-3.7%20|%203.8%20|%203.9%20-blue?logo=python&style=flat
[shield-poetry]:  https://img.shields.io/badge/Poetry-1.1-blue
[pytest-ci]:      https://github.com/tkhshtsh0917/pytemplate/workflows/Pytest-CI/badge.svg
