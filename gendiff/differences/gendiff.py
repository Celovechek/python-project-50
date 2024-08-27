from .tools import to_dict, build_diff, stylish


def generate_diff(f1: str, f2: str) -> str:
    '''Generating of difference for 2 files'''
    file1 = to_dict(f1)
    file2 = to_dict(f2)
    diff = build_diff(file1, file2)
    return f"{{\n{stylish(diff)}\n}}"
