install: #устанавливает зависимости в директорию .venv
	poetry install

brain-games: #запускает brain_games.py
	poetry run brain-games

build: #сборка пакета
	poetry build

publish: #публикация пакета
	poetry publish --dry-run

package-install: #установка пакета
	python3 -m pip install --user dist/*.whl

package-reinstall: #переустановка пакета
	python3 -m pip install --user --force-reinstall dist/*.whl

lint: #провера линтера
	poetry run flake8 brain_games

gendiff:
	poetry run gendiff
