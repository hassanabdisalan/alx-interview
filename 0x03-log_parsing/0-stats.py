#!/usr/bin/python3
"""
Log parsing script
Reads stdin line by line and computes metrics:
- Total file size
- Count of status codes
"""

import sys

status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
total_size = 0
line_count = 0

def print_stats():
    """Prints the accumulated statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.strip().split()

        if len(parts) < 7:
            continue

        # Last two elements are status_code and file_size
        status_code = parts[-2]
        file_size = parts[-1]

        try:
            total_size += int(file_size)
        except ValueError:
            continue

        if status_code in status_codes:
            status_codes[status_code] += 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
