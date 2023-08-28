#!/usr/bin/env python3

for filename in ("bits1.dat", "bits2.dat", "bits3.dat", "bits4.dat"):
    with open(filename, "rb") as f:
        bits = list(f.read())
        bits_inv = [b^1 for b in bits]
        for seq in (bits, bits_inv):
            for start_offset in range(8):
                ans = []
                for offset in range(start_offset, len(seq)-7, 8):
                    num = 0
                    for i in range(8):
                        num = (num << 1) | seq[offset+i]
                    ans.append(num)
                ans = bytes(ans)
                if b"flag" in ans:
                    print(filename, bytes(ans))
