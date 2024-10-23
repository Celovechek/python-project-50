import pytest
from gendiff.differences.gendiff import generate_diff


@pytest.fixture
def correct_answer_flat_path():
    return 'tests/fixtures/correct_answer_flat.txt'


@pytest.fixture
def correct_answer(correct_answer_flat_path):
    with open(correct_answer_flat_path, encoding='utf8') as f:
        return f.read()


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


@pytest.fixture
def unsupported_txt_file1():
    return 'tests/fixtures/file1.txt'


@pytest.fixture
def unsupported_txt_file2():
    return 'tests/fixtures/file2.txt'


@pytest.mark.parametrize("file1, file2", [
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json'),
    ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml'),
    ('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml'),
])
def test_generate_diff(file1, file2, correct_answer):
    result = generate_diff(file1, file2)
    assert result == correct_answer
    assert isinstance(result, str)


def test_unsupported_extension(unsupported_txt_file1, unsupported_txt_file2):
    with pytest.raises(ValueError) as exc_info:
        generate_diff(unsupported_txt_file1, unsupported_txt_file2, 'plain')
    assert str(exc_info.value) == "Unsupported extention"
