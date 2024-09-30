import pytest
from gendiff.differences.gendiff import generate_diff

with_links_path = 'tests/fixtures/correct_answer_flat.txt'
with open(with_links_path, encoding='utf8') as f:
    correct_answer = f.read()


@pytest.fixture
def file1_json_path():
    return 'tests/fixtures/file1.json'


@pytest.fixture
def file2_json_path():
    return 'tests/fixtures/file2.json'


@pytest.fixture
def file1_yaml_path():
    return 'tests/fixtures/file1.yml'


@pytest.fixture
def file2_yaml_path():
    return 'tests/fixtures/file2.yml'


def test_json(file1_json_path, file2_json_path):
    generator = generate_diff(file1_json_path, file2_json_path)
    assert generator == correct_answer
    assert isinstance(generator, str)
    assert (': False\n' not in generator
            or ': True\n' not in generator)


def test_yaml(file1_yaml_path, file2_yaml_path):
    generator = generate_diff(file1_yaml_path, file2_yaml_path)
    assert generator == correct_answer
    assert isinstance(generator, str)
    assert (': False\n' not in generator
            or ': True\n' not in generator)

    file1_yaml_path = file1_yaml_path.replace('.yml', '.yaml')
    file2_yaml_path = file2_yaml_path.replace('.yml', '.yaml')

    generator = generate_diff(file1_yaml_path, file2_yaml_path)
    assert generator == correct_answer
    assert isinstance(generator, str)
    assert (': False\n' not in generator
            or ': True\n' not in generator)
