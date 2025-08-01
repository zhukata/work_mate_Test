import sys
from tabulate import tabulate

from parsers import parse_args
from file_reader import read_files
from filters import filter_by_date
from reports import get_report_generator


def main():
    try:
        file_paths, report_name, date_filter = parse_args()
        data = read_files(file_paths)

        if not data:
            print("Нет данных для обработки")
            return

        if date_filter:
            data = filter_by_date(data, date_filter)
            if not data:
                print(f"Нет данных для даты: {date_filter}")
                return

        generator = get_report_generator(report_name)
        report = generator.generate(data)

        if not report:
            print("Не удалось создать отчет")
            return

        print(tabulate(
            report, 
            headers='keys', 
            showindex=range(0, len(report)),
        ))

    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем")
        sys.exit(1)
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()