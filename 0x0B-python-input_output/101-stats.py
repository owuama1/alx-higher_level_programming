#!/usr/bin/python3
"""
Script Name: metrics_script
Description: Read stdin line by line, accumulate metrics, and print statistics.
"""

from collections import Counter
import sys


def print_stats(total_size, status_counts):
    """
    Print accumulated metrics.

    Args:
        total_size (int): The total size of the files read so far.
        status_counts (Counter): It tracks the occurrence of each status code.
    """
    print(f"File size: {total_size}")
    for code, count in sorted(status_counts.items()):
        print(f"{code}: {count}")


if __name__ == "__main__":
    total_size = 0
    status_counts = Counter()
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(total_size, status_counts)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                total_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    status_counts[line[-2]] += 1
            except IndexError:
                pass

        print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise
