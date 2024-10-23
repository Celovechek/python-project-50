import pytest
from gendiff.differences.gendiff import generate_diff


@pytest.fixture
def correct_answer_plain_path():
    return 'tests/fixtures/correct_answer_deep.txt'


@pytest.fixture
def correct_answer(correct_answer_plain_path):
    with open(correct_answer_plain_path, encoding='utf8') as file:
        return file.read()


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


@pytest.fixture
def unsupported_file1():
    return 'tests/fixtures/file1.txt'


@pytest.fixture
def unsupported_file2():
    return 'tests/fixtures/file2.txt'


@pytest.mark.parametrize("file1, file2", [
    ('tests/fixtures/file1_deep.json', 'tests/fixtures/file2_deep.json'),
    ('tests/fixtures/file1_deep.yml', 'tests/fixtures/file2_deep.yml'),
    ('tests/fixtures/file1_deep.yaml', 'tests/fixtures/file2_deep.yaml'),
])
def test_generate_diff(file1, file2, correct_answer):
    result = generate_diff(file1, file2)
    assert result == correct_answer
    assert isinstance(result, str)
    assert (': False\n' not in result and ': True\n' not in result)


def test_unsupported_extension(unsupported_file1, unsupported_file2):
    with pytest.raises(ValueError) as exc_info:
        generate_diff(unsupported_file1, unsupported_file2)

    assert str(exc_info.value) == "Unsupported extention"
