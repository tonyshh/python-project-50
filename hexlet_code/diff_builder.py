def build_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    diff = {}

    for key in keys:
        if key not in data2:
            diff[key] = ('removed', data1[key])
        elif key not in data1:
            diff[key] = ('added', data2[key])
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = ('nested', build_diff(data1[key], data2[key]))
        elif data1[key] == data2[key]:
            diff[key] = ('unchanged', data1[key])
        else:
            diff[key] = ('changed', (data1[key], data2[key]))

    return diff
