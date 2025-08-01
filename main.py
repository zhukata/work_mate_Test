import argparse
import json

from tabulate import tabulate

def parse():
    parser = argparse.ArgumentParser(
        description="Read log files and show info"
    )
    parser.add_argument("-f", "--file", nargs='+', type=str, help="log file")
    parser.add_argument("-r", "--report", type=str, help="name of report")
    args = parser.parse_args()
    return (args.file, args.report)

print(parse())

def normalize_path(path):
    return

def readfiles(args):
    paths, report = args
    result = []
    for path in paths:
        with open(path, 'r') as f:
            for str in f.readlines():
                result.append(json.loads(str))
    return result

# print(readfiles(parse()))

def make_report(data):
    unique_urls = set(map(lambda x: x['url'], data))
    report = []
    # number = -1
    for i in unique_urls:
        all_matches = list(filter(lambda x: x['url'] == i, data))
        total = len(all_matches)
        avg_response_time = round(sum(map(lambda x: x['response_time'], all_matches)) / total, 3)
        log_line = {'handler': i, 'total': total, 'avg_response_time': avg_response_time}
        report.append(log_line)
    return sorted(report, key=lambda x: x['total'], reverse=True)

# print(make_report(readfiles(parse())))
print(tabulate(make_report(readfiles(parse())), headers='keys', showindex='default'))