SHELL := /bin/bash
.PHONY: test lint type docker

lint:
	ruff check .

type:
	mypy .

test:
	pytest -q --cov=app

docker:
	docker build -t healthapp-backend:dev .
	docker run --rm -p 8000:8000 healthapp-backend:dev
