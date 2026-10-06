s = "karthik"

p = ["r", "a", "t", "h", "i", "k"]

hash_map = [0]*26


for char in s:
    index = ord(char) - ord('a')
    hash_map[index]+=1
    
for char in p:
    index = ord(char) - ord('a')
    print(hash_map[index])
    
print(hash_map)