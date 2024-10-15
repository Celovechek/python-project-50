import json
import yaml


def open_yaml(file):
    return yaml.safe_load(file)


def open_json(file):
    return json.loads(file)


def to_dict(filepath):
    extention = filepath.split(".")[-1]
    func_mapper = dict(
        yaml=open_yaml,
        yml=open_yaml,
        json=open_json,
    )
    open_func = func_mapper.get(extention)
    if not open_func:
        raise ("Unsupported extention")
    with open(filepath, 'r', encoding='utf-8') as file:
        return open_func(file.read())


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
