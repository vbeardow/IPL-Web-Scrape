setup:
	pyenv local 3.10.8
	pre-commit install
	poetry shell

run:
	poetry run python extract.py

links:
	poetry run python extract_links.py

scores:
	poetry run python extract_scores.py

test:
	poetry run pytest

test-cov:
	#TODO

clean:
	rm -rf __pycache__