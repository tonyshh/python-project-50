def format_plain(diff, parent=''):
    lines = []
    for key, (status, value) in sorted(diff.items()):
        if status == 'nested':
            lines.append(format_plain(value, f'{parent}{key}.'))
        else:
            lines.append(format_change(key, status, value, parent))
    return '\n'.join(line for line in lines if line)

def format_change(key, status, value, parent):
    property_name = f"'{parent}{key}'"
    if status == 'added':
        formatted_value = format_value(value)
        return f"Property {property_name} was added with value: {formatted_value}"
    elif status == 'removed':
        return f"Property {property_name} was removed"
    elif status == 'changed':
        old_value, new_value = value
        formatted_old_value = format_value(old_value)
        formatted_new_value = format_value(new_value)
        return f"Property {property_name} was updated. From {formatted_old_value} to {formatted_new_value}"

def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool) or value is None:
        return str(value).lower()
    if isinstance(value, str):
        return f"'{value}'"
    return value