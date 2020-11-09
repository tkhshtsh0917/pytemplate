#!/bin/bash

COMMIT_TEMPLATE=`git config commit.template`
if [ $COMMIT_TEMPLATE != '.github\\COMMIT_TEMPLATE\\.commit_template' ]; then
  git config --local commit.template .github\\COMMIT_TEMPLATE\\.commit_template
  echo "Updated commit message template."
fi

poetry install
poetry run pre-commit install
if [ $? -eq 0 ]; then
  echo "Project setup is complete."
fi
