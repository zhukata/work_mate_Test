# Log Analyzer

Скрипт для анализа лог-файлов в формате JSON. Показывает статистику по эндпоинтам, количеству запросов и среднему времени ответа.

## Установка

```bash
git clone https://github.com/zhukata/work_mate_Test.git
cd work_mate_Test
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Использование

```bash
python main.py --file example1.log --report average
```

### Параметры

- `-f, --file`: Путь к лог-файлу(ам) (обязательный)
- `-r, --report`: Тип отчета (по умолчанию: `average`)
- `-d, --date`: Дата для фильтрации в формате YYYY-MM-DD
- `-h, --help`: Вывод справки

### Примеры

```bash
# Базовый отчет
python main.py --file example1.log --report average

# Несколько файлов
python main.py --file example1.log example2.log --report average

# С фильтрацией по дате
python main.py --file example1.log --report average --date 2025-06-22

# Отчет по User-Agent
python main.py --file example1.log --report user_agent
```

## Структура проекта

```
work_mate_Test/
├── main.py              # Точка входа
├── parsers.py           # Парсинг аргументов
├── file_reader.py       # Чтение файлов
├── filters.py           # Фильтрация данных
├── reports.py           # Генераторы отчетов
├── requirements.txt     # Зависимости
├── tests/               # Тесты
└── README.md
```

## Тестирование

```bash
pytest tests/ -v
pytest tests/ --cov=. --cov-report=term-missing
```

## Формат лог-файлов

JSON, по одной записи на строку:

```json
{"@timestamp": "2025-06-22T13:57:32+00:00", "status": 200, "url": "/api/context/...", "request_method": "GET", "response_time": 0.024, "http_user_agent": "..."}
```

## Примеры запуска

[![asciicast](https://asciinema.org/a/kvCfIXvovo4cH2JaTnqGWv9j5.svg)](https://asciinema.org/a/kvCfIXvovo4cH2JaTnqGWv9j5)