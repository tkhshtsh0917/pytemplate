#!/bin/bash

COMMIT_TEMPLATE=`git config commit.template`
if [ $COMMIT_TEMPLATE != '.github\\COMMIT_TEMPLATE\\.commit_template' ]; then
  git config --local commit.template .github\\COMMIT_TEMPLATE\\.commit_template
  echo "Updated commit message template."
fi

PRECOMMIT_MASTER_FILE='./.github/PRE_COMMIT_MASTER/pre-commit'
if [ -e $PRECOMMIT_MASTER_FILE ]; then
  diff -s $PRECOMMIT_MASTER_FILE ./.git/hooks/pre-commit > /dev/null 2>&1
  if [ $? -ne 0 ]; then
    cp $PRECOMMIT_MASTER_FILE ./.git/hooks/pre-commit
    echo "Updated pre-commit."
    echo "Pre-commit was not latest. Please run again." 1>&2
    exit 1
  fi
else
  echo "$PRECOMMIT_MASTER_FILE doesn't exist."
fi

poetry install
if [ $? -eq 0 ]; then
  echo "Project setup is complete."
fi
