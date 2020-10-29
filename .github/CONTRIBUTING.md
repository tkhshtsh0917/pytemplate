
# Contributing Guideline


## Pull Request Process

We use [GitHub flow](https://guides.github.com/introduction/flow/index.html), so all code changes happen through pull requests.

  1. Create your branch from `main`.
  2. If you've added code that should be tested, add tests.
  3. If you've changed APIs, update the documentation.
  4. Ensure the test suite passes.
  5. Make sure your code lints.
  6. Issue that pull request!


## Report bugs using GitHub's [issues](https://github.com/tkhshtsh0917/pytemplate/issues)

We use GitHub issues to track public bugs.<br>
Report a bug by [opening a new issue](https://github.com/tkhshtsh0917/pytemplate/issues/new) according to the [template](/ISSUE_TEMPLATE).


## Use a consistent coding style

  * This project will comply with [PEP8](https://www.python.org/dev/peps/pep-0008/).<br>To achieve this, use [`pylint`](https://www.pylint.org/) as a linter, [`black`](https://black.readthedocs.io/en/stable/) and [`isort`](https://pycqa.github.io/isort/) as a formatter.
  * [Type Hints](https://docs.python.org/3/library/typing.html) is required for this project.<br>To achieve this, use [`mypy`](http://mypy-lang.org/).
  * Documentation comments (`docstring`) must be completed in accordance with [Google Style](https://github.com/google/styleguide/blob/gh-pages/pyguide.md).<br>Automatically generate HTML documentation using [`sphinx`](https://www.sphinx-doc.org/en/master/) from documentation comments.
