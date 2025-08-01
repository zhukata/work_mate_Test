import pytest
import tempfile
import os

from file_reader import read_files
from filters import filter_by_date
from reports import AverageReportGenerator


class TestIntegration:
    """Интеграционные тесты."""
    
    def test_full_workflow(self):
        """Тест полного рабочего процесса."""
        test_data = [
            '{"url": "/api/test1", "response_time": 0.1, "@timestamp": "2025-06-22T10:00:00+00:00"}',
            '{"url": "/api/test1", "response_time": 0.2, "@timestamp": "2025-06-22T10:01:00+00:00"}',
            '{"url": "/api/test2", "response_time": 0.3, "@timestamp": "2025-06-23T10:00:00+00:00"}'
        ]
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write('\n'.join(test_data))
            temp_file = f.name
        
        try:
            # Читаем файл
            data = read_files([temp_file])
            assert len(data) == 3
            
            # Фильтруем по дате
            filtered_data = filter_by_date(data, '2025-06-22')
            assert len(filtered_data) == 2
            
            # Генерируем отчет
            generator = AverageReportGenerator()
            report = generator.generate(filtered_data)
            
            assert len(report) == 1
            assert report[0]['handler'] == '/api/test1'
            assert report[0]['total'] == 2
            assert report[0]['avg_response_time'] == 0.15
            
        finally:
            os.unlink(temp_file) 