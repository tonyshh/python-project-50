import pytest
from hexlet_code.gendiff import generate_diff


@pytest.fixture
def file1_path():
    return 'tests/fixtures/file1.json'


@pytest.fixture
def file2_path():
    return 'tests/fixtures/file2.json'


def test_generate_diff(file1_path, file2_path):
    correct_result = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

    result = generate_diff(file1_path, file2_path)
    assert result == correct_result


@pytest.fixture
def file1_yaml_path():
    return 'tests/fixtures/file1.yaml'

@pytest.fixture
def file2_yaml_path():
    return 'tests/fixtures/file2.yaml'

def test_generate_diff_yaml(file1_yaml_path, file2_yaml_path):
    correct_result_yaml = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

    result_yaml = generate_diff(file1_yaml_path, file2_yaml_path)
    assert result_yaml == correct_result_yaml