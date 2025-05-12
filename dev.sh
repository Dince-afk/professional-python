#!/usr/bin/env bash
echo "Running development server"

PYTHON_ENV=development nodemon --exec uv run main.py