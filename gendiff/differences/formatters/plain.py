def format_value(value):
    '''Format value for plain output'''
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f"'{value}'"
    return str(value)


def plain(diff: dict, path=None) -> str:
    '''Plain format for diff'''
    lines = []
    update_message = "Property '{0}' was updated. From {1} to {2}"
    for key, value in sorted(diff.items()):
        property_path = f"{path}.{key}" if path else key
        diff_type = value.get('type')

        if diff_type == 'include':
            lines.append(plain(value['children'], property_path))
        elif diff_type == 'added':
            formatted_value = format_value(value['value'])
            lines.append(f"Property '{property_path}' was added with value: {formatted_value}")
        elif diff_type == 'removed':
            lines.append(f"Property '{property_path}' was removed")
        elif diff_type == 'changed dict to not dict':
            old_value = format_value(value['old_value'])
            new_value = format_value(value['new_value'])
            lines.append(update_message.format(property_path, old_value, new_value))
        elif diff_type == 'changed not dict to dict':
            old_value = format_value(value['old_value'])
            new_value = format_value(value['new_value'])
            lines.append(update_message.format(property_path, old_value, new_value))
        elif diff_type == 'changed not dict to not dict':
            old_value = format_value(value['old_value'])
            new_value = format_value(value['new_value'])
            lines.append(update_message.format(property_path, old_value, new_value))
        elif diff_type == 'added dict':
            formatted_value = format_value(value['children'])
            lines.append(f"Property '{property_path}' was added with value: {formatted_value}")
        elif diff_type == 'removed dict':
            lines.append(f"Property '{property_path}' was removed")
    return '\n'.join(lines)
