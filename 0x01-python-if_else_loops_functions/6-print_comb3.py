#!/usr/bin/python3
for i in range(10):
    for j in range(1, 10):
        if i >= j:
            continue
        print(f"{i}{j}", end=", " if i < 8 or (i == 8 and j < 9) else "\n")
