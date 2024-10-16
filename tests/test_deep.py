import pytest
from gendiff.differences.gendiff import generate_diff


with_links_path = 'tests/fixtures/correct_answer_deep.txt'
with open(with_links_path, encoding='utf8') as f:
    correct_answer = f.read()


# @pytest.fixture
# def correct_answer_plain_path():
#     return 'tests/fixtures/correct_answer_deep.txt'
#
# @pytest.fixture
# def correct_answer(correct_answer_plain_path):
#     with open(correct_answer_plain_path) as file:
#         return file.read()


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


@pytest.mark.parametrize("file1, file2, correct_answer", [
    ('tests/fixtures/file1_deep.json', 'tests/fixtures/file2_deep.json', correct_answer),
    ('tests/fixtures/file1_deep.yml', 'tests/fixtures/file2_deep.yml', correct_answer),
    ('tests/fixtures/file1_deep.yaml', 'tests/fixtures/file2_deep.yaml', correct_answer),
])
def test_generate_diff(file1, file2, correct_answer):
    result = generate_diff(file1, file2)
    assert result == correct_answer
    assert isinstance(result, str)
    assert (': False\n' not in result or ': True\n' not in result)
