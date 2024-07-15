@echo off
coverage run --source=itb -m pytest
coverage report -m
coverage-badge -o coverage.svg -f
git add coverage.svg