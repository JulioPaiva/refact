requirements-dev:
	@pip install -U pip
	@pip install -r requirements/base.txt

run-ex1:
	@python example_01/backend.py

test:
	@pytest