import pytest
from unittest.mock import patch

from parsers import parse_args


class TestParseArgs:
    """Тесты для парсинга аргументов."""
    
    @patch('sys.argv', ['main.py', '--file', 'test.log', '--report', 'average'])
    def test_parse_args_basic(self):
        """Тест базового парсинга аргументов."""
        files, report, date = parse_args()
        assert files == ['test.log']
        assert report == 'average'
        assert date is None
    
    @patch('sys.argv', ['main.py', '--file', 'test1.log', 'test2.log', '--date', '2025-06-22'])
    def test_parse_args_multiple_files_with_date(self):
        """Тест парсинга с несколькими файлами и датой."""
        files, report, date = parse_args()
        assert files == ['test1.log', 'test2.log']
        assert report == 'average'  # значение по умолчанию
        assert date == '2025-06-22' 