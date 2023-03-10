import json


def generate_diff(file1, file2):
    data1 = json.load(open(file1.json))
    data2 = json.load(open(file2.json))

    diff = {}
    keys1 = set(data1.keys())
    keys2 = set(data2.keys())
    common_keys = keys1.intersection(keys2)

    for key in common_keys:
        if data1[key] == data2[key]:
            diff[key] = (' ', data1[key])
        else:
            diff[key] = ('-', data1[key])
            diff[key] = ('+', data2[key])

    for key in keys1 - common_keys:
        diff[key] = ('-', data1[key])

    for key in keys2 - common_keys:
        diff[key] = ('+', data2[key])

    lines = []
    for key, (prefix, value) in sorted(diff.items()):
        lines.append(f'{prefix} {key}: {json.dumps(value)}')

    return '{\n' + '\n'.join(lines) + '\n}'
