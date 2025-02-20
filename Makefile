.PHONY: fmt lint test build

fmt:
	@python -m pip -q install ruff black >/dev/null 2>&1 || true
	ruff check --fix . || true
	black . || true

lint:
	ruff check . || true

test:
	python -m pytest -q || true

build:
	python -m sidehustle build site

