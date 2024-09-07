import pytest
import json
from gendiff.differences.gendiff import generate_diff
from gendiff.differences.tools import to_dict, build_diff

file1_json_path = 'tests/fixtures/file1_deep.json'
file2_json_path = 'tests/fixtures/file2_deep.json'
file1_yaml_path = 'tests/fixtures/file1_deep.yml'
file2_yaml_path = 'tests/fixtures/file2_deep.yml'

def correct_answer(file1, file2):
    return json.dumps(build_diff(to_dict(file1), to_dict(file2)), indent=4)

def test_json():
    assert (generate_diff(file1_json_path, file2_json_path, 'json')
            == correct_answer(file1_json_path, file2_json_path))  # normal work
    assert type(generate_diff(file1_json_path, file2_json_path, 'json')) == str #string type
    assert (': False\n' not in generate_diff(file1_json_path, file2_json_path, 'json') or
            ': True\n' not in generate_diff(file1_json_path, file2_json_path, 'json')) #check true/false styling


def test_yaml():
    assert (generate_diff(file1_yaml_path, file2_yaml_path, 'json')
            == correct_answer(file1_yaml_path, file2_yaml_path))  # normal work
    assert type(generate_diff(file1_yaml_path, file2_yaml_path, 'json')) == str  # string type
    assert (': False\n' not in generate_diff(file1_yaml_path, file2_yaml_path, 'json') or
            ': True\n' not in generate_diff(file1_yaml_path, file2_yaml_path, 'json'))  # check true/false styling
