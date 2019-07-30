filename = './57215648.py'
b = bytearray(1)
lines = 0
with open(filename, 'rb', buffering=0) as f:
    while (f.readinto(b)):
        if b[0] == 10:
            lines += 1

print(lines)