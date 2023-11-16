# from hexlet_code.diff_builder import build_diff
# from hexlet_code.parsers import parse


INDENT = '    '


def format_stylish(diff, depth=0):
    lines = []
    for key, (status, value) in diff.items():
        if status == 'nested':
            formatted_value = format_stylish(value, depth + 1)
            line = f"{INDENT * depth}    {key}: {formatted_value}"
        else:
            line = format_value(key, status, value, depth)
        lines.append(line)
    return '{\n' + '\n'.join(lines) + '\n' + INDENT * depth + '}'


def format_value(key, status, value, depth):
    if status == 'removed':
        prefix = f"{INDENT * depth}  - "
    elif status == 'added':
        prefix = f"{INDENT * depth}  + "
    else:  # 'unchanged' or 'changed'
        prefix = f"{INDENT * depth}    "

    if isinstance(value, tuple):
        old_val, new_val = value
        removed = f"{prefix}{key}: {format_simple_value(old_val, depth + 1)}"
        added = (f"{INDENT * depth}  + {key}: "
                 f"{format_simple_value(new_val, depth + 1)}")

        return f"{removed}\n{added}"
    else:
        return f"{prefix}{key}: {format_simple_value(value, depth + 1)}"


def format_simple_value(value, depth):
    if isinstance(value, dict):
        formatted_items = [
            f"{INDENT * (depth + 1)}{k}: {format_simple_value(v, depth + 1)}"
            for k, v in value.items()
        ]
        return '{\n' + '\n'.join(formatted_items) + '\n' + INDENT * depth + '}'
    return value
