import os
import argparse
from hexlet_code.parsers import parse
from hexlet_code.diff_builder import build_diff
from hexlet_code.stylish import format_diff
from hexlet_code.plain import format_plain


def generate_diff(file_path1, file_path2, format_name='stylish'):
    format1 = os.path.splitext(file_path1)[1][1:]
    format2 = os.path.splitext(file_path2)[1][1:]

    with open(file_path1) as file1, open(file_path2) as file2:
        file1_data = parse(file1.read(), format1)
        file2_data = parse(file2.read(), format2)

    diff = build_diff(file1_data, file2_data)

    if format_name == 'stylish':
        return format_diff(diff)
    elif format_name == 'plain':
        return format_plain(diff)
    else:
        raise ValueError(f"Unknown format: {format_name}")


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str,
                        help='first configuration file')
    parser.add_argument('second_file', type=str,
                        help='second configuration file')
    parser.add_argument('-f', '--format',
                        help='set format of output', default='stylish')

    args = parser.parse_args()
    # formatter = choose_formatter(args.format)
    formatted_diff = generate_diff(args.first_file, args.second_file, args.format)
    print(formatted_diff)


if __name__ == '__main__':
    main()
