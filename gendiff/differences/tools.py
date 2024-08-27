import json
import yaml


def to_dict(file_path: str) -> dict:
    '''A function for conversion .json and .yml files in dict format'''
    if file_path[-5:] == '.json':
        return json.load(open(file_path))
    elif file_path[-4:] == '.yml':
        with open(file_path) as fp:
            return yaml.load(fp, Loader=yaml.FullLoader)


def build_diff(dict1: dict, dict2: dict) -> dict:
    '''Creating of diff dict'''
    diff = {}
    river = sorted(set(dict1.keys()).union(dict2.keys()))
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


def format_value(value, depth: int) -> str:
    '''Creating formating'''

    indent = '    ' * depth

    if isinstance(value, dict):
        lines = []
        for key, val in value.items():
            lines.append(f'{indent}{key}: {format_value(val, depth + 1)}')
        formatted_dict = '\n'.join(lines)
        return f'{{\n{formatted_dict}\n{indent[:-4]}}}'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    else:
        return str(value)


def stylish(diff: dict, depth=0) -> str:
    '''Styling of diff'''

    lines = []
    space = '    ' * depth

    for key, value in sorted(diff.items()):

        diff_type = value.get('type')

        if diff_type == 'include':
            children = stylish(value['children'], depth + 1)
            lines.append(f'{space}    {key}: {{\n{children}\n{space}    }}')
        elif diff_type == 'added':
            new_value = format_value(value['value'], depth + 1)
            lines.append(f'{space}  + {key}: {new_value}')
        elif diff_type == 'removed':
            old_value = format_value(value['value'], depth + 1)
            lines.append(f'{space}  - {key}: {old_value}')
        elif diff_type == 'changed dict to not dict':
            children = stylish(value['old_value'], depth + 1)
            lines.append(f'{space}  - {key}: {{\n{children}\n{space}    }}')
            new_value = format_value(value['new_value'], depth + 1)
            lines.append(f'{space}  + {key}: {new_value}')
        elif diff_type == 'changed not dict to dict':
            old_value = format_value(value['old_value'], depth + 1)
            lines.append(f'{space}  - {key}: {old_value}')
            children = stylish(value['new_value'], depth + 1)
            lines.append(f'{space}  + {key}: {{\n{children}\n{space}    }}')
        elif diff_type == 'changed not dict to not dict':
            old_value = format_value(value['old_value'], depth + 1)
            new_value = format_value(value['new_value'], depth + 1)
            lines.append(f'{space}  - {key}: {old_value}')
            lines.append(f'{space}  + {key}: {new_value}')
        elif diff_type == 'unchanged':
            unchanged_value = format_value(value['value'], depth + 1)
            lines.append(f'{space}    {key}: {unchanged_value}')
        elif diff_type == 'added dict':
            children = stylish(value['children'], depth + 1)
            lines.append(f'{space}  + {key}: {{\n{children}\n{space}    }}')
        elif diff_type == 'removed dict':
            children = stylish(value['children'], depth + 1)
            lines.append(f'{space}  - {key}: {{\n{children}\n{space}    }}')
    return '\n'.join(lines)
