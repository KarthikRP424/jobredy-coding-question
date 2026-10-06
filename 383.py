class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        hash_map = {}

        for char in magazine:
            index = ord(char) - ord("a")
            if index in hash_map:
                hash_map[index] += 1
            else:
                hash_map[index] = 1
        

        for char in ransomNote:
            index = ord(char) - ord("a")
            if index not in hash_map or hash_map[index] == 0:
                return False
            else:
                hash_map[index] -= 1
                
        return True
    
    
print(Solution().canConstruct("aa", "ab"))  # False
print(Solution().canConstruct("aab", "baa"))  # True