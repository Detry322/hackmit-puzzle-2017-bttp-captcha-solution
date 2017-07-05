import hashlib

USERNAME = 'aaaaa'

def combiner_1(name):
    return USERNAME + name

def combiner_2(name):
    return USERNAME + ' ' + name

def combiner_3(name):
    return name + USERNAME

def combiner_4(name):
    return name + ' ' + USERNAME

def combiner_5(name):
    return name

def hasher_1(combined):
    m = hashlib.sha1()
    m.update(combined)
    return int(m.hexdigest(), 16)

def hasher_2(combined):
    m = hashlib.sha224()
    m.update(combined)
    return int(m.hexdigest(), 16)

def hasher_3(combined):
    m = hashlib.sha256()
    m.update(combined)
    return int(m.hexdigest(), 16)

def hasher_4(combined):
    m = hashlib.sha384()
    m.update(combined)
    return int(m.hexdigest(), 16)

def hasher_5(combined):
    m = hashlib.sha512()
    m.update(combined)
    return int(m.hexdigest(), 16)

def hasher_6(combined):
    m = hashlib.md5()
    m.update(combined)
    return int(m.hexdigest(), 16)

def hasher_7(combined):
    return hash(combined)

COMBINER = [combiner_1, combiner_2, combiner_3, combiner_4, combiner_5]
HASHER = [hasher_1, hasher_2, hasher_3, hasher_4, hasher_5, hasher_6, hasher_7]
LETTERS = [
    'abcdefghijklmnopqrstuvwxyz0123456789',
    '0123456789abcdefghijklmnopqrstuvwxyz',
    'abcdefghijklmnopqrstuvwxyz1234567890',
    '1234567890abcdefghijklmnopqrstuvwxyz'
]

SOLUTIONS = [
    ("4ib0","0ab4caa266dc638d6e33bee10d140068"),
    ("t11p","0adca873b77bfc3cf2849ee575675e1d"),
    ("fpq4","0ae40c764b8e47387a2bc50ee77ae156"),
    ("hvn8","0aeca397b477b6a4fcf551c51a082cf9"),
    ("80w1","0aee0e0b96d4a377f4511f4fd3041673"),
    ("atot","0b0058724d9bd2759ee1925dd64968bb")
]

def test(combiner, hasher, hash_part_length, hash_part_index, letter_arr, name, answer):
    combined = combiner(name)
    hashed = hasher(combined)
    hashed /= 2**hash_part_index
    hashed &= ((2**hash_part_length) - 1)
    result = letter_arr[hashed % len(letter_arr)]
    return result == answer

def main():
    for combiner in COMBINER:
        for hasher in HASHER:
            for hash_part_length in range(2, 64):
                for hash_part_index in range(128):
                    for letter_arr in LETTERS:
                        if all(test(combiner, hasher, hash_part_length, hash_part_index, letter_arr, name, answer[3]) for answer, name in SOLUTIONS):
                            print (combiner.__name__, hasher.__name__, hash_part_length, hash_part_index, letter_arr)
                            return
    print "SAD"

if __name__ == "__main__":
    main()
