all: deps check test

deps:
	uv sync --locked
	uv run pre-commit install

check:
	uv run pre-commit run --all-files

test:
	uv run pytest

cov:
	uv run coverage erase \
	&& uv run coverage run --source=. --branch -m pytest \
	&& uv run coverage report --show-missing --skip-covered

clean:
	rm -rf .venv/ .*_cache/ .coverage *.egg-info/ dist/
	find -type d -name '__pycache__' -exec rm -rf {} +
