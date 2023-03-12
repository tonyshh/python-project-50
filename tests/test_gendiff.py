from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():
    '''
    Тест функции generate_diff
    '''
    file_path1 = '/home/tonysh/Мои файлы/Разработка/Hexlet_project_2/python-project-50/fixtures/file1.json'
    file_path2 = '/home/tonysh/Мои файлы/Разработка/Hexlet_project_2/python-project-50/fixtures/file2.json'
    format = 'plain'
    correct_result = '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''
    result = generate_diff(file_path1, file_path2, format)
    assert result == correct_result