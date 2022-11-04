setup:
	pyenv local 3.10.8
	pre-commit install
	poetry shell

run:
	poetry run python ipl_web_scrape/main.py

test:
	poetry run pytest

test-cov:
	#TODO

clean:
	rm -rf __pycache__