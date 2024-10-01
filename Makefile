install: #installs dependencies in the directory .venv
	poetry install

brain-games: #launches brain_games.py
	poetry run brain-games

build: #building a package
	poetry build

publish: #publishing a package
	poetry publish --dry-run

package-install: #installing the package
	python3 -m pip install --user dist/*.whl

package-reinstall: #reinstalling the package
	python3 -m pip install --user --force-reinstall dist/*.whl

lint: #checking the linter
	poetry run flake8 gendiff

gendiff:
	poetry run gendiff
