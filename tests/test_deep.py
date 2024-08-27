import pytest
from gendiff.differences.gendiff import generate_diff

correct_answer = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''

file1_json_path = 'tests/fixtures/file1_deep.json'
file2_json_path = 'tests/fixtures/file2_deep.json'
file1_yaml_path = 'tests/fixtures/file1_deep.yml'
file2_yaml_path = 'tests/fixtures/file2_deep.yml'

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
