import pytest
from hexlet_code.gendiff import generate_diff

@pytest.fixture
def file1_path():
    return 'tests/fixtures/file1.json'

@pytest.fixture
def file2_path():
    return 'tests/fixtures/file2.json'

def test_generate_diff_plain(file1_path, file2_path):
    expected_output = (
        "Property 'common.follow' was added with value: false\n"
        "Property 'common.setting2' was removed\n"
        "Property 'common.setting3' was updated. From true to none\n"  
        "Property 'common.setting4' was added with value: 'blah blah'\n"
        "Property 'common.setting5' was added with value: [complex value]\n"
        "Property 'common.setting6.doge.wow' was updated. From '' to 'so much'\n"
        "Property 'common.setting6.ops' was added with value: 'vops'\n"
        "Property 'group1.baz' was updated. From 'bas' to 'bars'\n"
        "Property 'group1.nest' was updated. From [complex value] to 'str'\n"
        "Property 'group2' was removed\n"
        "Property 'group3' was added with value: [complex value]"
)


    result = generate_diff(file1_path, file2_path, 'plain')
    assert result == expected_output
