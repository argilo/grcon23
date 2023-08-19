#!/usr/bin/env python3

import struct
import sys

smallest = 0
largest = 0

with open(sys.argv[1], "rb") as f:
    while True:
        data = f.read(4)
        if len(data) < 4:
            break
        value = struct.unpack("f", data)[0]
        smallest = min(value, smallest)
        largest = max(value, largest)
print(f"Smallest value: {smallest}")
print(f"Largest value: {largest}")