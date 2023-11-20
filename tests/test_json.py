from hexlet_code.gendiff import generate_diff
import json

def test_generate_diff_json(file1_path, file2_path):
    result = generate_diff(file1_path, file2_path, 'json')
    
    assert json.loads(result) is not None