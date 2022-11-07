setup:
	pyenv local 3.10.8
	pre-commit install
	poetry shell

extract:
	poetry run python extract.py

transform:
	poetry run python transform.py

load:
	poetry run python load.py

test:
	poetry run pytest

test-cov:
	#TODO

clean:
	rm -rf __pycache__