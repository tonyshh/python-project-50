import os
import argparse
from hexlet_code.parsers import parse
from hexlet_code.diff_builder import build_diff
from hexlet_code.stylish import format_diff


def to_string(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


import os
import argparse
from hexlet_code.parsers import parse
from hexlet_code.diff_builder import build_diff
from hexlet_code.stylish import format_diff

def generate_diff(file_path1, file_path2):
    format1 = os.path.splitext(file_path1)[1][1:]
    format2 = os.path.splitext(file_path2)[1][1:]

    with open(file_path1) as file1, open(file_path2) as file2:
        file1_data = parse(file1.read(), format1)
        file2_data = parse(file2.read(), format2)

    diff = build_diff(file1_data, file2_data)
    formatted_diff = format_diff(diff)  # Форматирование диффа
    return formatted_diff

def choose_formatter(format_name):
    if format_name == 'stylish':
        return format_diff 
    raise ValueError(f"Unknown format: {format_name}")
    


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str, help='first configuration file')
    parser.add_argument('second_file', type=str, help='second configuration file')
    parser.add_argument('-f', '--format', help='set format of output', default='stylish')

    args = parser.parse_args()
    formatter = choose_formatter(args.format)  # Эта строка больше не нужна, если generate_diff возвращает готовую строку
    formatted_diff = generate_diff(args.first_file, args.second_file)
    print(formatted_diff)

if __name__ == '__main__':
    main()


if __name__ == '__main__':
    main()
