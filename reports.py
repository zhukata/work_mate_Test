import sys
from typing import List, Dict, Any


class ReportGenerator:
    """Базовый класс для генерации отчетов."""
    def generate(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        raise NotImplementedError


class AverageReportGenerator(ReportGenerator):
    """Генератор отчета среднего времени ответа."""
    def generate(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        if not data:
            return []

        url_groups = {}
        for item in data:
            url = item.get('url')
            if url:
                if url not in url_groups:
                    url_groups[url] = []
                url_groups[url].append(item)

        report = []
        for url, items in url_groups.items():
            total = len(items)
            response_times = [item.get('response_time', 0) for item in items]
            avg_response_time = round(sum(response_times) / total, 3) if response_times else 0
            
            report.append({
                'handler': url,
                'total': total,
                'avg_response_time': avg_response_time
            })

        return sorted(report, key=lambda x: x['total'], reverse=True)


class UserAgentReportGenerator(ReportGenerator):
    """Генератор отчета количества запросов по User-Agent."""
    def generate(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        if not data:
            return []

        ua_groups = {}
        for item in data:
            user_agent = item.get('http_user_agent', 'Unknown')
            if user_agent not in ua_groups:
                ua_groups[user_agent] = 0
            ua_groups[user_agent] += 1

        report = []
        for ua, count in ua_groups.items():
            report.append({
                'user_agent': ua[:50] + '...' if len(ua) > 50 else ua,
                'count': count
            })

        return sorted(report, key=lambda x: x['count'], reverse=True)


def get_report_generator(report_type: str) -> ReportGenerator:
    """Получает генератор отчета по его типу."""
    generators = {
        'average': AverageReportGenerator(),
        'user_agent': UserAgentReportGenerator(),
    }
    
    if report_type not in generators:
        print(f"Неизвестный тип отчета: {report_type}")
        print(f"Доступные типы: {', '.join(generators.keys())}")
        sys.exit(1)
    
    return generators[report_type] 