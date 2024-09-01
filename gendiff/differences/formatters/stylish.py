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

    def wrapper(diff: dict, depth=0) -> str:
        lines = []
        space = '    ' * depth
        for key, value in sorted(diff.items()):

            diff_type = value.get('type')

            if diff_type == 'include':
                children = wrapper(value['children'], depth + 1)
                lines.append(f'{space}    {key}: {{\n{children}\n{space}    }}')
            elif diff_type == 'added':
                new_value = format_value(value['value'], depth + 1)
                lines.append(f'{space}  + {key}: {new_value}')
            elif diff_type == 'removed':
                old_value = format_value(value['value'], depth + 1)
                lines.append(f'{space}  - {key}: {old_value}')
            elif diff_type == 'changed dict to not dict':
                children = wrapper(value['old_value'], depth + 1)
                lines.append(f'{space}  - {key}: {{\n{children}\n{space}    }}')
                new_value = format_value(value['new_value'], depth + 1)
                lines.append(f'{space}  + {key}: {new_value}')
            elif diff_type == 'changed not dict to dict':
                old_value = format_value(value['old_value'], depth + 1)
                lines.append(f'{space}  - {key}: {old_value}')
                children = wrapper(value['new_value'], depth + 1)
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
                children = wrapper(value['children'], depth + 1)
                lines.append(f'{space}  + {key}: {{\n{children}\n{space}    }}')
            elif diff_type == 'removed dict':
                children = wrapper(value['children'], depth + 1)
                lines.append(f'{space}  - {key}: {{\n{children}\n{space}    }}')
        return '\n'.join(lines)
    return f"{{\n{wrapper(diff, depth)}\n}}"
