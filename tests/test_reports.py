import pytest

from reports import (
    ReportGenerator, 
    AverageReportGenerator, 
    UserAgentReportGenerator, 
    get_report_generator
)


class TestReportGenerator:
    """Тесты для базового класса ReportGenerator."""
    
    def test_report_generator_abstract(self):
        """Тест что базовый класс абстрактный."""
        generator = ReportGenerator()
        with pytest.raises(NotImplementedError):
            generator.generate([])


class TestAverageReportGenerator:
    """Тесты для AverageReportGenerator."""
    
    def test_generate_basic_report(self):
        """Тест базовой генерации отчета."""
        data = [
            {'url': '/api/test1', 'response_time': 0.1},
            {'url': '/api/test1', 'response_time': 0.2},
            {'url': '/api/test2', 'response_time': 0.3}
        ]
        generator = AverageReportGenerator()
        result = generator.generate(data)
        
        assert len(result) == 2

        result.sort(key=lambda x: x['handler'])
        
        assert result[0]['handler'] == '/api/test1'
        assert result[0]['total'] == 2
        assert result[0]['avg_response_time'] == 0.15
        
        assert result[1]['handler'] == '/api/test2'
        assert result[1]['total'] == 1
        assert result[1]['avg_response_time'] == 0.3


class TestUserAgentReportGenerator:
    """Тесты для UserAgentReportGenerator."""
    
    def test_generate_basic_report(self):
        """Тест базовой генерации отчета по User-Agent."""
        data = [
            {'http_user_agent': 'Chrome/91.0', 'url': '/api/test1'},
            {'http_user_agent': 'Chrome/91.0', 'url': '/api/test2'},
            {'http_user_agent': 'Firefox/89.0', 'url': '/api/test3'}
        ]
        generator = UserAgentReportGenerator()
        result = generator.generate(data)
        
        assert len(result) == 2

        result.sort(key=lambda x: x['user_agent'])
        
        assert result[0]['user_agent'] == 'Chrome/91.0'
        assert result[0]['count'] == 2
        
        assert result[1]['user_agent'] == 'Firefox/89.0'
        assert result[1]['count'] == 1


class TestGetReportGenerator:
    """Тесты для функции get_report_generator."""
    
    def test_get_average_generator(self):
        """Тест получения генератора average отчета."""
        generator = get_report_generator('average')
        assert isinstance(generator, AverageReportGenerator)
    
    def test_get_user_agent_generator(self):
        """Тест получения генератора user_agent отчета."""
        generator = get_report_generator('user_agent')
        assert isinstance(generator, UserAgentReportGenerator)
    
    def test_get_unknown_generator(self):
        """Тест обработки неизвестного типа отчета."""
        with pytest.raises(SystemExit):
            get_report_generator('unknown_report_type') 