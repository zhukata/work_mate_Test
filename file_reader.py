import json
import sys
from typing import List, Dict, Any


def read_files(file_paths: List[str]) -> List[Dict[str, Any]]:
    """Читает данные из файлов и возвращает список словарей."""
    result = []
    for path in file_paths:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if line:
                        try:
                            result.append(json.loads(line))
                        except json.JSONDecodeError as e:
                            print(f"Ошибка JSON в файле {path}, строка {line_num}: {e}")
                            continue
        except FileNotFoundError:
            print(f"Файл не найден: {path}")
            sys.exit(1)
        except PermissionError:
            print(f"Нет прав доступа к файлу: {path}")
            sys.exit(1)
    return result 