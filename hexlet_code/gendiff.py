import os
import argparse
from hexlet_code.parsers import parse


def to_string(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value

def generate_diff(file_path1, file_path2):
    format1 = os.path.splitext(file_path1)[1][1:]
    format2 = os.path.splitext(file_path2)[1][1:]

    with open(file_path1) as file1, open(file_path2) as file2:
        file1_data = parse(file1.read(), format1)
        file2_data = parse(file2.read(), format2)

    diff = []
    all_keys = sorted(file1_data.keys() | file2_data.keys())

    for key in all_keys:
        if key in file1_data and key not in file2_data:
            diff.append(f"  - {key}: {to_string(file1_data[key])}")
        elif key not in file1_data and key in file2_data:
            diff.append(f"  + {key}: {to_string(file2_data[key])}")
        elif file1_data[key] == file2_data[key]:
            diff.append(f"    {key}: {to_string(file1_data[key])}")
        else:
            diff.append(f"  - {key}: {to_string(file1_data[key])}")
            diff.append(f"  + {key}: {to_string(file2_data[key])}")

    return '{\n' + '\n'.join(diff) + '\n}'



def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str, help='first configuration file')
    parser.add_argument('second_file', type=str,
                        help='second configuration file')
    parser.add_argument('-f', '--format', help='set format of output',
                        default='stylish')

    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()