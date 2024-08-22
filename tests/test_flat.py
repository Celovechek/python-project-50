import pytest
from gendiff.differences.gendiff import generate_diff

correct_answer = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
file1_json_path = 'tests/fixtures/file1.json'
file2_json_path = 'tests/fixtures/file2.json'
file1_yaml_path = 'tests/fixtures/file1.yml'
file2_yaml_path = 'tests/fixtures/file2.yml'

def test_json():
    assert (generate_diff(file1_json_path, file2_json_path)
            == correct_answer)  # normal work
    assert type(generate_diff(file1_json_path, file2_json_path)) == str #string type
    assert (': False\n' not in generate_diff(file1_json_path, file2_json_path) or
            ': True\n' not in generate_diff(file1_json_path, file2_json_path)) #check true/false styling


def test_yaml():
    assert (generate_diff(file1_yaml_path, file2_yaml_path)
            == correct_answer)  # normal work
    assert type(generate_diff(file1_yaml_path, file2_yaml_path)) == str  # string type
    assert (': False\n' not in generate_diff(file1_yaml_path, file2_yaml_path) or
            ': True\n' not in generate_diff(file1_yaml_path, file2_yaml_path))  # check true/false styling
