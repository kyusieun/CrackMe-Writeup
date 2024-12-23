def get_key(Name):
    Name[0] = ord(Name[0])

    Name[0] *= 0x772
    if Name[0] > 0xFFFFFFFF:
        Name[0] = Name[0] & 0xFFFFFFFF

    tmp = Name[0] * Name[0]
    if tmp > 0xFFFFFFFF:
        tmp = tmp & 0xFFFFFFFF

    Name[0] += tmp
    if Name[0] > 0xFFFFFFFF:
        Name[0] = Name[0] & 0xFFFFFFFF

    Name[0] *= 0x474
    if Name[0] > 0xFFFFFFFF:
        Name[0] = Name[0] & 0xFFFFFFFF

    Name[0] += Name[0]
    if Name[0] > 0xFFFFFFFF:
        Name[0] = Name[0] & 0xFFFFFFFF

    Name[1] = ord(Name[1])

    Name[1] += Name[0]
    if Name[1] > 0xFFFFFFFF:
        Name[1] = Name[1] & 0xFFFFFFFF

    Name[1] *= 0x772
    if Name[1] > 0xFFFFFFFF:
        Name[1] = Name[1] & 0xFFFFFFFF

    Name[1] += Name[1] * Name[1]
    if Name[1] > 0xFFFFFFFF:
        Name[1] = Name[1] & 0xFFFFFFFF

    Name[1] *= 0x474
    if Name[1] > 0xFFFFFFFF:
        Name[1] = Name[1] & 0xFFFFFFFF

    Name[1] += Name[1]
    if Name[1] > 0xFFFFFFFF:
        Name[1] = Name[1] & 0xFFFFFFFF

    Key = Name[1]
    return hex(Key)


Name = ["A", "A"]
Key = get_key(Name)
print(Key)


def calculate_key(Name):
    Name_copy = [ord(Name[0]), ord(Name[1])]

    Name_copy[0] *= 0x772
    if Name_copy[0] > 0xFFFFFFFF:
        Name_copy[0] = Name_copy[0] & 0xFFFFFFFF

    Name_copy[0] += Name_copy[0] * Name_copy[0]
    if Name_copy[0] > 0xFFFFFFFF:
        Name_copy[0] = Name_copy[0] & 0xFFFFFFFF

    Name_copy[0] *= 0x474
    if Name_copy[0] > 0xFFFFFFFF:
        Name_copy[0] = Name_copy[0] & 0xFFFFFFFF

    Name_copy[0] += Name_copy[0]
    if Name_copy[0] > 0xFFFFFFFF:
        Name_copy[0] = Name_copy[0] & 0xFFFFFFFF

    Name_copy[1] += Name_copy[0]
    if Name_copy[1] > 0xFFFFFFFF:
        Name_copy[1] = Name_copy[1] & 0xFFFFFFFF

    Name_copy[1] *= 0x772
    if Name_copy[1] > 0xFFFFFFFF:
        Name_copy[1] = Name_copy[1] & 0xFFFFFFFF

    Name_copy[1] += Name_copy[1] * Name_copy[1]
    if Name_copy[1] > 0xFFFFFFFF:
        Name_copy[1] = Name_copy[1] & 0xFFFFFFFF

    Name_copy[1] *= 0x474
    if Name_copy[1] > 0xFFFFFFFF:
        Name_copy[1] = Name_copy[1] & 0xFFFFFFFF

    Name_copy[1] += Name_copy[1]
    if Name_copy[1] > 0xFFFFFFFF:
        Name_copy[1] = Name_copy[1] & 0xFFFFFFFF

    Key = Name_copy[1]
    return Key


def find_name_for_key(target_key_prefix):
    for char1 in range(32, 127):  # ASCII range
        for char2 in range(32, 127):
            Name = [chr(char1), chr(char2)]
            Key = calculate_key(Name)
            if (Key >> 16) == target_key_prefix:
                return Name, Key
    return None, None


target_key_prefix = 0x5D88
Name, Key = find_name_for_key(target_key_prefix)
if Name:
    print(f"Name = {Name}, Key = {hex(Key)}")
else:
    print("No valid Name found")
