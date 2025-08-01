import argparse
from typing import List, Tuple, Optional


def parse_args() -> Tuple[List[str], str, Optional[str]]:
    """Парсит аргументы командной строки."""
    parser = argparse.ArgumentParser(
        description="Читает лог файлы и показывает статистику"
    )
    parser.add_argument(
        "-f", "--file", 
        nargs='+', 
        type=str, 
        required=True,
        help="путь к лог файлу(ам)"
    )
    parser.add_argument(
        "-r", "--report", 
        type=str, 
        default="average",
        help="название отчета (по умолчанию: average)"
    )
    parser.add_argument(
        "-d", "--date", 
        type=str, 
        help="дата для фильтрации в формате YYYY-MM-DD"
    )
    args = parser.parse_args()
    return args.file, args.report, args.date 