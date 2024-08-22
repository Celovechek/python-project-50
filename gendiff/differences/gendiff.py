from .tools import to_dict


def generate_diff(f1: str, f2: str) -> str:
    file1 = to_dict(f1)
    file2 = to_dict(f2)
    file1_keys = sorted(file1.keys())
    file2_keys = sorted(file2.keys())
    river = sorted(set(file1_keys + file2_keys))
    string = '{\n'
    for i in river:
        if i in file1_keys and i in file2_keys:
            if file1[i] == file2[i]:
                string += f'    {i}: {file1[i]}\n'
            else:
                string += f'  - {i}: {file1[i]}\n'
                string += f'  + {i}: {file2[i]}\n'
        elif i in file1_keys and i not in file2_keys:
            string += f'  - {i}: {file1[i]}\n'
        else:
            string += f'  + {i}: {file2[i]}\n'
    string += '}'
    return (string.replace(': False\n', ': false\n')
            .replace(': True\n', ': true\n'))
