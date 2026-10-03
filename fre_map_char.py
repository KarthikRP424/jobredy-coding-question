s = "karthik"

q = ["l", "a", "r", "t", "h", "i", "k"]

ascii_map = {}

for char in s:
    ascii_map[char] = ord(char)

for char in q:
    if char in ascii_map:
        print(ascii_map[char])
    else:
        print(0)

print(ascii_map)