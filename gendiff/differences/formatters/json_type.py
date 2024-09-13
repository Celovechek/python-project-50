import json


def json_type(diff: dict, indent=4) -> str:
    return json.dumps(diff, indent=indent)
