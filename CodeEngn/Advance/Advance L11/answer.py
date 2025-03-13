def generate_serial(name):
    realSerial = ""
    buf = 0x3B10
    for c in name:
        buf += ord(c) * 0x426C

    for _ in range(8):
        mod = buf % 0xF
        buf //= 0xF
        char_val = 0x30 + mod
        if char_val > 0x39:
            char_val += 8
        realSerial += chr(char_val)
        buf *= 2

    return realSerial


def generate_serial_with_seed(seed):
    realSerial = ""
    buf = 0x3B10
    buf += seed

    for _ in range(8):
        mod = buf % 0xF
        buf //= 0xF
        char_val = 0x30 + mod
        if char_val > 0x39:
            char_val += 8
        realSerial += chr(char_val)
        buf *= 2

    return realSerial


res = generate_serial("testtest")
print(res)


seed = 1
while True:
    res = generate_serial_with_seed(seed)
    if res == "94E7DB1B":
        print(f"Found seed: {seed}")
        print(res)
        break
    seed += 1
