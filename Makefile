setup:
	pyenv local 3.10.8
	pre-commit install
	poetry shell

run:
	# poetry run python TODO.py

test:
	poetry run pytest

test-cov:
	#TODO

clean:
	rm -rf __pycache__