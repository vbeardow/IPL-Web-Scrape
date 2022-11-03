setup:
	pyenv local 3.10.8
	pre-commit install
	poetry shell

run:
	poetry run python blackjack/game.py

test:
	poetry run pytest

test-cov:
	pytest --cov=blackjack tests

clean:
	rm -rf __pycache__