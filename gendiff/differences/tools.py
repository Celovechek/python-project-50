import json
import yaml


def to_dict(file_path: str) -> dict:
    if file_path[-5:] == '.json':
        return json.load(open(file_path))
    elif file_path[-4:] == '.yml':
        with open(file_path) as fp:
            return yaml.load(fp, Loader=yaml.FullLoader)
