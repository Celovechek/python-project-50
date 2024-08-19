import pytest
from gendiff.differences.gendiff import generate_diff

def test_json():
    assert (generate_diff('file1.json', 'file2.json')
== '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}''') # normal work
    assert type(generate_diff('file1.json', 'file2.json')) == str #string type
    assert (': False\n' not in generate_diff('file1.json', 'file2.json') or
            ': True\n' not in generate_diff('file1.json', 'file2.json')) #check true/false style

