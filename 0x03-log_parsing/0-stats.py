#!/usr/bin/python3
"""Reads stdin line by line and computes metrics."""

import sys
import signal

# Initialize counters
total_size = 0
status_counts = {}
valid_statuses = {'200', '301', '400', '401', '403', '404', '405', '500'}
line_count = 0


def print_stats():
    """Prints the collected statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))


try:
    for line in sys.stdin:
        try:
            parts = line.strip().split()

            if len(parts) < 7:
                continue

            status_code = parts[-2]
            file_size = parts[-1]

            if status_code in valid_statuses:
                status_counts[status_code] = status_counts.get(status_code, 0) + 1

            total_size += int(file_size)
            line_count += 1

            if line_count % 10 == 0:
                print_stats()
        except Exception:
            continue

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
