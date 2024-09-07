def json_type(diff: dict, indent=4) -> str:
    def wrapper(value, space=0):
        if isinstance(value, dict):
            items = []
            for key, val in value.items():
                items.append(f'{wrapper(key)}: {wrapper(val, space + 1)}')
            inner = ', '.join(items)
            if indent:
                inner = ',\n'.join([f'{" " * indent * (space + 1)}{item}' for item in items])
                return f'{{\n{inner}\n{" " * indent * space}}}'
            return f'{{{inner}}}'

        elif isinstance(value, list):
            items = [wrapper(item, space + 1) for item in value]
            inner = ', '.join(items)
            if indent:
                inner = ',\n'.join([f'{" " * indent * (space + 1)}{item}' for item in items])
                return f'[\n{inner}\n{" " * indent * space}]'
            return f'[{inner}]'

        elif isinstance(value, str):
            return f'"{value}"'

        elif isinstance(value, bool):
            return 'true' if value else 'false'

        elif value is None:
            return 'null'

        else:
            return str(value)

    return wrapper(diff)
