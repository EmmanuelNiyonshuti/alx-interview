#!/usr/bin/python3
"""
reads stdin line by line and computes metrics.
"""
import sys
import re


def parse_line(line):
    """
    checks and validates the format of the input line.
    Args:
        line - stdin line.
    Return:
        bool - 1 if the line matches the desired format, 0 otherwise.
    """

    pattern = (
        r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
        r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] '
        r'"GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)'
    )
    match = re.match(pattern, line.strip())
    return bool(match)


def print_metrics(total_size, status_codes):
    """ prints the metrics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def main():
    """
    read stdin line by line and computes metrics,
    after ever 10 lines, it prints current metrics.
    if interrupted by `Ctrl + C`,
    the script catches the `KeyboarInterrupt,` and exits cleanly.
    """
    total_size = 0
    count_lines = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in sys.stdin:
            count_lines += 1
            result = parse_line(line)
            if result:
                file_size = int(line.split()[-1])
                total_size += file_size
                status_code = int(line.split()[-2])
                if status_code in status_codes:
                    status_codes[status_code] += 1
            if count_lines % 10 == 0:
                print_metrics(total_size, status_codes)
    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        sys.exit(0)


if __name__ == "__main__":
    main()
