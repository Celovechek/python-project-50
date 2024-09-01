import pytest
from gendiff.differences.gendiff import generate_diff

correct_answer = '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''

file1_json_path = 'tests/fixtures/file1_deep.json'
file2_json_path = 'tests/fixtures/file2_deep.json'
file1_yaml_path = 'tests/fixtures/file1_deep.yml'
file2_yaml_path = 'tests/fixtures/file2_deep.yml'

def test_json():
    assert (generate_diff(file1_json_path, file2_json_path, 'plain')
            == correct_answer)  # normal work
    assert type(generate_diff(file1_json_path, file2_json_path, 'plain')) == str #string type
    assert (': False\n' not in generate_diff(file1_json_path, file2_json_path, 'plain') or
            ': True\n' not in generate_diff(file1_json_path, file2_json_path, 'plain')) #check true/false styling


def test_yaml():
    assert (generate_diff(file1_yaml_path, file2_yaml_path, 'plain')
            == correct_answer)  # normal work
    assert type(generate_diff(file1_yaml_path, file2_yaml_path, 'plain')) == str  # string type
    assert (': False\n' not in generate_diff(file1_yaml_path, file2_yaml_path, 'plain') or
            ': True\n' not in generate_diff(file1_yaml_path, file2_yaml_path, 'plain'))  # check true/false styling
