import pytest
from hexlet_code.gendiff import generate_diff


@pytest.fixture
def nested_file1_path():
    return 'tests/fixtures/file1.json'


@pytest.fixture
def nested_file2_path():
    return 'tests/fixtures/file2.json'


def test_generate_diff_nested(nested_file1_path, nested_file2_path):
    correct_result = '''{
    common: {
      + follow: False
        setting1: Value 1
      - setting2: 200
        setting3: True
      + setting3: None
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
                wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
        baz: bas
      + baz: bars
        foo: bar
        nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''

    result = generate_diff(nested_file1_path, nested_file2_path)
    assert result == correct_result
