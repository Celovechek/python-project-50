### Hexlet tests and linter status:
[![Actions Status](https://github.com/Celovechek/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Celovechek/python-project-50/actions)

## GitHub Actions badge
![Actions Status](https://github.com/Celovechek/python-project-50/actions/workflows/gendiff.yml/badge.svg)

## Badge codeclimate
[![Maintainability](https://api.codeclimate.com/v1/badges/58f4d6dbbd5ce58036ec/maintainability)](https://codeclimate.com/github/Celovechek/python-project-50/maintainability)

## Test Coverage Badge codeclimate
[![Test Coverage](https://api.codeclimate.com/v1/badges/58f4d6dbbd5ce58036ec/test_coverage)](https://codeclimate.com/github/Celovechek/python-project-50/test_coverage)

## Информация о запуске проекта
Для проверки версии Python необходимо выполнить команду:
```
python3 -m pip --version
```

При необходимости версию можно обновить командой:
```
python3 -m pip install --upgrade --user pip
```

## Инструкции по установке и запуску
1. Клонируйте репозиторий на свой компьютер.
```
git clone git@github.com:Celovechek/python-project-50.git
```
2. Для создания билда необходимо выполнить следующую команду:
```
make build
```
2. Для установки пакета необходимо выполнить одну из следующих команд:
```
make package-install
```
```
python3 -m pip install --user dist/*.whl
```

3. В случае, если небходимо переустановить пакет, можно выполнить одну из команд:
```
make package-reinstall
```
```
python3 -m pip install --user --force-reinstall dist/*.whl
```

## Аскинема с примером работы пакета с flat файлами .json
[![asciicast](https://asciinema.org/a/MBh3AdrOC55jdITsVmKpf04kS.svg)](https://asciinema.org/a/MBh3AdrOC55jdITsVmKpf04kS)

## Аскинема с примером работы пакета с deep файлами .json и .yml
[![asciicast](https://asciinema.org/a/a5MK4a9lsbbyhqAfX4Rn0zX9d.svg)](https://asciinema.org/a/a5MK4a9lsbbyhqAfX4Rn0zX9d)

## Аскинема с примером работы пакета с deep файлами .json и .yml c форматом вывода plain
[![asciicast](https://asciinema.org/a/9WgPMEjvQfl7KkWiiyewOeQ69.svg)](https://asciinema.org/a/9WgPMEjvQfl7KkWiiyewOeQ69)

## Аскинема с примером работы пакета с deep файлами .json и .yml c форматом вывода json
[![asciicast](https://asciinema.org/a/d8pQOS99np9UYs4bjctNTw5AD.svg)](https://asciinema.org/a/d8pQOS99np9UYs4bjctNTw5AD)
