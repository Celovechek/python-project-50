import pytest
from gendiff.differences.gendiff import generate_diff

with_links_path = 'tests/fixtures/correct_answer_json_type.txt'
with open(with_links_path, encoding='utf8') as f:
    correct_answer = f.read()


@pytest.fixture
def file1_json_path():
    return 'tests/fixtures/file1_deep.json'


@pytest.fixture
def file2_json_path():
    return 'tests/fixtures/file2_deep.json'


@pytest.fixture
def file1_yaml_path():
    return 'tests/fixtures/file1_deep.yml'


@pytest.fixture
def file2_yaml_path():
    return 'tests/fixtures/file2_deep.yml'


def test_json(file1_json_path, file2_json_path):
    assert generate_diff(file1_json_path, file2_json_path, 'json') == correct_answer
    assert isinstance(generate_diff(file1_json_path, file2_json_path, 'json'), str)
    assert (': False\n' not in generate_diff(file1_json_path, file2_json_path, 'json')
            or ': True\n' not in generate_diff(file1_json_path, file2_json_path, 'json'))


def test_yaml(file1_yaml_path, file2_yaml_path):
    assert generate_diff(file1_yaml_path, file2_yaml_path, 'json') == correct_answer
    assert isinstance(generate_diff(file1_yaml_path, file2_yaml_path, 'json'), str)
    assert (': False\n' not in generate_diff(file1_yaml_path, file2_yaml_path, 'json')
            or ': True\n' not in generate_diff(file1_yaml_path, file2_yaml_path, 'json'))

    file1_yaml_path = file1_yaml_path.replace('.yml', '.yaml')
    file2_yaml_path = file2_yaml_path.replace('.yml', '.yaml')

    assert generate_diff(file1_yaml_path, file2_yaml_path, 'json') == correct_answer
    assert isinstance(generate_diff(file1_yaml_path, file2_yaml_path, 'json'), str)
    assert (': False\n' not in generate_diff(file1_yaml_path, file2_yaml_path, 'json')
            or ': True\n' not in generate_diff(file1_yaml_path, file2_yaml_path, 'json'))
