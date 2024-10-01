import json
import yaml


def reader(file_path: str) -> tuple:
    '''Reads the file and returns its content and type'''
    if file_path.endswith('.json'):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read(), 'json'
    elif file_path.endswith(('.yml', '.yaml')):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read(), 'yaml'


def to_dict(file_path: str) -> dict:
    '''A function for conversion .json and .yml files in dict format'''
    file_content, file_type = reader(file_path)
    if file_type == 'json':
        return json.loads(file_content)
    elif file_type == 'yaml':
        return yaml.safe_load(file_content)


def build_diff(dict1: dict, dict2: dict) -> dict:
    '''Creating of diff dict'''
    diff = {}
    keys_1 = set(dict1.keys())
    keys_2 = dict2.keys()

    double_keys = keys_1.union(keys_2)
    river = sorted(double_keys)
    for key in river:
        if key not in dict2 and isinstance(dict1[key], dict):
            diff[key] = {
                'type': 'removed dict',
                'children': build_diff(dict1[key], dict1[key])
            }
        elif key not in dict1 and isinstance(dict2[key], dict):
            diff[key] = {
                'type': 'added dict',
                'children': build_diff(dict2[key], dict2[key])
            }
        elif key not in dict2:
            diff[key] = {'type': 'removed', 'value': dict1[key]}
        elif key not in dict1:
            diff[key] = {'type': 'added', 'value': dict2[key]}
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            diff[key] = {
                'type': 'include',
                'children': build_diff(dict1[key], dict2[key])
            }
        elif isinstance(dict1[key], dict) and not isinstance(dict2[key], dict):
            diff[key] = {
                'type': 'changed dict to not dict',
                'old_value': build_diff(dict1[key], dict1[key]),
                'new_value': dict2[key]
            }
        elif not isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            diff[key] = {
                'type': 'changed not dict to dict',
                'old_value': dict1[key],
                'new_value': build_diff(dict2[key], dict2[key])
            }
        elif dict1[key] != dict2[key]:
            diff[key] = {
                'type': 'changed not dict to not dict',
                'old_value': dict1[key],
                'new_value': dict2[key]
            }
        else:
            diff[key] = {'type': 'unchanged', 'value': dict1[key]}
    return diff
