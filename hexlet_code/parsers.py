import json
import yaml


def parse(data, file_format):
    if file_format == 'json':
        return json.loads(data)
    elif file_format in ['yaml', 'yml']:
        return yaml.safe_load(data)
    else:
        raise ValueError(f"Unsupported file format: {file_format}")
