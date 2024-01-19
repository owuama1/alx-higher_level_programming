#!/usr/bin/python3
"""
Script Name: metrics_script
Description: Reads stdin line by line, computes metrics, and prints statistics.
"""

import signal
import sys


def signal_handler(sig, frame):
    """
    Signal handler function for keyboard interruption (CTRL + C).
    """
    print_metrics()
    sys.exit(0)


def print_metrics():
    """
    Prints the computed metrics.
    """
    total_size = sum(file_sizes)
    print(f"File size: {total_size}")

    for status_code in sorted(status_codes):
        print(f"{status_code}: {status_codes[status_code]}")


if __name__ == "__main__":
    file_sizes = []
    status_codes = {}

    try:
        signal.signal(signal.SIGINT, signal_handler)

        for line in sys.stdin:
            elements = line.split()
            if len(elements) >= 9:
                status_code = elements[-2]
                file_size = elements[-1]

                file_sizes.append(int(file_size))

                if status_code in status_codes:
                    status_codes[status_code] += 1
                else:
                    status_codes[status_code] = 1

                if len(file_sizes) % 10 == 0:
                    print_metrics()

    except KeyboardInterrupt:
        print_metrics()
        sys.exit(0)
