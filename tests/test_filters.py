import pytest

from filters import filter_by_date


class TestFilters:
    """Тесты для фильтрации."""
    
    def test_filter_by_date_no_date(self):
        """Тест фильтрации без указания даты."""
        data = [
            {'@timestamp': '2025-06-22T10:00:00+00:00', 'url': '/api/test'},
            {'@timestamp': '2025-06-23T10:00:00+00:00', 'url': '/api/test2'}
        ]
        result = filter_by_date(data, None)
        assert result == data
    
    def test_filter_by_date_specific_date(self):
        """Тест фильтрации по конкретной дате."""
        data = [
            {'@timestamp': '2025-06-22T10:00:00+00:00', 'url': '/api/test1'},
            {'@timestamp': '2025-06-23T10:00:00+00:00', 'url': '/api/test2'},
            {'@timestamp': '2025-06-22T15:00:00+00:00', 'url': '/api/test3'}
        ]
        result = filter_by_date(data, '2025-06-22')
        assert len(result) == 2
        urls = [item['url'] for item in result]
        assert '/api/test1' in urls
        assert '/api/test3' in urls
        assert '/api/test2' not in urls
    
    def test_filter_by_date_invalid_format(self):
        """Тест обработки некорректного формата даты."""
        data = [{'@timestamp': '2025-06-22T10:00:00+00:00', 'url': '/api/test'}]
        with pytest.raises(SystemExit):
            filter_by_date(data, 'invalid-date') 