import pytest
import tempfile
import os

from file_reader import read_files


class TestFileReader:
    """Тесты для чтения файлов."""
    
    def test_read_files_success(self):
        """Тест успешного чтения файла."""
        test_data = [
            '{"url": "/api/test", "response_time": 0.1}',
            '{"url": "/api/test2", "response_time": 0.2}'
        ]
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write('\n'.join(test_data))
            temp_file = f.name
        
        try:
            result = read_files([temp_file])
            assert len(result) == 2
            assert result[0]['url'] == '/api/test'
            assert result[1]['url'] == '/api/test2'
        finally:
            os.unlink(temp_file)
    
    def test_read_files_file_not_found(self):
        """Тест обработки отсутствующего файла."""
        with pytest.raises(SystemExit):
            read_files(['nonexistent.log']) 